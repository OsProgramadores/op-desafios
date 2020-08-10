#!/bin/bash
for num in {2..10000}; do
  primo=
  md=$((num/2))
  for((div=2;div<=md;div++)); do
    if ((num%div == 0)); then
      primo=0
      break
    fi
  done
  [[ $primo ]] || echo $num
done
