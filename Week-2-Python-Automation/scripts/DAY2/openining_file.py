#open a file in read mode

f = open("example.txt", "r")
print(f.read()) #read the entire file
f.close()

####MODES
# "r" -> read(default)
# "w" -> write(overwrites existing file)
# "a" -> append(adds to the end)
# "r+" -> read + write

# Best Practice  -> Use with

with open("example.txt","r") as f:
	data = f.read()
	print(data)
# no need to close, it's automatic
