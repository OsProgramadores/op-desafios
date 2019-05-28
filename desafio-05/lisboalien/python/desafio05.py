# -*- coding: utf-8 -*-
"""
Created on Wed May 22 23:48:44 2019.

Desafio 05 - Processando as informações da empresa
Extrair várias informações sobre funcionários.json

@author: Aline
"""


import json
from statistics import mean
import pandas as pd


def global_calc(data_frame):
    """
    Função global_calc.

    Parameters
    ----------
    data_frame : TYPE pandas.DataFrame
        Data Frame contendo as informações de funcionários com as colunas:
        area, id, nome, salario e sobrenome.

    Returns
    -------
    Imprime os seguintes dados:
        Salário Mínimo Global -> Nome Completo + Valor do Salário
        Salário Máximo Global -> Nome Completo + Valor do Salário
        Salário Médio Global -> Valor do Salário Médio

    """
    # Separando os valores do salário máximo, mínimo e médio global
    max_salary = max(data_frame['salario'])
    min_salary = min(data_frame['salario'])
    avg_salary = round(mean(data_frame['salario']), 2)
    global_results = []

    # Separando os valores do DF de acordo com os salários
    for index, row in data_frame.sort_values(by=['salario']).iterrows():
        if row['salario'] == max_salary:
            global_results.append(['global_max', row['nome'] + " "
                                   + row['sobrenome'], row['salario']])
        elif row['salario'] == min_salary:
            global_results.append(['global_min', row['nome'] + " "
                                   + row['sobrenome'], row['salario']])

    # Adicionando o valor do salário médio no array de resultados
    global_results.append(['global_avg', '', avg_salary])
    # Transformando o array de resultados para um Data Frame
    g_results = pd.DataFrame(global_results, columns=['Resultado',
                                                      'Nome Completo',
                                                      'Salario'])

    # Imprimindo os valores do DF de resultados no formato solicitado no
    # desafio
    for index, row in g_results.iterrows():
        if row['Resultado'] == 'global_avg':
            print(row['Resultado'] + '|' + "%.2f" % row['Salario'])
        else:
            print(row['Resultado'] + '|' + row['Nome Completo'] + '|'
                  + "%.2f" % row['Salario'])


def area_salary_calc(data_frame, areas):
    """
    Função area_salary_calc.

    Parameters
    ----------
    data_frame : TYPE pandas.DataFrame
        Data Frame contendo as informações de funcionários com as colunas:
        area, id, nome, salario e sobrenome.
    areas : TYPE pandas.DataFrame
        Data Frame contendo as informações das áreas com as columnas:
            codigo e nome.

    Returns
    -------
    Imprime os seguintes dados:
        Salário Mínimo por Área -> Área + Nome Completo + Valor do Salário
        Salário Máximo por Área -> Área + Nome Completo + Valor do Salário
        Salário Médio por Área -> Área + Valor do Salário Médio

    """
    # Separando os salários máximo, mínimo e médio em dataframes por área
    max_c = data_frame.groupby(['area']).max()
    max_c['result'] = 'area_max'
    min_c = data_frame.groupby(['area']).min()
    min_c['result'] = 'area_min'
    avg_c = data_frame.groupby(['area']).mean()
    avg_c['result'] = 'area_avg'

    # Concatenando os DF em um DF único
    area_results = pd.concat([max_c, min_c, avg_c], sort=False)
    # Criando um DF final com o formato solicitado no desafio
    a_results = pd.DataFrame(columns=['Resultado', 'Area', 'Nome Completo',
                                      'Salario'])

    # Adicionando os valores do DF concatenado ao DF final
    for i in range(len(area_results)):
        if area_results['result'].get(i) == 'area_avg':
            a_results.loc[i] = [area_results['result'].get(i),
                                area_results['result'].index[i], '',
                                area_results['salario'].get(i)]
        else:
            a_results.loc[i] = [area_results['result'].get(i),
                                area_results['result'].index[i],
                                area_results['nome'].get(i) + ' '
                                + area_results['sobrenome'].get(i),
                                area_results['salario'].get(i)]

    # Substituindo os códigos das áreas pelos nomes completos
    for index, row in areas.iterrows():
        a_results['Area'] = a_results['Area'].replace(row['codigo'],
                                                      row['nome'])

    # Imprimindo os valores finais no formato do desafio
    for index, row in a_results.iterrows():
        if row['Resultado'] == 'area_avg':
            print(row['Resultado'] + '|' + row['Area'] + '|'
                  + "%.2f" % row['Salario'])
        else:
            print(row['Resultado'] + '|' + row['Area'] + '|'
                  + row['Nome Completo'] + '|' + "%.2f" % row['Salario'])


