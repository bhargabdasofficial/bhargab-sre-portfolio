import logging

logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Hi")
logging.debug("Debug initiate...")
logging.warning("Disk Usage is above major threshold.")
logging.error(" Error Observed")
logging.critical("Disk Usage is above critical threshold")
