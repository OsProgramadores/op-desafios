# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:32:46 2019

Desafio 02 - Listar todos os números primos de 1 à 10000

@author: Aline
"""

def isPrime(primes, n):
    # Função para definir se um número é primo e adicionar ao array de primos
    isNPrime = True
    if (n > 3):    
        # Como 2 e 3 são primos, a verificação começa quando n > 3
        for i in primes:
            # Para verificar se um número é primo, verificamos se ele é
            # divisível pelos outros número primos encontrados menores que n
            if (n%i == 0):
                # Caso ele seja divisível, ele não é primo
                isNPrime = False
                break
    
    if (isNPrime == True):
        # Se ele passou por todo o array de primes e não encontrou um outro
        # número que ele seja divisível, a função adiciona o número ao array
        # de primos
        primes.append(n)
    
    # No fim a função retorna o array de primos
    return primes
    
        
def main():
    primes = []
    for i in range(2, 10000):
        # Para achar os primos entre 1 e 10000 temos que começar em 2, já que
        # 1 não é primo
        # Utilizando a recursividade para popular o array de primos
        primes = isPrime(primes, i)
        
    print(primes)
    
if __name__ == "__main__":
    main()

