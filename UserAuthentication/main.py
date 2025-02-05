# main.py - User Authentication Module
import hashlib
import uuid

# Simple in-memory user database for demonstration purposes
user_db = {}
session_db = {}

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
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    stored_password = user_db.get(username)
    if stored_password and stored_password == hashed_password:
        # Create a session token for the user
        session_token = str(uuid.uuid4())
        session_db[username] = session_token
        return f"Authentication successful. Session token: {session_token}"
    return "Authentication failed."

def logout_user(username):
    """
    Function to log out a user and invalidate the session.
    """
    if username in session_db:
        del session_db[username]
        return "User logged out successfully."
    return "User not logged in."

if __name__ == "__main__":
    # Test user registration and authentication
    username = input("Enter username: ")
    password = input("Enter password: ")
    print(register_user(username, password))
    print(authenticate_user(username, password))
    print(logout_user(username))
