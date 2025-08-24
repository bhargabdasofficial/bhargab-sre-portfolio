import subprocess as sb


def get_disk_usage(path="/"):
	try:
	   output = sb.getoutput(f"df -h {path} | tail -1").split()
	   used_percent = int(output[4].replace("%",""))
	   return used_percent
	except Exception as e:
	   print("Error checking disk usage: {e}")
	   return None

# Example usage
usage = get_disk_usage("/")
if usage:
	print("Disk Usage: {usage}%")
	if usage > 80:
	   print(" Alert: Disk almost full!")
