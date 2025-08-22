#!/bin/bash

#DIR=/Users/bhargabdas/bhargab-sre-portfolio/bhargab-sre-portfolio/Week-1-Linux-Bash/bash_scripts/*
DIR=($(pwd)) # Looks for file in current working dir

echo "Checking files under current working directory :$DIR"


# commenting previous script
#for file in "$DIR"/*; do
#       echo "File: $file"
#done 

# update for loop for more clarity
for file in "$DIR"/*; do
    if [ -f "$file" ]; then # -f tests if the given path is a regular file (not a directory, not a symlink)
       echo "File: $(basename $file)" # extracts just the filename without the path
    fi
done 
