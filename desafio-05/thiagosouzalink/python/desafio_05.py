"""
Processando as informações da empresa.

Utilize a linguagem de programação de sua preferência (e quaisquer
bibliotecas que sejam necessárias) e escreva um programa que leia o nome
de um arquivo JSON como parâmetro – que seguirá os mesmos moldes do
arquivo funcionarios.json listado acima – e imprima as informações
solicitadas a seguir, baseado no conteúdo do arquivo lido.

"""
import json
import sys


def get_data(data):
    """Processa as informações principais a serem exibidas.

    Args:
        data (dict): Dados do arquivo de informações da empresa.
    """
    salaries = []
    salaries_area = {}
    quantity_per_surname = {}

    for employee in data['funcionarios']:
        salary = employee['salario']
        area = employee['area']
        surname = employee['sobrenome']

        salaries.append(salary)

        # 2. Quem mais recebe e quem menos recebe em cada área e a
        # média salarial em cada área
        if area not in salaries_area:
            # [max_salary, min_salary, sum_salaries, num_employees]
            salaries_area[area] = [salary, salary, 0, 0]
        if salary > salaries_area[area][0]:
            salaries_area[area][0] = salary
        elif salary < salaries_area[area][1]:
            salaries_area[area][1] = salary
        salaries_area[area][2] += salary
        salaries_area[area][3] += 1

        # 4. Maiores salários para funcionários com o mesmo sobrenome
        if surname not in quantity_per_surname:
            # [max_salary, quantity]
            quantity_per_surname[surname] = [salary, 0]
        if salary > quantity_per_surname[surname][0]:
            quantity_per_surname[surname][0] = salary
        quantity_per_surname[surname][1] += 1

    # 1. Quem mais recebe e quem menos recebe na empresa e a média
    # salarial da empresa.
    g_max = max(salaries, default=0)
    g_min = min(salaries, default=0)
    g_avg = sum(salaries) / len(salaries) if salaries else 0

    # 3. Área(s) com o maior e menor número de funcionários
    employees_area = ([area, values[3]]
                       for area, values in salaries_area.items())

    # 1
    print_global_data(data, g_max, g_min, g_avg)
    # 2
    print_salaries_by_area(data, salaries_area)
    # 3
    print_number_employees_area(data, employees_area)
    # 4
    print_max_salaries_surname(data, quantity_per_surname)


def print_global_data(data, global_max, global_min, global_avg):
    """Imprime quem mais recebe e quem menos recebe na empresa e a
    média salarial da empresa.

    Args:
        data (dict): Dados do arquivo de informações da empresa.
        global_max (float): Maior salário global da empresa.
        global_min (float): Menor salário global da empresa.
        global_avg (float): Média salarial global da empresa.
    """
    for employee in data['funcionarios']:
        if employee['salario'] == global_max:
            print(f"global_max|{employee['nome']} {employee['sobrenome']}|"
                  f"{global_max:.2f}")

    for employee in data['funcionarios']:
        if employee['salario'] == global_min:
            print(f"global_min|{employee['nome']} {employee['sobrenome']}|"
                  f"{global_min:.2f}")

    print(f"global_avg|{global_avg:.2f}")


def print_salaries_by_area(data, salaries_area):
    """Imprime quem mais recebe e quem menos recebe em cada área e a
    média salarial em cada área.

    Args:
        data (dict): Dados do arquivo de informações da empresa.
        salaries_area (dict): Informações com maior e menor salario e
        média de cada área da empresa.
    """
    # salaries_area = {'area': [area_max, area_min,
    #                           sum_salaries, num_employees]}
    areas = {area['codigo']: area['nome'] for area in data['areas']}

    for area, values in salaries_area.items():
        for employee in data['funcionarios']:
            if employee['area'] == area:
                if employee['salario'] == values[0]:
                    print(f"area_max|{areas[area]}|"
                          f"{employee['nome']} {employee['sobrenome']}|"
                          f"{values[0]:.2f}")

        for employee in data['funcionarios']:
            if employee['area'] == area:
                if employee['salario'] == values[1]:
                    print(f"area_min|{areas[area]}|"
                          f"{employee['nome']} {employee['sobrenome']}|"
                          f"{values[1]:.2f}")

        avg_area = values[2] / values[3]
        print(f"area_avg|{areas[area]}|{avg_area:.2f}")


def print_number_employees_area(data, employees_area):
    """Imprime área(s) com o maior e menor número de funcionários.

    Args:
        data (dict): [description]
        employees_area (generator): Informações da quantidade de
        funcionários por área da empresa.
    """
    dict_areas = {area['codigo']: area['nome'] for area in data['areas']}
    number_employees_area = dict(employees_area)

    most_employees = max(number_employees_area.values())
    least_employees = min(number_employees_area.values())

    for area, number in number_employees_area.items():
        if number == most_employees:
            print(f"most_employees|{dict_areas[area]}|{number}")

    for area, number in number_employees_area.items():
        if number == least_employees:
            print(f"least_employees|{dict_areas[area]}|{number}")


def print_max_salaries_surname(data, quantity_surname):
    """Imprime maiores salários para funcionários com o mesmo sobrenome.

    Args:
        data (dict): Dados do arquivo de informações da empresa.
        quantity_surname (dict): Informações contendo maior salário e
        quantidade de funcionário de cada área da empresa.
    """
    # quantity_surname = {'surname': [max_salary, quantity]}
    surnames = {surname: values[0]
                for surname, values in quantity_surname.items()
                if values[1] > 1}

    for employee in data['funcionarios']:
        surname = employee['sobrenome']
        salary = employee['salario']
        if surname in surnames and salary == surnames[surname]:
            print(f"last_name_max|{employee['sobrenome']}|"
                  f"{employee['nome']} {employee['sobrenome']}|"
                  f"{employee['salario']:.2f}")


if __name__ == "__main__":
    file_json = sys.argv[1]

    with open(file_json, 'r', encoding='utf-8') as json_file:
        data_json = json.load(json_file)

    get_data(data_json)
