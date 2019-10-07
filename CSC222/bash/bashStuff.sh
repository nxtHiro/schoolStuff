#!/bin/bash

# environment variables
# $$ (pid of the script)
# $# (number of input params)
# $0 (name of the script)
# $1 (first param)
# $2 (second params)
# ...
# $@ (arguements list - iterative)
# $* (arguement list)


# variable
# var=value
var=10
var2=CSC222

# print to the console
echo $var
echo $var2

# arithmetic operation
# let <arithmetic expression>
var1=1
var2=2
let var3=$var1+$var2
let var3++

# expression
# expr item1 <operator> item2
expr 4 + 5

# read a variable value
# read

echo "Enter an int value"
read var

# file.sh
# run: bash file.sh
# or ./file.sh
read -p var
#prompt
read -sp var2
#silent prompt for passwds


# quotes
# single quotes -> literal string
#    echo 'var is $var'
#    "var is $var"
# double quotes -> replaces variables with values
#    echo "var is $var"
#    "var is <value>"
# back quotes `
#    execute a command
#    echo "today is `date`"

#if <condition
#then
#     code
#elif <conditiion>
#else
#fi

#if operators
# !expr
# n string   string not empty
# z string   string empty
# space with equals here
