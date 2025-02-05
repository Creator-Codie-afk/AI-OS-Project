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

import shutil
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Existing functions...

def organize_files_by_content(directory):
    """
    Function to organize files in a directory based on content similarity.
    """
    try:
        files = os.listdir(directory)
        file_contents = []
        for file in files:
            with open(os.path.join(directory, file), 'r') as f:
                file_contents.append(f.read())

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(file_contents)
        similarity_matrix = cosine_similarity(tfidf_matrix)

        for i, file in enumerate(files):
            similar_files = [files[j] for j in range(len(files)) if similarity_matrix[i][j] > 0.8]
            if len(similar_files) > 1:
                new_folder = os.path.join(directory, f"Similar_{i}")
                os.makedirs(new_folder, exist_ok=True)
                for similar_file in similar_files:
                    shutil.move(os.path.join(directory, similar_file), new_folder)
        return "Files organized successfully."
    except Exception as e:
        return f"Error organizing files: {e}"

def search_file_by_content(directory, query):
    """
    Function to search for a file in a directory based on content similarity.
    """
    try:
        files = os.listdir(directory)
        file_contents = []
        for file in files:
            with open(os.path.join(directory, file), 'r') as f:
                file_contents.append(f.read())

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(file_contents + [query])
        similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

        similar_files = [files[i] for i in range(len(files)) if similarity_scores[0][i] > 0.8]
        return similar_files if similar_files else "No similar files found."
    except Exception as e:
        return f"Error searching files: {e}"

def encrypt_file(file_path, key):
    """
    Function to encrypt a file using a simple XOR cipher.
    """
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

        encrypted_data = bytes([byte ^ key for byte in data])

        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

        return "File encrypted successfully."
    except Exception as e:
        return f"Error encrypting file: {e}"
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
