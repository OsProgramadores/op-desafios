"""
    @Author: Thiago Felix.
    Propósito: Resolução do desafio-2.
    Detalhes: Metodo usado para a resolução Crivo de Erastóstenes.
"""
def verificaPrimos(number: int) -> list:
    prime = []

    for num in range(2, number):
        if not(num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0) or num in [2, 3, 5, 7]:
            prime.append(num)
            
    return prime

if __name__ == "__main__":
    print(verificaPrimos(1000))