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

def get_input(msg) -> str:
    return input(msg)


if __name__ == "__main__":
    MAX = (1 << 64) - 1
    while True:
        try:
            first_number: int = int(get_input("Informe o primeiro numero: "))
            last_number: int = int(get_input("Informe o ultimo numero: "))

        except ValueError:
            print("O primeiro e ultimo numero precisam ser interios positivos, nao letras!")
            continue

        if first_number <= 0 or last_number <= 0:
            print("O primeiro e ultimo numero precisam ser POSITIVOS! nao negativos ou ZEROS.")
            continue

        if last_number < first_number:
            print("O ultimo numero nao pode ser MENOR que o primeiro numero")
            continue

        if first_number > MAX or last_number > MAX:
            print("EPA! primeiro ou segundo excedem o valor limite. Tente denovo.")
            continue

        break

    print(f"\nPalindromos de {first_number} a {last_number}")
    for n in range(first_number, last_number+1):
        if is_palindrome(n):
            print(n)
