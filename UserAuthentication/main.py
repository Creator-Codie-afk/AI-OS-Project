# main.py - User Authentication Module
import hashlib
import uuid
import random

# Simple in-memory user database for demonstration purposes
user_db = {}
session_db = {}
user_roles = {}

def register_user(username, password, role):
    """
    Function to register a new user with a specific role.
    """
    if username in user_db:
        return "User already exists."
    # Hash the password for secure storage
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_db[username] = hashed_password
    user_roles[username] = role
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

def multi_factor_authentication(username):
    """
    Function to perform multi-factor authentication.
    """
    if username not in session_db:
        return "User not authenticated."
    # Simulate sending a verification code (e.g., via email or SMS)
    verification_code = random.randint(100000, 999999)
    print(f"Verification code sent to user: {verification_code}")
    entered_code = int(input("Enter the verification code: "))
    if entered_code == verification_code:
        return "Multi-factor authentication successful."
    return "Multi-factor authentication failed."

def check_user_role(username, role):
    """
    Function to check if a user has a specific role.
    """
    return user_roles.get(username) == role

if __name__ == "__main__":
    # Test the user authentication functions
    username = input("Enter username to register: ")
    password = input("Enter password: ")
    role = input("Enter user role (admin/user): ")
    print(register_user(username, password, role))

    username = input("Enter username to authenticate: ")
    password = input("Enter password: ")
    print(authenticate_user(username, password))

    print(multi_factor_authentication(username))

    role_to_check = input("Enter role to check: ")
    print(f"User has role {role_to_check}: {check_user_role(username, role_to_check)}")
