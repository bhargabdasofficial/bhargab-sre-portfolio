#!/bin/bash
#Process Monitor script
#Checks if nginx is running and starts it if not

PROCESS="nginx"

#pgrep checks if process is running
#if ... then
# In Bash, commands have exit status; 0 -> success(true) ; Non Zero -> failure(false)
# pgrep "$PROCESS": Returns 0 if atleast one process with the name is running; Returns 1 if no such process is running
# > /dev/null ; redirect the output to /dev/null (a special blackhole file that discards anything written to it)

if pgrep "$PROCESS" > /dev/null; then
    echo "$PROCESS is running fine"
else
    echo "$PROCESS is not runnin. Starting $PROCESS ..."
    sudo systemctl start nginx
fi
