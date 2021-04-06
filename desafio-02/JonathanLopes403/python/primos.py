#!/usr/bin/python3
""" Solução do desafio 02 - osprogramadores.com."""

def num_primos(inicio, fim):
    """ Mostra todos os números primos entre "Inicio" e "Fim" """
    npmqd = [2, 3, 5, 7]    # npmqd = Números primos menor que dez
    multiplos = set()
    primos = set()
    # Adiciona todos os números multiplos de 2, 3, 5 e 7 no conjunto "multiplos"
    for numero in npmqd:
        for i in range(inicio, fim):
            #print(f"{npmqd[numero]} x {i} = {npmqd[numero] * i}")
            calculo = numero * i
            if calculo not in npmqd:
                if calculo < fim:
                    multiplos.add(calculo)
    # Adiciona os números que estão em "npmqd" e que não estão em "multiplos"
    for i in range(inicio, fim):
        if i < 10 and i in npmqd:
            primos.add(i)
        elif i >= 10 and i not in multiplos:
            primos.add(i)
    return primos

num_primos = num_primos(0, 10000)
# Colocando em Ordem Crescente
primos_ord = list(num_primos)
primos_ord.sort()
print(primos_ord)
