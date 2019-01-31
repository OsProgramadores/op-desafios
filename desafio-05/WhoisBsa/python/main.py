
""" Funcionarios JSON """

# -*- coding: utf-8 -*-

import json
import sys
import pandas


def main(file_name):
    """ main """
    with open(file_name, 'r', encoding="utf-8") as r:
        dados = json.loads(r.read())

    #declaração de váriaveis
    salarioMin = 100000000
    global_max = {0: 0, 1: []}
    global_min = {0: salarioMin, 1: []}
    global_avg = {0: 0, 1: 0}
    area_max = {}
    area_min = {}
    areas = {area['codigo']: [area['nome'], salarioMin, 0, 0, 0] for area in dados['areas']}
    most_employees = {0: 0, 1: []}
    least_employees = {0: salarioMin, 1: []}
    last_name_max = {}

    #solução feita pelo integrante arlima
    df_funcionarios = pandas.DataFrame.from_dict(dados['funcionarios'], orient='columns')
    df_funcionarios['nome_completo'] = \
    df_funcionarios.apply(lambda row: row.nome + ' ' + row.sobrenome, axis=1)
    #fim da solução feita por arlima

    for funcionario in dados['funcionarios']:
        nome = funcionario['nome']
        sobrenome = funcionario['sobrenome']
        salario = funcionario['salario']
        area = funcionario['area']

#Quem mais recebe e quem menos recebe na empresa
#e a média salarial da empresa.
    #funcionario com maior salário
        if salario > global_max[0]:
            global_max[0] = salario
            global_max[1] = [[nome, sobrenome, salario]]
        elif salario == global_max[0]:
            global_max[1] += [[nome, sobrenome, salario]]

    #funcionario com menor salário
        if salario < global_min[0]:
            global_min[0] = salario
            global_min[1] = [[nome, sobrenome, salario]]
        elif salario == global_min[0]:
            global_min[1] += [[nome, sobrenome, salario]]

    #media do salario dos funcionarios
        global_avg[0] += salario
        global_avg[1] += 1

#Quem mais recebe e quem menos recebe em cada
#área e a média salarial em cada
    #funcionario com maior salário na area
        if salario > areas[area][2]:
            areas[area][2] = salario
            area_max[areas[area][0]] = [[nome, sobrenome, salario]]
        elif salario == areas[area][2]:
            area_max[areas[area][0]] += [[nome, sobrenome, salario]]

    #funcionario com menor salário na area
        if salario < areas[area][1]:
            areas[area][1] = salario
            area_min[areas[area][0]] = [[nome, sobrenome, salario]]
        elif salario == areas[area][1]:
            area_min[areas[area][0]] += [[nome, sobrenome, salario]]

    #media de funcionarios de cada area
        areas[area][3] += salario
        areas[area][4] += 1

#Maiores salários para funcionários com o mesmo sobrenome
        df_sobrenome = df_funcionarios[df_funcionarios.duplicated('sobrenome', keep=False)]
        idx_max2 = \
        df_sobrenome.groupby(['sobrenome'])['salario'].transform(max) == df_sobrenome['salario']
        last_name_max = df_sobrenome[idx_max2]

#Área(s) com o maior e menor número de funcionários
#maior número de funcionários
    for area in areas.values():
        if area[4] > most_employees[0]:
            most_employees[0] = area[4]
            most_employees[1] = [[area[0], area[4]]]
        elif area[4] == most_employees[0]:
            most_employees[1] += [[area[0], area[4]]]

#menor número de funcionários
        if area[4] != 0 and area[4] < least_employees[0]:
            least_employees[0] = area[4]
            least_employees[1] = [[area[0], area[4]]]
        elif area[4] == least_employees[0]:
            least_employees[1] += [[area[0], area[4]]]


#Respondendo as questões
#questao 1 respondida
    #maximo
    for f in global_max[1]:
        print(f'global_max|{f[0]} {f[1]}|{f[2]:.2f}')
    #minimo
    for f in global_min[1]:
        print(f'global_min|{f[0]} {f[1]}|{f[2]:.2f}')
    #media
    print(f'global_avg|{global_avg[0] / global_avg[1]:.2f}')

#questao 2 respondida
    #maximo
    for kmax in area_max:
        for fAreaMax in area_max[kmax]:
            print(f'area_max|{kmax}|{fAreaMax[0]} {fAreaMax[1]}|{fAreaMax[2]:.2f}')
    #minimo
    for kmin in area_min:
        for fAreaMin in area_min[kmin]:
            print(f'area_min|{kmin}|{fAreaMin[0]} {fAreaMin[1]}|{fAreaMin[2]:.2f}')
    #media
    for area in areas.values():
        if area[4] > 0:
            print(f'area_avg|{area[0]}|{area[3] / area[4]:.2f}')

#questao 3 respondida
    #maior n func
    for nEmployees in most_employees[1]:
        print(f'most_employees|{nEmployees[0]}|{nEmployees[1]}')
    #menor n func
    for nEmployees in least_employees[1]:
        print(f'least_employees|{nEmployees[0]}|{nEmployees[1]}')

#questao 4 respondida
    for _, row in last_name_max.iterrows():
        print("last_name_max", row['sobrenome'], row['nome_completo'], \
        "{0:.2f}".format(row['salario']), sep="|")

if __name__ == "__main__":
    main(sys.argv[1])
