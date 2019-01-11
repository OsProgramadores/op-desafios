""" Desafio 03 - Os Programadores - Imprimir números palindromicos """

import sys

class EncontrarPalindromicos():

    def __init__(self, numero_inicial, numero_final):
        self.numero_inicial = int(numero_inicial)
        self.numero_final = int(numero_final)

    def executar(self):
        for numero in range(self.numero_inicial, self.numero_final) :
            if str(numero) == ''.join(reversed(str(numero))) :
                print(numero)


""" Exemplo de como executar: python3 main.py 10 20 """
if __name__ == "__main__" and len(sys.argv) > 1:
    palindromicos = EncontrarPalindromicos(sys.argv[1], sys.argv[2])
    palindromicos.executar()