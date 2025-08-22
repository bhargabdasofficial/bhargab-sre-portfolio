#!/bin/bash
#Directory cleanup script
#cleanup all .tmp files older than 7 days in /tmp

TARGET_DIR="/tmp"

# find .tmp files older than 7 days and delete
find "$TARGET_DIR" -name "*.tmp" -type f -mtime +7 -exec rm -f {} \;

echo "Cleanup completed in $TARGET_DIR"
