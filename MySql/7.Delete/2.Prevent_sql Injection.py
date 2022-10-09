import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "tejas@123",
    database = "mydatabase"
)
mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Highway 24",)
mycursor.execute(sql,adr)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted.")