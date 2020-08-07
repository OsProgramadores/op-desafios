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


def funcionario_area(dados):
    """
    Área(s) com o maior e menor número de funcionários.
    """
    quantidade = dados.groupby('nome_area')['area'].count()

    for linha in quantidade.iteritems():
        if linha[1] == quantidade.max():
            print(f'most_employees|{linha[0]}|{linha[1]}')
        if linha[1] == quantidade.min():
            print(f'least_employees|{linha[0]}|{linha[1]}')


def funcionario_sobrenome(dados):
    """
    Maiores salários para funcionários com o mesmo sobrenome.
    """
    duplicados = dados['sobrenome'].value_counts()
    duplicados = [nome[0] for nome in duplicados.iteritems() if nome[1] >= 2]
    duplicados = dados.query('sobrenome in @duplicados')
    maiores = duplicados.groupby('sobrenome')
    maiores = maiores.max()

    for linha in maiores.itertuples():
        print(f'last_name_max|{linha[0]}|{linha[2]} {linha[0]}|{linha[3]:.2f}')


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

    dados = empregados(json)
    geral(dados)
    area(dados)
    funcionario_area(dados)
    funcionario_sobrenome(dados)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        raise TypeError('Informe os dois argumentos: arquivo (.py) e o arquivo (.json)')
        sys.exit()
