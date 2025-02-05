# main.py - File Management Module
import os

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

def update_file(file_path, content):
    """
    Function to update the content of a file.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(content)
        return "File updated successfully."
    except FileNotFoundError:
        return "File not found."

def delete_file(file_path):
    """
    Function to delete a file.
    """
    try:
        os.remove(file_path)
        return "File deleted successfully."
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    # Test file management functions
    directory = input("Enter directory path: ")
    print(f"Files in {directory}: {list_files(directory)}")
    
    file_path = input("Enter file path to create: ")
    content = input("Enter content for the file: ")
    print(create_file(file_path, content))
    
    print(f"Content of {file_path}: {read_file(file_path)}")
    
    update_content = input("Enter content to append to the file: ")
    print(update_file(file_path, update_content))
    
    print(f"Updated content of {file_path}: {read_file(file_path)}")
    
    delete_choice = input("Do you want to delete the file? (yes/no): ")
    if delete_choice.lower() == 'yes':
        print(delete_file(file_path))
