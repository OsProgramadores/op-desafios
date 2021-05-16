#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Desafio 5 - Os Programadores
# Solução preliminar proposta por Marcelo A F Gomes

from os.path import getsize
import pandas as pd
import numpy as np
import sys

#input_filename = input('Arquivo de entrada:')
#input_filename = 'funcionarios.json'
#input_filename = 'Funcionarios-10K.json'
#input_filename = 'Funcionarios-30M.json'
input_filename = sys.argv[1]

input_size = getsize(input_filename)

with open(input_filename) as file:
  db = eval(file.read(input_size))

func = pd.DataFrame(db['funcionarios'])
del(db['funcionarios'])
areas = pd.DataFrame(db['areas'])
area = dict()
for a in db['areas']:
  area[a['codigo']] = a['nome']
del(db)

#func.head()
#area

# Calcula e mostra os salários mínimo, médio e máximo:
def min_med_max(place=None):
  if place == None:
    sel = func
    prefi = 'global_min|'
    prefe = 'global_avg|'
    prefa = 'global_max|'
  else:
    sel = func[func['area'] == place]
    if sel.shape[0] < 1:
      return
    aname = area[place]
    prefi = f'area_min|{aname}|'
    prefe = f'area_avg|{aname}|'
    prefa = f'area_max|{aname}|'

  min = sel.salario.min()
  med = sel.salario.mean()
  max = sel.salario.max()

  maxs=list(sel[['nome', 'sobrenome']][sel.salario == max].agg(' '.join, axis=1))
  for nome in maxs:
    print(f'{prefa}{nome}|{max:.2f}')

  mins=list(sel[['nome', 'sobrenome']][sel.salario == min].agg(' '.join, axis=1))
  for nome in mins:
    print(f'{prefi}{nome}|{min:.2f}')

  print(f'{prefe}{med:.2f}')

min_med_max()
for a in area.keys():
  min_med_max(a)

# Calcula os números de funcionários por área
areas['nf'] = areas.shape[0] * [0]
for a in area.keys():
  areas.loc[areas.codigo == a,'nf'] = np.sum(func.area == a)

# Imprime as áreas com menor e com maior número de funcionários
max = np.max(areas.nf)
# Evitamos imprimir informação sobre áreas sem funcionário algum:
areas.loc[areas.nf == 0, 'nf'] = max -1
min = np.min(areas.nf)

# Agora efetivamente imprimimos os resultados:
mins=list(areas[areas.nf == min].nome)
for nome in mins:
  print(f'least_employees|{nome}|{min}')

maxs=list(areas[areas.nf == max].nome)
for nome in maxs:
  print(f'most_employees|{nome}|{max}')

# Verifica os salários por sobrenome, mas
# apenas para sobrenomes que ocorram ao menos 2x no banco
nlast = dict()
for sn in func.sobrenome.unique():
  num = np.sum(func.sobrenome == sn)
  if num > 1:
    nlast[sn] = num

# Imprime os salários de quem empatou com o maior salário por sobrenome
for sn in nlast.keys():
  maxs = np.max(func[func.sobrenome == sn].salario)
  for i in func[np.logical_and(func.sobrenome == sn, func.salario == maxs)].index:
    rico = func.loc[i,['nome','sobrenome']]
    print(f'last_name_max|{rico.sobrenome}|{rico.nome} {rico.sobrenome}|{maxs:.2f}')
