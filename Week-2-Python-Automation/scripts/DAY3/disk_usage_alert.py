import subprocess

threshold = 80

#get root disk usage
output = subprocess.getoutput("df -h / | tail -1).split()
used_percentage = int(output[4].replace("%", "")

if used_percentage > threshold:
	print(f"Disk usage is high! : {used_percentage})
else:
	print(f"Disk usage is normal. : {used_percentage})
