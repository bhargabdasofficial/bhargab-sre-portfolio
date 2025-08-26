import os
import logging

#configure logging

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s - %(levelname)s - %(message)s",
	filename="failed_login_monitor.log", #Logs will be written here
	filemode='a'  #append mode
)

log_file = "/var/log/auth.log"

if not os.path.exists(log_file):
	logging.error(f"File {log_file} not found!")
else:
	try:
		with open(log_file,"r") as f:
		    content=f.read()

		failed_count = content.count("Failed")
		
		if failed_count < 3:
		    logging.info(f"Failed login attempts: {failed_count}")
		elif 3 <= failed_Count <= 5:
		    logging.warning(f"Failed login attemos {failed_count}")
		else:
		    logging.error(f"Too many failed login attempts: {failed_counts}")
	
	except Exception as e:
		logging.critical(f"Error reading {log_file}:{e}")
