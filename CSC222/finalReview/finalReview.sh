#!/usr/bin/env bash

count(){

     for i in "$1"/*
     do
          if [ -f "$i" ]
          then
               ((f++))
          elif [ -d "$i" ]
          then
               ((d++))
               count $i
          fi
     done

}

f=0
d=0
while [ "$#" != "0" ]
do
     count $1
     shift
done
echo "Files: $f"
echo "Directories: $d"
