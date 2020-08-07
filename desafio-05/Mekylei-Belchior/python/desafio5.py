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
    gmax = dados[dados['salario'] == dados['salario'].max()][['nome', 'sobrenome', 'salario']]
    gmin = dados[dados['salario'] == dados['salario'].min()][['nome', 'sobrenome', 'salario']]
    gavg = dados['salario'].mean()

    for linha in gmax.itertuples():
        print(f'global_max|{linha[1]} {linha[2]}|{linha[3]:.2f}')

    for linha in gmin.itertuples():
        print(f'global_min|{linha[1]} {linha[2]}|{linha[3]:.2f}')

    print(f'global_avg|{gavg:.2f}')


def area(dados):
    """
    Quem mais recebe e quem menos recebe em cada área e a média salarial em cada área.
    """
    amax = dados.groupby('area')['salario'].max()
    amin = dados.groupby('area')['salario'].min()
    areamax = dados.query('salario in @amax')
    areamin = dados.query('salario in @amin')
    area_avg = dados.groupby('nome_area')['salario'].mean()

    for linha in areamax.itertuples():
        print(f'area_max|{linha[6]}|{linha[2]} {linha[3]}|{linha[4]:.2f}')

    for linha in areamin.itertuples():
        print(f'area_min|{linha[6]}|{linha[2]} {linha[3]}|{linha[4]:.2f}')
    
    for linha in area_avg.iteritems():
        print(f'area_avg|{linha[0]}|{linha[1]:.2f}')


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

    with open(arquivo, 'r', encoding='utf-8') as arquivo_json:
       dados_json = load(arquivo_json)

    funcionarios = dados_json.pop('funcionarios')
    areas = dados_json.pop('areas')

    base = pd.DataFrame(funcionarios)
    area = pd.DataFrame(areas)
    area.rename(columns={'codigo': 'area'}, inplace=True)
    empregados = pd.merge(base, area, on='area', suffixes=[None, '_area'])

    return empregados


def main(json):
    """ Função principal. """

    emp = empregados(json)
    geral(emp)
    print()
    area(emp)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        raise TypeError('Informe os dois argumentos: arquivo (.py) e o arquivo (.json)')
        sys.exit()
