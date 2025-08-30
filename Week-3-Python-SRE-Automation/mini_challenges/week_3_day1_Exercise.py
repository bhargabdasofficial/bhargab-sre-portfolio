
# Error Handling example

filename = input("Enter File name")

try:
	with open(filename, "r") as f:
		# read first 3 line
		for i in range(3):
		    line = f.readline()
		    if not line:
		        break
		    print(line.strip())

except FileNotFoundError:
	print(f"Error: The file '{filename}' was not found.")

except PermissionError:
	print(f"Error: You don't have permission to read file '{filename}'.")

else:
	print("File read successfully")

finally:
	print("Execution completed")


