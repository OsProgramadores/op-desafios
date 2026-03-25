'''Descrição: Solução do desafio-05 - osprogramadores.com
Autor(a): karinnecristina
Linguagem: Python'''

import sys
import json
import pandas as pd
from pandas.io.json import json_normalize

def main(filename):
    '''Faz a leitura do arquivo JSON e une em uma tabela'''

    with open(filename) as file:
        data = json.load(file.read())


    funcionario = json_normalize(data['funcionarios'])
    area = json_normalize(data['areas'])
    dados = pd.merge(funcionario, area, left_on="area", right_on="codigo")

    # 1. Quem mais recebe e quem menos recebe na empresa e a média salarial da empresa.
    maximum_value = dados.loc[dados['salario'].idxmax()]
    value = dados[dados['salario'] == maximum_value['salario']]
    for i in value.values:
        print('global_max|' + i[2] + ' ' + i[4] + '|' + '{:.2f}'.format(float(i[3])))

    maximum_value = dados.loc[dados['salario'].idxmin()]
    value = dados[dados['salario'] == maximum_value['salario']]
    for i in value.values:
        print('global_min|' + i[2] + ' ' + i[4] + '|' + '{:.2f}'.format(float(i[3])))

    value = dados['salario'].mean()
    print("global_avg|" + '{:.2f}'.format(float(value)))

    # 2. Quem mais recebe e quem menos recebe em cada área e a média salarial em cada área.

    areas = dados['maximo_salario'] = dados.groupby(["area"])[["salario"]].transform('max')
    areas = dados[(dados['salario'] == dados['maximo_salario'])]
    for i in areas.values:
        print('area_max|' + i[6] + '|' + i[2] + ' ' + i[4]+ '|' + '{:.2f}'.format(float(i[3])))

    areas = dados['minimo_salario'] = dados.groupby(["area"])[["salario"]].transform('min')
    areas = dados[(dados['salario'] == dados['minimo_salario'])]
    for i in areas.values:
        print('area_min|' + i[6] + '|' + i[2] + ' ' + i[4]+ '|' + '{:.2f}'.format(float(i[3])))

    value = dados['salario'].groupby(dados['area']).mean()
    for i, item in enumerate(value):
        print('area_avg|' + area.loc[area['codigo'] == value.index.values[i]].values[0][1]
              + "|" + '{:.2f}'.format(item))

    # 3. Área(s) com o maior e menor número de funcionários.
    maximum_area = dados['nome_y'].value_counts()
    maximum_area = dict(maximum_area)
    maximum = max(maximum_area, key=lambda x: maximum_area[x])
    value = maximum_area[maximum]
    print('most_employees|'  + maximum, '|' + str(value))

    maximum_area = dados['nome_y'].value_counts()
    maximum_area = dict(maximum_area)
    minimum = min(maximum_area, key=lambda x: maximum_area[x])
    value = maximum_area[minimum]
    print('least_employees|'  + minimum, '|' + str(value))

    # 4. Maiores salários para funcionários com o mesmo sobrenome
    salary = dados.groupby('sobrenome').filter(lambda group: len(group) > 1).copy()
    salary['funcionario'] = salary.groupby(["sobrenome"])[["salario"]]. \
        transform('max')
    salary = salary[(salary['salario'] == \
                                       salary['funcionario'])]
    for item in salary.values:
        print('last_name_max|' + item[4] + '|' + item[2] + ' ' + item[4]+ '|' + '{:.2f}'. \
              format(float(item[7])))

if __name__ == '__main__':
    main(sys.argv[1])
