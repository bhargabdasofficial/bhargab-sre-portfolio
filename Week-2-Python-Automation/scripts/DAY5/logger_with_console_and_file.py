import logging

#set logger
logger = logging.getLogger("bhadas")
logger.setLevel(logging.DEBUG)

#console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

#file handler
fh = logging.FileHandler("application.log")
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

#Add handler
logger.addHandler(ch)
logger.addHandler(fh)

logger.info("This is information alert...")
logger.critical("This is critical alert") 
