#Script that use os to check if /tmp exists

import os

try:
	# check if /tmp exists
	if os.path.exists("/tmp"):
		print("Tmp folder found")
	else:
		#If Missing create it
		os.makedirs("/tmp")
		print("/tmp folder was missing, created now")
except Exception as e:
	print("Error:", e)
finally:
	print("Script Finished.")
