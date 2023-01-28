"""
Solução Desafio-08
Author: Guilherme Silva Schultz
Data: 28-01-2023

le um arquivo de texto contedo uma lista de frações
e aplica regras matematicas para simplificar
"""

import sys
from math import gcd


if len(sys.argv) < 2:
    print("chame este programa passando um arquivo de fraçoes")
    print("Ex python main.py frac.txt")
    sys.exit(1)

try:
    with open(sys.argv[1],"r", encoding="utf-8") as file:
        for line in file.readlines():
            parse = line.strip().split("/")
            if len(parse) == 1: # caso não tenha uma fração, apenas imprime o valor
                print(parse[0])
            else:
                try:
                    dividendo = int(parse[0])
                    divisor = int(parse[1])
                except ValueError as erro:
                    print(erro)
                    continue
                if divisor == 0:
                    print("ERR") # caso divisão por 0 escreve ERR
                    continue
                resto = dividendo % divisor
                int_num = dividendo // divisor
                if resto == 0:
                    print(f"{int_num}")
                    continue

                # calcula  o maior divisor comum e escreve a fração simplificada
                commum = gcd(resto, divisor)
                divisor = divisor/commum
                resto = resto/commum
                num_str = f"{int_num} " if int_num != 0 else ''
                print(f"{num_str}{int(resto)}/{int(divisor)}")
except FileNotFoundError:
    print(f"Arquivo {sys.argv[1]} não encontrado")
    sys.exit(1)
