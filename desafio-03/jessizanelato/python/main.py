"""
Desafio 03 - Os Programadores - Imprimir números palindromicos
"""

import sys

class EncontrarPalindromicos():
    """
    Classe para Encontrar todos os possívels números Palindromicos entre dois números
    """

    def __init__(self, numero_inicial, numero_final):
        """
        Construtor da classe
        Args:
            numero_inicial (str): Início do range
            numero_final (str): Fim do range
        """
        self.numero_inicial = int(numero_inicial)
        self.numero_final = int(numero_final)

    @staticmethod
    def reverse(string):
        """
        Método responsável por retornar a string reversa de uma string
        Args:
            string (str): String a ser revertida
        Returns:
            String revertida
        """
        r_string = ''
        for i in string:
            r_string = i + r_string
        return r_string

    def executar(self):
        """
        Método responsável por verificar se o número, entre os dois números informados,
        é um palindromo e imprimir caso seja
        """
        for numero in range(self.numero_inicial, self.numero_final):
            if str(numero) == EncontrarPalindromicos.reverse(str(numero)):
                print(numero)

if __name__ == "__main__" and len(sys.argv) > 1:
    EncontrarPalindromicos(sys.argv[1], sys.argv[2]).executar()
