#!/bin/zsh
#Programa para encontrar primos em sh
echo "3"
((var=4))
while [ $var -le  100000 ]
do
    ((var2=2))
    ((var3=0))    
    while [ $var2 -lt $var ]
    do
        ((var4=$var % $var2 ))
        if [ $var4 -eq 0 ]
        then
            ((var3=1))
            break
        fi 
        ((var2=$var2 + 1)) 
    done
    if [ $var3 -eq 0 ]
    then
       echo "$var" 
    fi
    ((var=$var + 1))
done
