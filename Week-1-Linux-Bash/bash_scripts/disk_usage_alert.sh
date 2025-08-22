#!/bin/bash
# Disk Usage ALert Script
# Checks disk usage of /home and alerts if above threshold

#set threshold percentage
THRESHOLD=80

#Get disk usage of /(root)
# df -h: show disk usage
#awk 'NR>1 {print $5}' : get 5th column (%used)
#sed 's/%//g' : remove % sign
DISK_USAGE=$( df / | awk 'NR>1 {print $5}' | sed 's/%//g' )
echo $DISK_USAGE
#compare the current usage with threshold
if [ $DISK_USAGE -gt $THRESHOLD ]; then
   echo "ALERT! Disk usage is : $DISK_USAGE%"
else
   echo "Disk usage is OK! : $DISK_USAGE%"
fi
