# models/user.py
import mysql.connector
from flask import current_app
import bcrypt  # Import bcrypt for password hashing

def authenticate_user(email, password):
    """Checks if the user exists with the given credentials."""
    try:
        conn = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
            database=current_app.config['MYSQL_DB'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD']
        )
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()
        conn.close()

        if result:
            hashed_password = result[0]  # Get the hashed password from the database
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                return True  # Passwords match
            else:
                return False #Passwords do not match
        else:
            return False  # User not found

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False

def hash_password(password):
    """Hashes a password using bcrypt."""
    salt = bcrypt.gensalt()  # Generate a salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8') #return as a string.

# Example usage (for registration):
# hashed_password = hash_password("user_password")
# Insert hashed_password into the database