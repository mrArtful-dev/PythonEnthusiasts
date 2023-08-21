import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=os.environ.get('DATABASE_PASSWORD'),
    database="enthusiasts_temp"
)

db.autocommit = True

mycursor = db.cursor()


mycursor.execute("SELECT * FROM student")

for person in mycursor:
    print(person)

mycursor.execute("SELECT * FROM sakila.actor ORDER BY first_name DESC")

first = mycursor.fetchmany(10)
print(first)
