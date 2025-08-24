#Error will happen (eg. missing files, bad comments) 
# we use try / except to gracefully handle failures

try:
	f = open("missing.log", "r")
	print(f.read())
except FileNotFoundError as e:
	print(" File not found:", e)
finally:
	print("Always Executed (cleanup here)")

 
