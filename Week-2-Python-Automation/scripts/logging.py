import logging

#Basic logging config

logging.basicConfig(level=logging.info, format="%(asctime)s - %(levelname)s - %(message)s)")

logging.info("Starting the script...")
logging.warning("Disk usage is high.")
logging.error("Failed to read log file")
