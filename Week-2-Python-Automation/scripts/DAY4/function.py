#function example

import subprocess as sb


def check_disk_usage(path='/'):
	output = sb.getoutput(f"df -h {path} | tail -1").split()
	used_percent = int(output[4].replace("%", "")
	return used_percent

print(check_disk_usage("/")) #Example usage


