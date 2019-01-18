"""
Adriano Roberto de Lima
Desafio 5
"""

import json
import pandas as pd

def main():
    """
    Main function
    """

    # Lê o dataset
    dados = json.loads(open('funcionarios.json').read())

    # Separando o dataset em areas e funcionarios. Dois dataframes distintos
    df_areas = pd.DataFrame.from_dict(dados['areas'], orient='columns')
    df_funcionarios = pd.DataFrame.from_dict(dados['funcionarios'], orient='columns')

    # Criando uma coluna com o nome completo
    df_funcionarios['nome_completo'] = \
    df_funcionarios.apply(lambda row: row.nome + ' ' + row.sobrenome, axis=1)

    # Definindo o ID como indice do dataframe
    df_funcionarios = df_funcionarios.set_index('id')

    # Mudando de código da área para nome da área no dataframe
    df_funcionarios['area'] = df_funcionarios['area'].map(df_areas.set_index('codigo')['nome'])

    # Agora vamos descobrir os funcionarios com maiores e menores salários
    global_max = df_funcionarios.loc[df_funcionarios['salario'] == df_funcionarios['salario'].max()]
    global_min = df_funcionarios.loc[df_funcionarios['salario'] == df_funcionarios['salario'].min()]

    # Agora vamos calcular a média da coluna salário para todo o dataframe
    global_avg = df_funcionarios['salario'].mean()

    #Agora vamos agrupar por área e identificar os maiores salários de cada área
    idx_max = \
    df_funcionarios.groupby(['area'])['salario'].transform(max) == df_funcionarios['salario']

    area_max = df_funcionarios[idx_max]

    #Agora vamos agrupar por área e identificar os menores salários de cada área
    idx_min = \
    df_funcionarios.groupby(['area'])['salario'].transform(min) == df_funcionarios['salario']

    area_min = df_funcionarios[idx_min]

    # Calculando o salário médio por área
    area_avg = df_funcionarios.groupby(['area'])['salario'].mean().reset_index(name='avg')

    # Agora vamos agrupar por área e contar o numero de
    # funcionários por área. Em seguida encontramos
    # as areas com maior e menor numero de empregados
    temp_areas = df_funcionarios.groupby(['area']).size().reset_index(name='counts')
    most_employees = temp_areas.loc[temp_areas['counts'] == temp_areas['counts'].max()]
    least_employees = temp_areas.loc[temp_areas['counts'] == temp_areas['counts'].min()]

    # Vamos criar um dataframe removendo todas as linhas que não tenham sobrenomes duplicados
    df_sobrenome = df_funcionarios[df_funcionarios.duplicated('sobrenome', keep=False)]

    # Agora encontramos os maiores salários por sobrenome
    idx_max2 = \
    df_sobrenome.groupby(['sobrenome'])['salario'].transform(max) == df_sobrenome['salario']

    last_name_max = df_sobrenome[idx_max2]

    # Hora de mostrar todos os resultados

    for _, row in global_max.iterrows():
        print("global_max", row['nome_completo'], "{0:.2f}".format(row['salario']), sep="|")

    for _, row in global_min.iterrows():
        print("global_min", row['nome_completo'], "{0:.2f}".format(row['salario']), sep="|")

    print("global_avg", "{0:.2f}".format(global_avg), sep="|")

    for _, row in area_max.iterrows():
        print("area_max", row['area'], row['nome_completo'], \
        "{0:.2f}".format(row['salario']), sep="|")

    for _, row in area_min.iterrows():
        print("area_min", row['area'], row['nome_completo'], \
        "{0:.2f}".format(row['salario']), sep="|")

    for _, row in area_avg.iterrows():
        print("area_avg", row['area'], "{0:.2f}".format(row['avg']), sep="|")

    for _, row in most_employees.iterrows():
        print("most_employees", row['area'], "{0:.0f}".format(row['counts']), sep="|")

    for _, row in least_employees.iterrows():
        print("least_employees", row['area'], "{0:.0f}".format(row['counts']), sep="|")

    for _, row in last_name_max.iterrows():
        print("last_name_max", row['sobrenome'], row['nome_completo'], \
        "{0:.2f}".format(row['salario']), sep="|")

if __name__ == "__main__":
    main()
