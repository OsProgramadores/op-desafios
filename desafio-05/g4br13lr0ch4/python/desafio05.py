"""Solução do desafio 05 submetido por Gabriel Rocha - G4BR13LR0CH4"""

import json
import sys

FILE_NAME = sys.argv[1]

def question01(funcionarios):
    """
        Lista os funcionarios com os maiores e menores salarios,
        além de exibir o valor medio dos salarios
    """
    global_max = False
    global_min = False
    global_avg = False

    for funcionario in funcionarios:
        if global_min or global_max or global_avg:
            if funcionario['salario'] > global_max:
                global_max = funcionario['salario']

            if funcionario['salario'] < global_min:
                global_min = funcionario['salario']

            global_avg += funcionario['salario']

        else:
            global_min = global_avg = global_max = funcionario['salario']

    for funcionario in funcionarios:
        if funcionario['salario'] == global_max:
            print(f"global_max|{funcionario['nome']} {funcionario['sobrenome']}|" +
                  f"{funcionario['salario']:.2f}")

    for funcionario in funcionarios:
        if funcionario['salario'] == global_min:
            print(f"global_min|{funcionario['nome']} {funcionario['sobrenome']}|" +
                  f"{funcionario['salario']:.2f}")

    print(f"global_avg|{(global_avg/len(funcionarios)):.2f}")

def question02(file):
    """Separa quem mais recebe e quem menos recebe por area"""
    data = {}

    for funcionario in file['funcionarios']:
        if funcionario['area'] not in data:
            data[funcionario['area']] = [
                1,
                funcionario['salario'],
                funcionario['salario'],
                funcionario['salario']
            ]#quantidade de pessoas, salario maximo, salario minimo e medio.

        else:
            data[funcionario['area']][0] += 1 #quantidade de pessoas por area

            if data[funcionario['area']][1] < funcionario['salario']:
                data[funcionario['area']][1] = funcionario['salario'] #Maior salario

            if data[funcionario['area']][2] > funcionario['salario']:
                data[funcionario['area']][2] = funcionario['salario'] #Menor salario

            data[funcionario['area']][3] += funcionario['salario'] #Salario medio

    for area in file['areas']:
        if area['codigo'] not in data:
            data[area['codigo']] = [0, 0, 0, 0]

    for area in file['areas']:
        for funcionario in file['funcionarios']:
            if (
                    (funcionario['area'] == area['codigo']) and
                    (funcionario['salario'] == data[area['codigo']][1])
            ):
                print(f"area_max|{area['nome']}|{funcionario['nome']} {funcionario['sobrenome']}|" +
                      f"{funcionario['salario']:.2f}")

        for funcionario in file['funcionarios']:
            if (
                    (funcionario['area'] == area['codigo']) and
                    (funcionario['salario'] == data[area['codigo']][2])
            ):
                print(f"area_min|{area['nome']}|{funcionario['nome']} " +
                      f"{funcionario['sobrenome']}|{funcionario['salario']:.2f}")

        if data[area['codigo']][0] > 0:
            print(f"area_avg|{area['nome']}|" +
                  f"{((data[area['codigo']][3])/data[area['codigo']][0]):.2f}")

    return data

def question03(areas, data):
    """Informa a area com mais pessoas funcionarios e a com menor"""
    most_employees = 0
    least_employees = 0

    for area in areas:
        if most_employees == 0 and least_employees == 0:
            least_employees = most_employees = data[area['codigo']][0]
            most = {
                "area": area['nome'],
                "quantidade": data[area['codigo']][0]
            }
            least = {
                "area": area['nome'],
                "quantidade": data[area['codigo']][0]
            }

        if most_employees < data[area['codigo']][0]:
            most_employees = data[area['codigo']][0]
            most = {"area": area['nome'], "quantidade": data[area['codigo']][0]}

        if least_employees > data[area['codigo']][0] and data[area['codigo']][0] != 0:
            least_employees = data[area['codigo']][0]
            least = {"area": area['nome'], "quantidade": data[area['codigo']][0]}

    print(f"most_employees|{most['area']}|{most['quantidade']}")
    print(f"least_employees|{least['area']}|{least['quantidade']}")

def question04(funcionarios):
    """Separa quem ganha mais comparando entre os sobrenomes"""
    data = {}

    for funcionario in funcionarios:
        if funcionario['sobrenome'] not in data:
            data[funcionario['sobrenome']] = [1, funcionario['salario']]
        else:
            data[funcionario['sobrenome']][0] += 1
            if data[funcionario['sobrenome']][1] < funcionario['salario']:
                data[funcionario['sobrenome']][1] = funcionario['salario']

    for funcionario in funcionarios:
        if (
                (data[funcionario['sobrenome']][0] > 1) and
                (funcionario['salario'] == data[funcionario['sobrenome']][1])
        ):
            print(f"last_name_max|{funcionario['sobrenome']}|" +
                  f"{funcionario['nome']} {funcionario['sobrenome']}|{funcionario['salario']:.2f}")

def load():
    """Carrega o arquivo e decodifica"""
    with open(FILE_NAME, 'r') as json_file:
        file = json.load(json_file)
        question01(file['funcionarios'])
        question03(file['areas'], question02(file))
        question04(file['funcionarios'])

if __name__ == "__main__":
    load()
