import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tejas@123",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
val = ("Ron","Highway 24")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount,"record inserted.")