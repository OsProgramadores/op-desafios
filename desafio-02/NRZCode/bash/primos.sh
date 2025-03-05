#!/usr/bin/env bash
# Desafio 02 - [Os programadores](https://osprogramadores.com/desafios/d02)
# Imprime os números primos de 1 a 10000
is_prime() {
    local divisor \
        max_divisor=$(($1 / 2)) \
        number=$1
    for ((divisor = 2; divisor <= max_divisor; divisor++)); do
        ((number % divisor == 0)) && return 1
    done
    return 0
}

printf '%d\n' 1 2
for ((number = 3; number <= 10000; number+=2)); do
    if is_prime $number; then
        echo $number
    fi
done
