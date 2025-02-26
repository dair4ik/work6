import os

path = input("Input path: ")

existence = os.path.exists(path)
readability = os.access(path, os.R_OK)
writability = os.access(path, os.W_OK)
executability = os.access(path, os.X_OK)

print(f"Existence: {existence}")
print(f"Readability: {readability}")
print(f"Writability: {writability}")
print(f"Executability: {executability}")
