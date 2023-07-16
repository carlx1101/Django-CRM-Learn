import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin123'
)


# Define cursor obkect 
cursorObject = database.cursor()

# Create database 
cursorObject.execute("CREATE DATABASE djangocrm")

print("Connection Sucessful !")