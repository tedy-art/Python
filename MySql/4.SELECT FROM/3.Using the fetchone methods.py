import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "tejas@123",
    database = "mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()
print(myresult)