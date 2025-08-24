
#Reading files

with open("example.txt", "r") as f:
	print(f.readline()) 	#read one line
	print(f.readlines())	#read all lines as list

#Writing Files

with open("example.txt", "w") as f:
	f.write("Hello SRE!\n")
	f.write("Learning python file handling.\n")

#Appending iles

with open("example.txt", "a") as f:
	f.wrte("New log entry appended.\n)