def area_func_calc(data_frame, areas):
    """
    Função area_func_calc.

    Parameters
    ----------
    data_frame : TYPE pandas.DataFrame
        Data Frame contendo as informações de funcionários com as colunas:
        area, id, nome, salario e sobrenome.
    areas : TYPE pandas.DataFrame
        Data Frame contendo as informações das áreas com as columnas:
            codigo e nome.

    Returns
    -------
    Imprime os seguintes dados:
        Área com maior número de funcionários -> Área + Número de Funcionários
        Área com menor número de funcionários -> Área + Número de Funcionários

    """
    # Separando o DF com o número de funcionários por área
    area_count = data_frame.groupby(['area']).count()
    # Criando um DF final com o formato solicitado no desafio
    func = pd.DataFrame(columns=['Resultado', 'Area',
                                 'Numero de Funcionarios'])

    # Adicionando os valores do DF area_count no DF final
    for i in range(len(area_count)):
        if area_count['id'].get(i) == max(area_count['id']):
            func.loc[i] = ['most_employees', area_count['id'].index[i],
                           area_count['id'].get(i)]
        elif area_count['id'].get(i) == min(area_count['id']):
            func.loc[i] = ['least_employees', area_count['id'].index[i],
                           area_count['id'].get(i)]

    # Substituindo os códigos das áreas pelos nomes completos
    for index, row in areas.iterrows():
        func['Area'] = func['Area'].replace(row['codigo'], row['nome'])

    # Imprimindo os valores finais no formato do desafio
    for index, row in func.iterrows():
        print(row['Resultado'] + '|' + row['Area'] + '|'
              + str(row['Numero de Funcionarios']))


def salary_same_name_calc(data_frame):
    """
    Função salary_same_name_calc

    Parameters
    ----------
    data_frame : TYPE pandas.DataFrame
        Data Frame contendo as informações de funcionários com as colunas:
        area, id, nome, salario e sobrenome.

    Returns
    -------
    Imprime os seguintes dados:
        Maiores salários por sobrenome -> Sobrenome + Nome Completo +
        Valor do salário.

    """
    # Separando o DF contendo os maiores salários por sobrenome
    last_name_count = data_frame.groupby(['sobrenome']).max()
    # Criando um DF final com o formato solicitado no desafio
    last_name_max = pd.DataFrame(columns=['Resultado', 'Sobrenome',
                                          'Nome Completo', 'Salario'])

    # Adicionando os valores do DF last_name_count no DF final
    for i in range(len(last_name_count)):
        last_name_max.loc[i] = ['last_name_max',
                                last_name_count['salario'].index[i],
                                last_name_count['nome'].get(i) + ' '
                                + last_name_count['salario'].index[i],
                                last_name_count['salario'].get(i)]

    # Imprimindo os valores finais no formato do desafio
    for index, row in last_name_max.iterrows():
        print(row['Resultado'] + '|' + row['Sobrenome'] + '|'
              + row['Nome Completo'] + '|' + "%.2f" % row['Salario'])


def main():
    """Função main para a análise do arquivo funcionarios.json."""
    with open('funcionarios.json', 'r', encoding='utf-8') as file:
        empresa = json.load(file)

    # Separando os dados do arquivo em 2 dataframes
    # areas contém os códigos e nomes das áreas da empresa
    areas = pd.DataFrame(empresa['areas'])
    # funcionarios contém os dados de cada funcionário da empresa
    funcionarios = pd.DataFrame(empresa['funcionarios'])

    # Chamando as funções que fazem as análises do arquivo funcionarios.json
    global_calc(funcionarios)
    area_salary_calc(funcionarios, areas)
    area_func_calc(funcionarios, areas)
    salary_same_name_calc(funcionarios)


if __name__ == "__main__":
    main()
