import os

path = input("Enter file path: ")

if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print(f"File {path} deleted.")
else:
    print(f"Cannot be deletes {path}. File not exist.")
