# exceptions to handle error gracefully

try:
	#code that may throw error
	x=10/0
except ZeroDivisionError:
	print("Cannot Divide by zero")

#======================================

try:
	#unable to open a file
	f = open("data.txt")
	print(f.read())
except FileNotFoundError:
	print("File not found")
finally:
	print("Cleaning up resources ...")

#====================================

try:
	f = open("data.txt")
except FileNotFoundError:
	print("File missing")
else:
	print("File opened successfully")
	f.close()

# ==== Raising own exception

def deploy(service):
	if service not in ["nginx", "mysql"]:	
		raise ValueError("Unsupported service!")
	print(f"Deploying {service}...")

# === Custome Exceptions

def DiskFullError(Exception):
	pass

try:
	raise DiskFullError("Disk is full, Cannot continue deployment")
except DiskFullError as e:
	print(f"Error: {e}")
