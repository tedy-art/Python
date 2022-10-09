import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "tejas@123",
    database = "mydatabase"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = 'Apple st 662'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)