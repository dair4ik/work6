import os

path = input("Input path:")

if os.path.exists(path):
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print(f"File name: {filename}")
    print(f"Directory: {directory}")
else:
    print("Path not found.")
