import logging

logging.basicConfig(
	filename="app.log",
	filemode='a',
	level=logging.INFO,
	format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("This is informational")
logging.critical("FS excedded critical utilization")
