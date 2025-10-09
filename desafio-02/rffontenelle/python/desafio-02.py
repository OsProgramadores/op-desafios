"""
Desafio 02 - https://osprogramadores.com/desafios/d02/
Lista todos os números primos entre 1 e 10000.
"""

def eh_primo(numero: int, lista_de_primos: list[int]):
    if numero == 2:
        return True
    if numero < 2 or numero % 2 == 0:
        return False
    for divisor in lista_de_primos:
        if divisor > numero ** 0.5:
            break
        if numero % divisor == 0:
            return False
    return True

if __name__ == "__main__":
    print("Listando números primos:")
    primos = []
    for num in range(1,10000):
        if eh_primo(num, primos):
            primos.append(num)
            print(f"{num}", end=" ")
    print("")

