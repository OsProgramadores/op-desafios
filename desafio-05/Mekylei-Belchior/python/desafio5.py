#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Desafio 05
"""

""" Importa os pacotes """
from json import load
import sys

import pandas as pd


def geral(dados):
    """
    Quem mais recebe e quem menos recebe na empresa e a média salarial da empresa. 
    """
    pass


def area():
    """
    Quem mais recebe e quem menos recebe em cada área e a média salarial em cada área.
    """
    pass


def funcionario_area():
    """
    Área(s) com o maior e menor número de funcionários.
    """
    pass


def funcionario_sobrenome():
    """
    Maiores salários para funcionários com o mesmo sobrenome.
    """
    pass


def empregados(arquivo):
    """ Carrega a base de dados. """

    pass


def main(json):
    """ Função principal. """

    pass   


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        raise TypeError('Informe os dois argumentos: arquivo (.py) e o arquivo (.json)')
        sys.exit()
