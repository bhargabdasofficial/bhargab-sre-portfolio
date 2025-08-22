#!/bin/bash

#DIR=/Users/bhargabdas/bhargab-sre-portfolio/bhargab-sre-portfolio/Week-1-Linux-Bash/bash_scripts/*
DIR=($(pwd)) # Looks for file in current working dir

echo "Checking files under current working directory :$DIR"

for file in "$DIR"/*; do
    if [ -f "$file" ]; then
       echo "File: $(basename $file)"
    fi
done 
