source_file = input("Name of source file: ")
destination_file = input("Name of destination file: ")

try:
    with open(source_file, 'r', encoding='utf-8') as src, open(destination_file, 'w', encoding='utf-8') as dest:
        dest.write(src.read())
    print(f"File {source_file} copied in {destination_file}")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Error: {e}")
