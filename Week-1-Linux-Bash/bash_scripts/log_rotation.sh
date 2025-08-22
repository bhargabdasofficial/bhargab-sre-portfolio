#!/bin/bash
# Log rotation script
# Move all .log files from logs to archive/ with current date appended

#Directories
LOG_DIR="/home/devops_project/logs"
ARCHIVE_DIR="$LOG_DIR/archive"

#create archive directory if it doesn't exist
mkdir -p "$ARCHIVE_DIR

#Loop through all .log files

for file in "$LOG_DIR"/*.log; do
	if [ -f "$file" ]: then
	   mv "$file" "$ARCHIVE_DIR/$(basename $file)-$(date +%F)"
        fi
done 
