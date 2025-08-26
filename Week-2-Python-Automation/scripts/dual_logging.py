import os
import logging

#configure logging

#create logger
logger = logging.getlogger("AuthMonitor")
logger.setLevel(logging.DEBUG) #captures all levels (DEBUG -> Critical

#------ Handlers ----
#create filehandler (Logs everything to a file)
file_handler=logging.FileHandler("failed_login_monitor.log")
file_handler.setLevel(logging.DEBUG)

#consloe Handler
console_handler=logging.Streamhandler()
console_handler.setLevel(logging.INFO)

#------- Formatter ---
formatter = logging.Formatter(%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
conole_handler.setFormatter(formatter)

#------ Add handlers to logger ---
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# --- Script Logic ---
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
