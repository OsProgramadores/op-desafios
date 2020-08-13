#!/bin/bash
declare -i n1 n2
[[ $1 ]] && n1=$1 || read -p 'Digite um número positivo: ' n1
[[ $2 ]] && n2=$2 || read -p 'Digite o segundo número positivo: ' n2
((n1<n2)) || { n1[1]=$n2; n2=$n1; n1=${n1[1]}; }
for((;n1<=n2;n1++)); do
  rev=$(for((c=${#n1}-1;c>=0;c--)); do printf '%s' "${n1:c:1}"; done)
  if [[ $n1 == $rev ]]; then
    echo $n1
  fi
done
