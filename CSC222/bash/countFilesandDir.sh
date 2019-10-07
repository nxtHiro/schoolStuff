count(){
     for i "$1"
     do
     if [ -f $i ]
          ((f++))
     elif [ -d $i ]
          ((d++))
          count "$i"
     fi
     done
}


f=0
d=0
