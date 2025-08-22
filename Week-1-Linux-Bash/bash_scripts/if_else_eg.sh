#!/bin/bash
DISK_USAGE=$(df / | awk '{print $5}' | sed 's/%//g')
THRESHOLD=80

if [ "$DISK_USAGE" -gt "$THRESHOL" ]; then
     echo "ALERT! Disk usage is $DISK_USAGE%"
else
     echo "Disk Usage is OK: $DISK_USAGE%" 
fi
