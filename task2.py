import os

path = input("Input path: ")

if os.path.exists(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    print("Directories:", directories)
    print("Files:", files)
else:
    print("Path Not Found")
