import logging
from logging.handlers import RotatingFileHandler


#Step 1 set logger
logger = logging.getLogger("jay_app")
logger.setLevel(logging.DEBUG)


#Step 2: set console Handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

#Step 3: File handler with rotation
File_Handlers = RotatingFileHandler(
	"jay.log",
	maxBytes=300,
	backupCount=3
)
File_Handlers.setLevel(logging.DEBUG)

#Step 4: Formatter(Same format for both)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
File_Handlers.setFormatter(formatter)

#Step5: Add handlers to logger
logger.addHandler(ch)
logger.addHandler(File_Handlers)

for i in range(50):
	logging.info(f"Info message {i}") 
	logging.debug(f"Debug message {i}")
	logging.warning(f"Warning message {i}")
	logging.error(f"Error Message {i}")
	logging.critical(f"Critical message {i}")
