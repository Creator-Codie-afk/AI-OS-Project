# main.py - File Management Module
import os
import hashlib

def list_files(directory):
    """
    Function to list files in a directory.
    """
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return "Directory not found."

def create_file(file_path, content):
    """
    Function to create a new file with the given content.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "File created successfully."
    except Exception as e:
        return f"Error creating file: {e}"

def read_file(file_path):
    """
    Function to read the content of a file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

def encrypt_file(file_path, key):
    """
    Function to encrypt a file using a simple XOR cipher.
    """
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted_data = bytes([b ^ key for b in data])
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        return "File encrypted successfully."
    except FileNotFoundError:
        return "File not found."

def search_files(directory, query):
    """
    Function to search for files containing a specific query.
    """
    try:
        files = os.listdir(directory)
        result = []
        for file in files:
            if query in file:
                result.append(file)
        return result
    except FileNotFoundError:
        return "Directory not found."

if __name__ == "__main__":
    # Test the file management functions
    directory = input("Enter directory path: ")
    print("Files in directory:", list_files(directory))

    file_path = input("Enter file path to create: ")
    content = input("Enter content for the file: ")
    print(create_file(file_path, content))

    print("Content of the file:", read_file(file_path))

    key = int(input("Enter encryption key (0-255): "))
    print(encrypt_file(file_path, key))

    query = input("Enter query to search for files: ")
    print("Files containing query:", search_files(directory, query))
