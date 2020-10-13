"""
Autor: Elismar Silva Pereira
Data: 06/10/2020

Desafio 2: listando números primos.

Escreva um programa para listar todos os números primos entre 1 e 10000.
"""

RANGE = 10000

def main():

  def numero_primo(numero: int):
    numDivisoes = 0
    for divisor in range(2, numero):
      if(numero % divisor == 0):
        return False
    return True


  for numero in range(2, RANGE+1):
    primo = numero_primo(numero)
    if(primo):
      print("{} é primo.".format(numero), end="\n")

if(__name__ == "__main__"):
  main()
