#os module allowa python to interact with OS

import os

#get current working directory
cwd = os.getcwd()
print("Current Directory:", cwd)

#List files in a directory
files = os.listdir("/var/log")
print(files)

#Check if a path exists
if os.path.exists("/tmp/test.log"):
	print("File Exists")
else:
	print("File doesn't exists")


