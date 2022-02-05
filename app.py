import mimetypes
from flask import Flask, request, Response
import json 

# custom error
class EmptyValueField(Exception):
    pass

app = Flask(__name__)

# hard coded animals list
animals = ['rabbit', 'rat', 'dog', 'cat', 'elephant', 'cow', 'monkey', 'snake']

# GET request
@app.get('/animals')
def get_animals():
    try:
        # converts list to JSON
        animals_json = json.dumps(animals, default=str)
        return Response(animals_json, mimetype="application/json", status=200)
    except Exception as e:
        print(e)
        return Response("Looks like something went wrong, please try again", mimetype="application/json", status=400)

# POST request
@app.post('/animals')
def post_animals():
    try:
        add_animal = request.json['add_animal']
        # conditional to raise custom error if value entered is empty
        if add_animal == "":
            raise EmptyValueField
        else:
            # add onto list
            animals.append(add_animal)
            return Response("An animal has been added to the list", mimetype="application/json", status=200)
    except KeyError:
        return Response("Invalid Key, please check data", mimetype="application/json", status=400)
    except EmptyValueField:
        return Response("You have not entered a value", mimetype="application/json", status=400)

# PATCH request
@app.patch('/animals')
def patch_animals():
    # 
    i = None
    old_animal = "cow"
    new_animal = "mad_cow"
    try:
        # finds index of element and replaces with new element
        i = animals.index(old_animal)
        animals[i] = new_animal
        print(i)
    except ValueError:
        return Response(f"looks like {old_animal} is not in the list", mimetype="application/json", status=400)        
    return Response("you have replaced an animal in the list", mimetype='application/json', status=200)

# DELETE request
@app.delete('/animals')
def delete_animals():
    #  
    delete_animal = "cat"
    try:
        # remove element from list
        animals.remove(delete_animal)
        return Response("you've successfully deleted an animal from the list", mimetype="application/json", status=200)
    except TypeError:
        return Response("looks like the animal has already been deleted", mimetype="application/json", status=400)
    except ValueError:
        return Response("looks like the animal has already been deleted", mimetype="application/json", status=400)


app.run(debug=True)