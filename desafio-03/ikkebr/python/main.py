"""Solução do Desafio 03 em Python por @ikkebr"""
inicio = int(input())
fim = int(input())

for num in range(inicio, fim+1):
    s_num = str(num)
    if s_num == s_num[::-1]:
        print(s_num)
