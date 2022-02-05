import dbcreds as c
import mariadb as db


# connect to database function
def connect_db():
    conn = None
    cursor = None
    try:
        conn = db.connect(user=c.user,
                          password=c.password,
                          host=c.host,
                          port=c.port,
                          database=c.database)
        cursor = conn.cursor()
    except db.OperationalError:
        print(
            "something went wrong with the DB, please try again in 5 minutes")
    except Exception as e:
        print(e)
        print("Something went wrong!")
    return conn, cursor


# disconnect from database function
def disconnect_db(conn, cursor):
    try:
        cursor.close()
    except Exception as e:
        print(e)
        print('cursor close error: what happened?')

    try:
        conn.close()
    except Exception as e:
        print(e)
        print('connection close error')

def get_animals_db():
    animals = []
    conn, cursor = connect_db()

    try:
        cursor.execute("select name from animals")
        animals_raw = cursor.fetchall()
    except db.OperationalError:
        print(
            "something went wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB Query, please file bug report")
    except:
        print("Something went wrong!")

    disconnect_db(conn, cursor)

    # create new list 
    for animal in animals_raw:
        animals.append(animal[0])

    return animals