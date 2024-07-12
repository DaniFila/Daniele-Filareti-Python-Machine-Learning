"""#query = "create database testpython"
query = "SHOW DATABASES"
my_cursor.execute(query)

for database in my_cursor:
print(database)"""



import mysql.connector

def connessione_server():
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        port = "8889"
        )
        print("Connessione avvenuta!")
    except:
        print("Errore")

def connessione_database():
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        port = "8889",
        database = "testpython"
        )
        my_cursor = mydb.cursor()
        print("Connessione avvenuta!")
        return my_cursor
    except:
        print("Errore")


my_cursor = connessione_database()
