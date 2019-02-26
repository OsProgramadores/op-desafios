'''Descrição: Solução do desafio-05 - osprogramadores.com
Autor(a): karinnecristina
Linguagem: Python'''

import json
import pandas as pd
from pandas.io.json import json_normalize
with open('funcionarios.json') as file:
    DATA = json.load(file)

FUNCIONARIO = json_normalize(DATA['funcionarios'])
AREA = json_normalize(DATA['areas'])
DADOS = pd.merge(FUNCIONARIO, AREA, left_on="area", right_on="codigo")

# 1. Quem mais recebe e quem menos recebe na empresa e a média salarial da empresa.
MAXIMUMVALUE = DADOS.loc[DADOS['salario'].idxmax()]
HIGHERWAGES = DADOS[DADOS['salario'] == MAXIMUMVALUE['salario']]
for i in HIGHERWAGES.values:
    print('global_max|' + i[2] + ' ' + i[4] + '|' + '{:.2f}'.format(float(i[3])))

MINIMUMVALUE = DADOS.loc[DADOS['salario'].idxmin()]
LOWERWAGES = DADOS[DADOS['salario'] == MINIMUMVALUE['salario']]
for i in LOWERWAGES.values:
    print('global_min|' + i[2] + ' ' + i[4] + '|' + '{:.2f}'.format(float(i[3])))

AVERAGEWAGES = DADOS['salario'].mean()
print("global_avg|" + '{:.2f}'.format(float(AVERAGEWAGES)))

# 2. Quem mais recebe e quem menos recebe em cada área e a média salarial em cada área.

ARE = DADOS['maximo_salario'] = DADOS.groupby(["area"])[["salario"]].transform('max')
ARE = DADOS[(DADOS['salario'] == DADOS['maximo_salario'])]
for i in ARE.values:
    print('area_max|' + i[6] + '|' + i[2] + ' ' + i[4]+ '|' + '{:.2f}'.format(float(i[3])))

ARE = DADOS['minimo_salario'] = DADOS.groupby(["area"])[["salario"]].transform('min')
ARE = DADOS[(DADOS['salario'] == DADOS['minimo_salario'])]
for i in ARE.values:
    print('area_min|' + i[6] + '|' + i[2] + ' ' + i[4]+ '|' + '{:.2f}'.format(float(i[3])))

AVERAGE = DADOS['salario'].groupby(DADOS['area']).mean()
for i, item in enumerate(AVERAGE):
    print('area_avg|' + AREA.loc[AREA['codigo'] == AVERAGE.index.values[i]].values[0][1]
          + "|" + '{:.2f}'.format(item))

# 3. Área(s) com o maior e menor número de funcionários.
MAXIMUMAREA = DADOS['nome_y'].value_counts()
DATAARE = dict(MAXIMUMAREA)
MAXIMUM = max(DATAARE, key=lambda x: DATAARE[x])
VALUE = DATAARE[MAXIMUM]
print('most_employees|'  + MAXIMUM, '|' + str(VALUE))

MAXIMUMAREA = DADOS['nome_y'].value_counts()
DATAARE = dict(MAXIMUMAREA)
MINIMUM = min(DATAARE, key=lambda x: DATAARE[x])
VALUE = DATAARE[MINIMUM]
print('least_employees|'  + MINIMUM, '|' + str(VALUE))

# 4. Maiores salários para funcionários com o mesmo sobrenome
SALARYLASTNAME = DADOS.groupby('sobrenome').filter(lambda group: len(group) > 1).copy()
SALARYLASTNAME['funcionario'] = SALARYLASTNAME.groupby(["sobrenome"])[["salario"]]. \
    transform('max')
SALARYLASTNAME = SALARYLASTNAME[(SALARYLASTNAME["salario"] == SALARYLASTNAME["funcionario"])]
for item in SALARYLASTNAME.values:
    print("last_name_max|" + item[4] + "|" + item[2] + " " + item[4]+ "|" + '{:.2f}'. \
          format(float(item[7])))
