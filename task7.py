for letter in range(65, 91):  
    filename = f"{chr(letter)}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"File {chr(letter)} created.")
print("Files from A to Z created.")
