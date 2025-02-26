filename = input("Input File Name: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    print(f"Number of rows: {len(lines)}")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Error: {e}")
