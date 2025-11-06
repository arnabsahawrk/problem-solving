import mysql.connector

dbName = "python_db"

dbConnection = mysql.connector.connect(
    host="localhost", user="root", password="arnab12345", database=dbName
)

cursor = dbConnection.cursor()

sqlQuery = """
UPDATE Student
SET name = 'Arnab'
WHERE name = 'Arnab Saha';
"""


cursor.execute(sqlQuery)
dbConnection.commit()

print("Insert into table successful")
