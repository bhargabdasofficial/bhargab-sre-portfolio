#!/bin/bash
#user report script
#list currently logged in user and saves to users.txt

OUTPUT_FILE="$(pwd)/users.txt"
#echo $OUTPUT_FILE

# 'who' lists logged-in users
who > "$OUTPUT_FILE"

echo "User report saved to $OUTPUT_FILE"
