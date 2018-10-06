import json
import sys

FILE_NAME = sys.argv[1]
print(FILE_NAME)


def processar(file_name):
    with open(file_name, 'r', encoding="utf8") as file:
        dados = json.loads(file.read())

    menor = 99999999999

    # questão 1
    global_max = {0: 0, 1: []}
    global_min = {0: menor, 1: []}
    global_avg = {0: 0, 1: 0}

    # questão 2
    area_max = []
    area_min = []

    # questão 3
    least_employees = {0: menor, 1: []}
    most_employees = {0: 0, 1: []}

    # questão 4
    last_name_max = {}
    last_name = {}

    areas = {area['codigo']: [area['nome'], 9999999, 0, 0, 0] for area in dados['areas']}

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
            area_min = [[areas[codigo_area][0], nome, sobrenome, salario]]

        elif salario == areas[codigo_area][1]:
            area_min += [[areas[codigo_area][0], nome, sobrenome, salario]]

        # Maiores salários - áreas
        if salario > areas[codigo_area][2]:
            areas[codigo_area][2] = salario
            area_max = [[areas[codigo_area][0], nome, sobrenome, salario]]

        elif salario == areas[codigo_area][2]:
            area_max += [[areas[codigo_area][0], nome, sobrenome, salario]]

        # Cada area vai receber seus respectivos salários
        areas[codigo_area][3] += salario

        # Incremento da quantidade de salários de cada área.
        areas[codigo_area][4] += 1

        # Maiores salários para funcionários com o mesmo sobrenome
        if sobrenome in last_name_max:
            if salario > last_name_max[sobrenome][1]:
                qt_sn = last_name_max[sobrenome][1]
                last_name_max[sobrenome] = [salario, qt_sn + 1]
                last_name[sobrenome] = [[nome, salario]]

            elif salario == last_name_max[sobrenome][1]:
                qt_sn = last_name_max[sobrenome][1]
                last_name_max[sobrenome] = [salario, qt_sn + 1]
                last_name[sobrenome] += [[nome, salario]]

        else:
            last_name_max[sobrenome] = [salario, 1]

    # Número de funcionários
    for area in areas.values():

        # Menor número
        if area[4] < least_employees[0]:
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

    # Questao 1
    for func in global_max[1]:
        saida += '\nglobal_max|{} {}|{:.2f}'.format(*func)

    for func in global_min[1]:
        saida += '\nglobal_min|{} {}|{:.2f}'.format(*func)

    saida += f'\nglobal_avg|{global_avg[0] / global_avg[1]:.2f}'

    # Questao 2

    for area_m in area_max:
        saida += '\narea_max|{}|{} {}|{:.2f}'.format(*area_m)

    for area_m in area_min:
        saida += '\narea_min|{}|{} {}|{:.2f}'.format(*area_m)

    for area in areas.values():
        if area[4] > 1:
            saida += f'\narea_avg|{area[0]}|{area[3] / area[4]:.2f}'

    # Questao 3

    for most in most_employees[1]:
        saida += '\nmost_employees|{}|{}'.format(*most)

    for least in least_employees[1]:
        saida += '\nleast_employees|{}|{}'.format(*least)

    # Questao 4

    for valor, key in zip(last_name_max.values(), last_name_max.keys()):
        if valor[1] > 1:
            for name in last_name[key]:
                saida += f'\nlast_name_max|{key}|{name[0]} {key}|{name[1]}'

    print(saida)


processar(FILE_NAME)
