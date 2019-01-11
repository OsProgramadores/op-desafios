""" Desafio 03 - Os Programadores - Imprimir números palindromicos """

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

    def _reverse(self, string):
        """
        Método responsável por retornar a string reversa de uma string
        Args:
            string (str): String a ser revertida
        Returns:
            String revertida
        """
        rString = ''
        for i in string:
            rString = i + rString
        
        return rString

    def executar(self):
        """
        Método responsável por verificar se o número, entre os dois números informados, é um palindromo e imprimir caso seja
        """
        for numero in range(self.numero_inicial, self.numero_final):
            rString = self._reverse(str(numero))
            if str(numero) == rString:
                print(numero)


""" 
Exemplo de como executar: python3 main.py 10 20 
"""
if __name__ == "__main__" and len(sys.argv) > 1:
    palindromicos = EncontrarPalindromicos(sys.argv[1], sys.argv[2])
    palindromicos.executar()
