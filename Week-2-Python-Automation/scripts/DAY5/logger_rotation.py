import logging
from logging.handlers import RotatingFileHandler

#create logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

#Rotating File Handler
handler = RotatingFileHandler(
	"bhadas.log", #Log file Name
	maxBytes=200, # max size in bytes before rotation(~200 bytes here)
	backupCount=5 # keep last 5 log file
)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

for i in range(30):
	logger.debug(f"Log entry number {i}")

