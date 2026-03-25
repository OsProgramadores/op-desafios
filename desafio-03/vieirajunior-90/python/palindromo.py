"""
Solução do Desafio 03 por Junior Vieira
"""
def palindromo(start=1, end=10000):
    """
    Função para procurar por algarismos palíndromos
    """
    while start <= end:
        valor = str(start)
        if valor == valor[::-1]:
            print(f'[{valor}]', end='')
        start += 1
    print()
palindromo()
