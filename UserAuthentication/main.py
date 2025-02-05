# main.py - User Authentication Module
import hashlib

# Simple in-memory user database (for demonstration purposes)
user_db = {}

def register_user(username, password):
    """
    Function to register a new user.
    """
    if username in user_db:
        return "User already exists."
    # Hash the password for secure storage
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_db[username] = hashed_password
    return "User registered successfully."

def authenticate_user(username, password):
    """
    Function to authenticate a user.
    """
    # Hash the input password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    stored_password = user_db.get(username)
    if stored_password and stored_password == hashed_password:
        return True
    return False

if __name__ == "__main__":
    # Test user registration and authentication
    while True:
        action = input("Enter 'register' to register or 'login' to authenticate: ").strip().lower()
        if action == 'register':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(register_user(username, password))
        elif action == 'login':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate_user(username, password):
                print("Authentication successful.")
            else:
                print("Authentication failed.")
        else:
            print("Invalid action.")
