"""Solução para o desafio 05 - RafaelDSS."""

import sys
import time

FILE_NAME = sys.argv[1]


def processar(file_name):
    """Processa arquivo JSON e gera saida em formato padronizado."""
    
    with open(file_name, 'r', encoding="utf8") as file:
        dados = json.loads(file.read())

    menor = 99999999999

    # questão 1
    global_max = {0: 0, 1: []}
    global_min = {0: menor, 1: []}
    global_avg = {0: 0, 1: 0}

    # questão 2
    area_max = {}
    area_min = {}

    # questão 3
    least_employees = {0: menor, 1: []}
    most_employees = {0: 0, 1: []}

    # questão 4
    last_name_max = {}
    last_name = {}

    areas = {area['codigo']: [area['nome'], menor, 0, 0, 0] for area in dados['areas']}

    for funcionario in dados['funcionarios']:
        salario = funcionario['salario']
        nome = funcionario['nome']
        sobrenome = funcionario['sobrenome']
        codigo_area = funcionario['area']

        # Média salarial de todos os fucionários
        global_avg[0] += salario
        global_avg[1] += 1

        # Menores salários
        if salario < global_min[0]:
            global_min[0] = salario
            global_min[1] = [[nome, sobrenome, salario]]

        elif salario == global_min[0]:
            global_min[1] += [[nome, sobrenome, salario]]

        # Maiores salários
        if salario > global_max[0]:
            global_max[0] = salario
            global_max[1] = [[nome, sobrenome, salario]]

        elif salario == global_max[0]:
            global_max[1] += [[nome, sobrenome, salario]]

        # Menores salários - áreas
        if salario < areas[codigo_area][1]:
            areas[codigo_area][1] = salario
            area_min[areas[codigo_area][0]] = [[nome, sobrenome, salario]]

        elif salario == areas[codigo_area][1]:
            area_min[areas[codigo_area][0]] += [[nome, sobrenome, salario]]

        # Maiores salários - áreas
        if salario > areas[codigo_area][2]:
            areas[codigo_area][2] = salario
            area_max[areas[codigo_area][0]] = [[nome, sobrenome, salario]]

        elif salario == areas[codigo_area][2]:
            area_max[areas[codigo_area][0]] += [[nome, sobrenome, salario]]

        # Cada area vai receber seus respectivos salários
        areas[codigo_area][3] += salario

        # Incremento da quantidade de salários de cada área.
        areas[codigo_area][4] += 1

        # Maiores salários para funcionários com o mesmo sobrenome
        if sobrenome in last_name_max:
            if salario > last_name_max[sobrenome]:
                last_name_max[sobrenome] = salario
                last_name[sobrenome] = [[nome, salario]]

            elif salario == last_name_max[sobrenome]:
                last_name_max[sobrenome] = salario
                last_name[sobrenome] += [[nome, salario]]

        else:
            last_name_max[sobrenome] = salario
            last_name[sobrenome] = [[nome, salario]]

    # Número de funcionários
    for area in areas.values():

        # Menor número
        if area[4] < least_employees[0] and area[4] != 0:
            least_employees[0] = area[4]
            least_employees[1] = [[area[0], area[4]]]

        elif area[4] == least_employees[0]:
            least_employees[1] += [[area[0], area[4]]]

        # Maior número
        if area[4] > most_employees[0]:
            most_employees[0] = area[4]
            most_employees[1] = [[area[0], area[4]]]

        elif area[4] == most_employees[0]:
            most_employees[1] += [[area[0], area[4]]]

    saida = ''

    # Questão 1

    saida += f'global_avg|{global_avg[0] / global_avg[1]:.2f}\n'

    for func in global_max[1]:
        saida += 'global_max|{} {}|{:.2f}\n'.format(*func)

    for func in global_min[1]:
        saida += 'global_min|{} {}|{:.2f}\n'.format(*func)

    # Questão 2

    for key in area_max.keys():
        for f in area_max[key]:
            if f[2] > 0:
                saida += f'area_max|{key}|{f[0]} {f[1]}|{f[2]:.2f}\n'

    for key in area_min.keys():
        for f in area_min[key]:
            if f[2] > 0:
                saida += f'area_min|{key}|{f[0]} {f[1]}|{f[2]:.2f}\n'

    for area in areas.values():
        if area[4] > 1:
            saida += f'area_avg|{area[0]}|{area[3] / area[4]:.2f}\n'

    # Questão 3

    for most in most_employees[1]:
        saida += 'most_employees|{}|{}\n'.format(*most)

    for least in least_employees[1]:
        saida += 'least_employees|{}|{}\n'.format(*least)

    # Questão 4

    for valor, key in zip(last_name_max.values(), last_name_max.keys()):
        for name in last_name[key]:
            saida += f'last_name_max|{key}|{name[0]} {key}|{name[1]:.2f}\n'

    print(saida, end='')


processar(FILE_NAME)
