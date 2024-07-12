import mysql.connector

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
