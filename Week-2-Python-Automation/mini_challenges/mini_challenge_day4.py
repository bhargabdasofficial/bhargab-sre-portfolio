#Script that use os to check if /tmp exists

import os

try:
	# check if /tmp exists
	if os.path.exists("/tmp"):
		print("Tmp folder found")
	else:
		# Raise custom exception if not found
		raise FileNotFoundError("/tmp folder not found")
except FileNotFoundError as e:
	print("Error:", e)
finally:
	print("Script Finished.")
