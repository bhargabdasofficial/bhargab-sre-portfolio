# Sub process allows python to run shell commands like ls, df, systemctl etc and stores it 

import subprocess

#run a simple command and get output
disk_usage =subprocess.getoutput("df -h /") #subprocess.getoutput -> runs command and return stdout as string
print(f"Disk Usage is : {disk_usge}")

#check if service is runnin
service_status = subprocess.getoutput("systemctl is-active nginx")
print(f"Nginx status is {sevice_status}")
