""" Desafio 5 em Python """


import json


def nome_completo(func):
    """ Recebe nome e sobrenome e retorna nome completo """
    nome_sobrenome = func['nome'] + " " + func['sobrenome']
    return nome_sobrenome


def nome_area(func, area):
    """ Recebe funcionario e area e retorna nome completo da area """
    for a in area:
        if func['area'] == a['codigo']:
            return a['nome']


def analise_salarios(funcionarios):
    """ Imprime funcionários com maior, menor salário e média """
    maior = max([func['salario'] for func in funcionarios])
    menor = min([func['salario'] for func in funcionarios])
    media = sum([func['salario'] for func in funcionarios]) / len(funcionarios)

    nomes_maior = []
    nomes_menor = []

    for func in funcionarios:
        if func['salario'] == maior:
            nomes_maior.append(nome_completo(func))
        elif func['salario'] == menor:
            nomes_menor.append(nome_completo(func))

    for n in nomes_maior:
        print(f'global_max|{n}|{maior:.2f}')

    for n in nomes_menor:
        print(f'global_min|{n}|{menor:.2f}')

    print(f'global_avg|{media:.2f}')


def analise_salarios_por_area(funcionarios, areas):
    """ Imprime informações de cada área """

    maior = 0
    menor = 0

    for func in funcionarios:
        if func['salario'] > maior:
            maior = func['salario']

        if func['salario'] < maior:
            menor = func['salario']

    nomes_maior = []
    nomes_menor = []

    for func in funcionarios:
        if func['salario'] == maior:
            nomes_maior.append((nome_area(func, areas), nome_completo(func)))
        if func['salario'] == menor:
            nomes_menor.append((nome_area(func, areas), nome_completo(func)))

    for n in nomes_maior:
        print(f'area_max|{n[0]}|{n[1]}|{maior:.2f}')

    for n in nomes_menor:
        print(f'area_min|{n[0]}|{n[1]}|{menor:.2f}')


def analise_area(funcionarios, areas):
    """ Compara as códigos de area dos funcionários com o nome de area """
    lista_cod = [a['codigo'] for a in areas]

    salarios_areas = {}

    for area in lista_cod:
        if area not in salarios_areas:
            salarios_areas[area] = []

    for func in funcionarios:
        for area in salarios_areas:
            if func['area'] == area:
                salarios_areas[area].append(func)

    for area in salarios_areas:
        analise_salarios_por_area(salarios_areas[area], areas)


def contagem_funcionarios(funcionarios, areas):
    """ Realiza a contagem de funcionarios por area """

    funcionarios_por_area = {}

    for func in funcionarios:
        func_area = nome_area(func, areas)
        if func_area not in funcionarios_por_area:
            funcionarios_por_area[func_area] = 0

    for func in funcionarios:
        for area in funcionarios_por_area:
            if nome_area(func, areas) == area:
                funcionarios_por_area[area] += 1

    dados = zip(funcionarios_por_area.items())
    max_min = list(dados)
    contagem = []

    for elem in max_min:
        contagem.append(elem[0][1])

    cont_max = max(contagem)
    cont_min = min(contagem)

    for elem in max_min:
        if elem[0][1] == cont_min:
            print(f'least_employes|{elem[0][0]}|{cont_min}')

        if elem[0][1] == cont_max:
            print(f'most_employes|{elem[0][0]}|{cont_max}')


def mesmo_sobrenome(funcionarios):
    """Exibe maiores salários para funcionarios com mesmo sobrenome"""

    sobrenomes = {}

    for func in funcionarios:
        if func['sobrenome'] not in sobrenomes:
            sobrenomes[func['sobrenome']] = [func]
        else:
            sobrenomes[func['sobrenome']].append(func)

    for nomes in sobrenomes:
        maior = 0
        if len(sobrenomes[nomes]) > 1:
            for func in sobrenomes[nomes]:
                if func['salario'] > maior:
                    maior = func['salario']

        for func in sobrenomes[nomes]:
            if func['salario'] == maior:
                print(f'last_name_max|{func["sobrenome"]}|\
{nome_completo(func)}|{maior:.2f}')


with open('funcionarios.json', 'r', encoding="utf-8") as json_file:
    info = json.load(json_file)

    json_func = info['funcionarios']
    json_area = info['areas']

    analise_salarios(json_func)
    analise_area(json_func, json_area)
    contagem_funcionarios(json_func, json_area)
    mesmo_sobrenome(json_func)
