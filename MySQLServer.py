#importing the mysql connector
import mysql.connector

#trying to connect with the mysql
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Moha@22nov",
    
)
##finding out i the connection is successfull
try:
    if conn.is_connected():
        print("Database 'alx_book_store' created successfully!")
except:
    print("Error:please try again")

conn.close()            