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
        print("Connessione avvenuta!")
        return mydb
    except:
        print("Errore")



mydb = connessione_database()
my_cursor = mydb.cursor()

#query = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
#query = "show tables"

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
"""val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')]"""

#val = ('Peter', 'Lowstreet 4'),
# my_cursor.execute(sql, val)

#my_cursor.executemany(sql, val)

#mydb.commit()

#print(my_cursor.rowcount, "record inserted.")


def inserimento(query,valori):
    my_cursor.executemany(query,valori)
    mydb.commit()
    print(my_cursor.rowcount, "record inserted.")

def seleziona(query):
    my_cursor.execute(query)
    risultati = my_cursor.fetchall()
    #risultati = my_cursor.fetchone()
    for risultato in risultati:
        print(risultato)

def eliminazione(query):
    my_cursor.execute(query)
    mydb.commit()
    print(my_cursor.rowcount, "record deleted.")


def aggiorna(query):
    my_cursor.execute(query)
    mydb.commit()
    print(my_cursor.rowcount, "record updated.")


#query1 = "select * from customers"

#seleziona(query)

#query = "delete from customers WHERE address = 'Mountain 21' "

#eliminazione(query)


#query = "UPDATE customers set address = 'cariati 7' WHERE address ='Lowstreet 4'"

#aggiorna(query)

#seleziona(query1)
