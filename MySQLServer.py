# Importing the MySQL connector
import mysql.connector

def create_database():
    try:
        # Step 1: Connect to MySQL without specifying a database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Moha@22nov"
        )

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            cursor.close()
        
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        #if 'conn' in locals() and conn.is_connected():  # Safe check before closing
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
