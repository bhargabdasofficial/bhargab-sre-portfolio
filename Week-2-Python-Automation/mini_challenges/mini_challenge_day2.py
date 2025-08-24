#Create a script that
#1 Create a file sre_notes.txt
#2 write 3 lines
#3 Read the file and print each line with numbers (like 1: Hello)


with open("sre_notes.txt", "w") as f:
	f.write("Hello world.\n")
	f.write("Learning python File handling\n")
	f.write("Thanks")

with open("sre_notes.txt", "r") as f:
	lines = f.readlines()

# Print each line with line numbers

for i, line in enumerate(lines,start=1):
	print(f"{i}: {line.strip()}")

#######
#enumerate takes an iterable(like a list, file lines, etc) and return each item along with its index

# syntax
# enumerate(iterable, start=0)
# iterable -> any list, tuple or iterator
# start -> optional, which number the index should start from(default=0)

	
