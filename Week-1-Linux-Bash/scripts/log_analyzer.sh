#!/bin/bash
#log_analyzer.sh
#Count how many times "ERROR" Appears in /var/log/syslog

LOG_FILE="/var/log/syslog"
COUNT=$(grep -c "ERROR" $LOG_FILE)

echo "Total ERROR entries in $LOGFILE: $COUNT"

