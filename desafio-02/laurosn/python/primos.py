#!/usr/bin/python
import time
def erastotenes(n):
    # cria uma lista onde ficarao os multiplos do numero primo
    multiples = []
    # iteracao a partir do 2 (primeiro primo) ate o limite definido como parametro
    for i in range(2, n+1):
        # se o numero nao esta na lista de multiplos do numero primo, ele e primo
        if i not in multiples:
            # imprime os numeros primos
            print (i)
            # adiciona os multiplos na lista de "nao" primos
            for j in range(i*i, n+1, i):
                multiples.append(j)
def main():
  start_time = time.time()
  erastotenes(10000)
  print(" Tempo de execucao --- %s segundos ---" % (time.time() - start_time))
if __name__ == "__main__":
  main()

