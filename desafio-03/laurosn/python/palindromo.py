#!/usr/bin/python
import time


def palindromo(palavra):
    impar = 0
    tamanho = len(palavra)
    if not (tamanho % 2 == 0):
        impar = 1
    primeiraparte, segundaparte = palavra[:(tamanho // 2) + impar], palavra[tamanho // 2:][::-1]
    return primeiraparte == segundaparte


def checa_palindromos(min, max):
    for i in range(min, max + 1):
        if palindromo(str(i)):
            print(str(i))


def main():
    start_time = time.time()
    checa_palindromos(1, 101)
    print("Tempo de execucao  --- %s segundos ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
