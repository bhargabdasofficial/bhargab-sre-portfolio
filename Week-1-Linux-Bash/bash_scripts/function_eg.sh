#!/bin/bash

greet() {
    echo "Hello, $1"
}

greet $1 

# To run this > bash scriptname.py <username> 
# name will be given as input to the function which is $1 
