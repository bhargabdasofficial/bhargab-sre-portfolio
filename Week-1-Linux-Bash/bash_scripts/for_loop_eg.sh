#!/bin/bash

#DIR=/Users/bhargabdas/bhargab-sre-portfolio/bhargab-sre-portfolio/Week-1-Linux-Bash/bash_scripts/*
DIR=($(pwd)) # Looks for file in current working dir

echo "Checking files under :$DIR"

for file in $DIR; do
    echo "File: $file"
done 
