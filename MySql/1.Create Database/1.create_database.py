import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "tejas@123"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")