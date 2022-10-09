import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "tejas@123",
    database = "mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customer (name VARCHAR(255),address VARCHAR(255))")