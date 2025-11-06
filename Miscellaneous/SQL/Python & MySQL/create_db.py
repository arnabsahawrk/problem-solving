import mysql.connector

dbConnection = mysql.connector.connect(
    host="localhost", user="root", password="arnab12345"
)

print(dbConnection)


dbName = "python_db"

cursor = dbConnection.cursor()

sqlQuery = "CREATE DATABASE " + dbName


cursor.execute(sqlQuery)
