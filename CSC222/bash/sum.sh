#!/bin/bash

add(){
     ((total+=$1))
}

total=0
while [ $1 ]
do
add $1
shift
done
echo "sum = $total"
