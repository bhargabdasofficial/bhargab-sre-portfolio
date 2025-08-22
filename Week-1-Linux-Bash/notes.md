# Week-1-Linux-Bash Notes

📘 Week 1 – Linux & Bash Basics
🔹 1. Linux Basics
File System Structure
/ → Root of the file system


/home → User home directories


/etc → Config files


/var → Logs, variable data


/tmp → Temporary files


/bin, /usr/bin → Commands


Important Commands
ls, pwd, cd → Navigation


touch, mkdir, rm, rmdir → File/dir operations


cp, mv → Copy/move


cat, less, head, tail → View files


man <command> → Help



🔹 2. Permissions
Format: -rwxr-xr--


r = read, w = write, x = execute


Owner | Group | Others


Change Permissions
chmod 755 file.sh
chown user:group file.sh


🔹 3. Processes
ps aux → View processes


top, htop → Live monitoring


kill -9 <pid> → Kill process


Check if Process Running
if pgrep "nginx" > /dev/null; then
    echo "nginx is running"
else
    echo "nginx is not running"
fi

🔎 pgrep → returns PID if process exists.
 > /dev/null → suppress output.

🔹 4. File Search (find)
find /var/log -name "*.log"

Useful Flags
-type f → files


-type d → directories


-mtime +7 → modified more than 7 days ago


-mtime -7 → modified within last 7 days


Action with -exec
find /tmp -name "*.tmp" -type f -mtime +7 -exec rm -f {} \;

-exec … {} \; → run a command on each result.


{} → placeholder for filename.


Other use cases:
# Compress old logs
find /var/log -name "*.log" -mtime +30 -exec gzip {} \;

# Change permissions of .sh files
find . -name "*.sh" -exec chmod +x {} \;


🔹 5. Text Processing (Basics)
grep
grep "error" /var/log/syslog

awk
awk '{print $1, $2}' /etc/passwd

Field separator = space by default.


$1, $2 = first, second column.


sed
sed 's/error/issue/g' logfile.log

s/pattern/replacement/g → substitute globally.



🔹 6. Bash Scripting
Script 1 – Move Old Logs
#!/bin/bash
LOG_DIR="/var/log/myapp"
ARCHIVE_DIR="/var/log/myapp/archive"

mkdir -p "$ARCHIVE_DIR"

for file in "$LOG_DIR"/*.log; do
    if [ -f "$file" ]; then
        mv "$file" "$ARCHIVE_DIR/$(basename $file)-$(date +%F)"
        echo "Moved $file to archive"
    fi
done

Script 2 – Cleanup Temp Files
#!/bin/bash
TARGET_DIR="/tmp"

find "$TARGET_DIR" -name "*.tmp" -type f -mtime +7 -exec rm -f {} \;
echo "Old .tmp files cleaned"


🔹 7. Mini Challenge (Practice)
Create a directory structure under /home/devops_project:


/home/devops_project
 ├── logs/
 ├── scripts/
 └── archive/

Write a script that:


Moves logs from logs/ → archive/ with a timestamp.


Deletes .tmp files older than 7 days.


Prints a summary after completion.



✅ End of Week 1 Notes


