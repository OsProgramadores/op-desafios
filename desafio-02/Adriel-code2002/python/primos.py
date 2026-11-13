"""Lista os números primos entre 1 e 10.000."""

# Autor: Adriel Mendes da Silva
# Desafio: 02 - Primos
# Linguagem: Python 3

from math import isqrt


def eh_primo(numero):
    """Verifica se um número é primo."""
    if numero < 2:
        return False

    for divisor in range(2, isqrt(numero) + 1):
        if numero % divisor == 0:
            return False

    return True


def main():
    """Lista todos os números primos até 10.000."""
    for numero in range(2, 10001):
        if eh_primo(numero):
            print(numero)


if __name__ == "__main__":
    main()
