#!/bin/bash
num=1
while ((num <= 10000)); do
  primo=1
  div=$((num/2))
  while ((div > 1)); do
    if ((num%div == 0)); then
      primo=0 # $num não é primo
      break
    else
      ((div--))
    fi
  done
  ((primo == 1)) && echo "$num" # $num é primo
  ((num++))
done
