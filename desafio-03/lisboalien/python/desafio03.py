# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:53:20 2019

Desafio 03  - Palíndromos numéricos entre 1 e 999999

@author: Aline
"""

def isPalindrome(n):
    # Função que verifica se um número é um palíndromo
    # Convertendo o número em string
    sn = str(n)
    # Obtendo o reverso desse número para a comparação
    rsn = sn[::-1]
    if (n<10):
        # Se o número é menor que 10, ele é um palíndromo
        return True
    else:
        if(sn[:int(len(sn)/2)] == rsn[:int(len(sn)/2)]):
            # Para que o número seja um palíndromo os números de 0 à len(n)/2
            # têm que ser iguais aos números de 0 à len(n)/2 do seu respectivo
            # reverso
            return True
        else: 
            return False
        

def main():
    # Criando um array que irá conter todos os palíndromos
    pal = []
    for i in range(999999):
        if(isPalindrome(i)):
            # Se o número for palíndromo, adicionar esse número ao array
            pal.append(i)
    
    # Imprimir o array de palíndromos
    print(pal)

if __name__ == "__main__":
    main()