# Marco Flores

#!/usr/bin/env bash

usage(){
     echo "Usage: bash one.sh val [val [ ... ] ]"
     echo " e.g., bash one.sh 17 49 3 466"
}

prod(){
     ((total=$total*$1))
}

if [  $# -le 1 ] 
	then 
		usage
		exit 1
	fi

total=1
nums="The prod of "

while [ $1 ]
do
     prod $1
     nums+=$1" "
     shift
done

echo $nums"is $total"
