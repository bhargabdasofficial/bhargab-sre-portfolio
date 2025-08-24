## This script is created to check if log file exists and if it exists than print the last five lines(like tail -n 5), else print file doesn't exists

import os
import subprocess

#path to log file
log_file = "/var/log/syslog"

#Step1 check if file exists
if os.path.exists(log_file):
	print(f" Log file {log_file} exists.})
	
	#step 2: run tail command to get last 5 lines
	last_lines = subprocess.getoutput(f"tail -n 5 {log_file}")

	print("\n--- Last 5 lines ---")	
	print(last_lines)
else:
	print("File not found!")
