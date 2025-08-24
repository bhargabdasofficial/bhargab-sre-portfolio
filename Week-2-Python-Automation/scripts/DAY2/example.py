
# Count how many times "ERROR" appears in a log file
with open("app.log", "r") as log:
	errors=0
	for line in log:
	    if "ERROR" in line:	
		errors += 1
	print(f"Total errors found: {errors}")

