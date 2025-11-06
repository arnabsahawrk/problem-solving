import mysql.connector

dbName = "python_db"

dbConnection = mysql.connector.connect(
    host="localhost", user="root", password="arnab12345", database=dbName
)

cursor = dbConnection.cursor()

sqlQuery = """
CREATE TABLE Student(
    roll VARCHAR(10),
    name VARCHAR(30)
);
"""


cursor.execute(sqlQuery)
print("Create table successful")
