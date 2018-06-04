#!/usr/bin/env python3

def is_prime(x):
  # cria uma lista somente com o número 2
  prime_list = [2]
  # cria uma lista vazia
  total_list = []  
  # este "for loop" adiciona todos os números ímpares nas duas listas
  for n in range(2, x):
    if n % 2 != 0:
      total_list.append(n)
      prime_list.append(n)
  """ este "for loop" é o coração do programa: ele divide todos os números de uma lista
      por todos os números da outra (exceto o seu igual - eliminação feita no "if");
      se o número for divisível por qualquer outro, é removido da lista de primos ("prime_list")"""
  for m in total_list:      
    for n in prime_list:
      if n != m:
        if n % m == 0:
          prime_list.remove(n)
  print(prime_list)
        
  
  
is_prime(10000)
