#!/bin/bash
#cleanup_logs.sh


#!/bin/bash
#cleanup_logs.sh

DIR="/tmp/logs"
find $DIR -name "*.log" -type f -mtime +7 -print -exec rm {} \;

echo "Old logs deleted from $DIR"
