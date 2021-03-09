#!/usr/bin/python3
# Esse progama mostra todos os números primos entre um número e outro

def num_primos(inicio, fim):
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

primos = num_primos(0, 10000)
# Colocando em Ordem Crescente
primos_ord = list(primos)
primos_ord.sort()
print(primos_ord)
