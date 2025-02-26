filename = input("Input File Name: ")
my_list = input("Input elements: ").split(",")

with open(filename, 'w', encoding='utf-8') as file:
    for item in my_list:
        file.write(f"{item.strip()}\n")

print(f"List in {filename}")
