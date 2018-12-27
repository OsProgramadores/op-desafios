import json
import pandas as pd
import numpy as np
import sys


def get_funcjson(filename):
    with open(filename) as f:
        return json.load(f)

def get_areas(funcjson):
    return pd.DataFrame(funcjson['areas'])

def get_funcionariosfull(funcjson, areas):
    funcionarios = pd.DataFrame(funcjson['funcionarios'], columns=['id', 'nome', 'sobrenome', 'salario', 'area'])
    funcionarios['salario'] = funcionarios['salario'].astype(float)
    return funcionarios.merge(areas, left_on="area", right_on="codigo")

def questao1(funcionariosfull):
    idxmaxglobal = funcionariosfull[funcionariosfull["salario"] == funcionariosfull["salario"].max()]
    for item in idxmaxglobal.values:
        print("global_max|" + item[2] + " " + item[4] + "|" + '{:.2f}'.format(float(item[3])))

    idxminglobal = funcionariosfull[funcionariosfull["salario"] == funcionariosfull["salario"].min()]
    for item in idxminglobal.values:
        # print(item)
        print("global_min|" + item[2] + " " + item[4] + "|" + '{:.2f}'.format(float(item[3])))

    idxavgglobal = funcionariosfull["salario"].mean()
    print("global_avg|" + '{:.2f}'.format(float(idxavgglobal)))

def questao2(funcionariosfull, areas):
    funcgroupbyarea = funcionariosfull.groupby('area').filter(lambda group: len(group) > 0)
    funcgroupbyarea['salariomax'] = funcgroupbyarea.groupby(["area"])[["salario"]].transform('max')
    funcgroupbyarea = funcgroupbyarea[(funcgroupbyarea["salario"] == funcgroupbyarea["salariomax"])]

    for item in funcgroupbyarea.values:
        print("area_max|" + item[6] + "|" + item[1] + " " + item[2] + "|" + '{:.2f}'.format(float(item[3])))

    funcgroupbyarea['salariomin'] = funcgroupbyarea.groupby(["area"])[["salario"]].transform('min')
    funcgroupbyarea = funcgroupbyarea[(funcgroupbyarea["salario"] == funcgroupbyarea["salariomin"])]
    for item in funcgroupbyarea.values:
        print("area_min|" + item[6] + "|" + item[1] + " " + item[2] + "|" + '{:.2f}'.format(float(item[3])))

    idxavg = funcionariosfull["salario"].groupby(funcionariosfull["area"]).mean()
    for i, item in enumerate(idxavg):
        print("area_avg|" + areas.loc[areas['codigo'] == idxavg.index.values[i]].values[0][1] + "|" + '{:.2f}'.format(item))

def questao3(funcionariosfull, areas):
    funcgroupbyareacount = funcionariosfull.groupby(funcionariosfull["area"]).count()
    arraycount = np.array(funcgroupbyareacount.values)
    valuemaxarea = arraycount.max()
    indicemaxarea = []
    valueminarea = arraycount.min()
    indiceminarea = []
    for i, arr in enumerate(funcgroupbyareacount.values):
        if valuemaxarea in arr:
            indicemaxarea.append(i)
        else:
            if valueminarea in arr:
                indiceminarea.append(i)

    for imax in indicemaxarea:
        print("most_employees|" + areas.loc[areas['codigo'] == funcgroupbyareacount.index.values[imax]].values[0][
            1] + "|" + str(valuemaxarea))
    for imin in indiceminarea:
        print("least_employees|" + areas.loc[areas['codigo'] == funcgroupbyareacount.index.values[imin]].values[0][
            1] + "|" + str(valueminarea))


def questao4(funcionariosfull):
    funcbysobrenome = funcionariosfull.groupby('sobrenome').filter(lambda group: len(group) > 1).copy()
    funcbysobrenome['salariomax'] = funcbysobrenome.groupby(["sobrenome"])[["salario"]].transform('max')
    funcbysobrenome = funcbysobrenome[(funcbysobrenome["salario"] == funcbysobrenome["salariomax"])]
    for item in funcbysobrenome.values:
        print("last_name_max|" + item[2] + "|" + item[1] + " " + item[2] + "|" + '{:.2f}'.format(float(item[3])))

def desafio5(filename):
    funcjson = get_funcjson(filename)
    areas = get_areas(funcjson)
    funcionariosfull = get_funcionariosfull(funcjson, areas)
    questao1(funcionariosfull)
    questao2(funcionariosfull,areas)
    questao3(funcionariosfull,areas)
    questao4(funcionariosfull)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {}  filename.json'.format(sys.argv[0]))
        sys.exit(2)
    desafio5(sys.argv[1])