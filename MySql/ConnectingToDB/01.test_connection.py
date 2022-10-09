# Check mysql install or not
import mysql.connector

# Create Connection between python and mysql database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tejas@123"
)
print(mydb)