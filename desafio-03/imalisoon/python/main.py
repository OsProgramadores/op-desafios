#!/usr/bin/env python3
# author: Alison gh: @imalisoon

def is_palindrome(number: int) -> bool:
    number_copy: int = number
    number_reverse: int = 0

    while number_copy > 0:
        last_digit: int = number_copy % 10
        number_reverse = number_reverse * 10 + last_digit

        number_copy = number_copy // 10

    return number_reverse == number

def get_input(msg: str) -> int:
    digit: int = int()
    while True:
        try:
            digit = int(input(msg))
        except ValueError:
            print("Informe apenas NUMEROS!")
            continue
        break

    return digit


if __name__ == "__main__":
    MAX = (1 << 64) - 1
    while True:
        first_number: int = get_input("Informe o primeiro numero: ")
        if first_number < 0:
            print("Primeiro numero precisar ser um INTEIRO POSITIVO!")
            continue

        if first_number > MAX:
            print("Primeiro numero excede o valor limite!")
            continue

        break

    while True:
        last_number: int = get_input("Informe o ultimo numero: ")
        if last_number < 0:
            print("Ultimo numero precisar ser um INTEIRO POSITIVO!")

            continue
        if last_number > MAX:
            print("Ultimo numero excede o valor limite!")
            continue

        if last_number < first_number:
            print("Ultimo numero nao pode ser menor que o Primeiro!")
            continue

        break

    print(f"\nPalindromos de {first_number} a {last_number}")
    for n in range(first_number, last_number+1):
        if is_palindrome(n):
            print(n)
