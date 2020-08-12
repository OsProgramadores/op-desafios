#-*- coding: utf-8 -*-

""" Importa os pacotes """
from sys import argv
from json import load
from pandas import DataFrame, merge


class Informacoes():
    """ Obtém a relação de informações dos funcionários. """

    def __init__(self, dados):
        self.dados = dados
        self.impressao = ''


    def geral(self):
        """
        Quem mais recebe e quem menos recebe na empresa e a média salarial da empresa.
        """
        salario_info = self.dados['salario'].describe()
        maior = salario_info['max']
        menor = salario_info['min']
        gavg = salario_info['mean'].round(2)

        gmax = self.dados.loc[self.dados['salario'] == maior, ['nome', 'sobrenome', 'salario']]
        gmin = self.dados.loc[self.dados['salario'] == menor, ['nome', 'sobrenome', 'salario']]

        for linha in gmax.itertuples():
            self.impressao = f'global_max|{linha[1]} {linha[2]}|{linha[3]:.2f}\n'

        for linha in gmin.itertuples():
            self.impressao += f'global_min|{linha[1]} {linha[2]}|{linha[3]:.2f}\n'

        self.impressao += f'global_avg|{gavg}\n'


    def area(self):
        """
        Quem mais recebe e quem menos recebe em cada área e a média salarial em cada área.
        """
        amax = self.dados.groupby('area')['salario'].max()
        amin = self.dados.groupby('area')['salario'].min()

        amax = self.dados.query('salario in @amax')
        amin = self.dados.query('salario in @amin')
        area_avg = self.dados.groupby('nome_area')['salario'].mean()

        for linha in amax.itertuples():
            self.impressao += f'area_max|{linha[6]}|{linha[2]} {linha[3]}|{linha[4]:.2f}\n'

        for linha in amin.itertuples():
            self.impressao += f'area_min|{linha[6]}|{linha[2]} {linha[3]}|{linha[4]:.2f}\n'

        for linha in area_avg.iteritems():
            self.impressao += f'area_avg|{linha[0]}|{linha[1]:.2f}\n'


    def funcionario_area(self):
        """
        Área(s) com o maior e menor número de funcionários.
        """
        quantidade = self.dados['nome_area'].value_counts()

        for linha in quantidade.iteritems():
            if linha[1] == quantidade.max():
                self.impressao += f'most_employees|{linha[0]}|{linha[1]}\n'
            if linha[1] == quantidade.min():
                self.impressao += f'least_employees|{linha[0]}|{linha[1]}\n'


    def funcionario_sobrenome(self):
        """
        Maiores salários para funcionários com o mesmo sobrenome.
        """
        duplicados = []

        frequencia_sobrenomes = self.dados['sobrenome'].value_counts()

        if frequencia_sobrenomes.min() < 2:
            for nomes in frequencia_sobrenomes.iteritems():
                if nomes[1] >= 2:
                    duplicados.append(nomes[0])
                else:
                    break
            duplicados = self.dados.query('sobrenome in @duplicados')
            maiores_salarios = duplicados.loc[
                duplicados.groupby('sobrenome')['salario'].idxmax()]
        else:
            maiores_salarios = self.dados.loc[
                self.dados.reset_index().groupby('sobrenome')['salario'].idxmax()]

        for linha in maiores_salarios.itertuples():
            self.impressao += f'last_name_max|{linha[3]}|{linha[2]} {linha[3]}|{linha[4]:.2f}\n'


def carregar_dados(arquivo):
    """ Carrega os dados. """

    with open(arquivo, encoding='utf-8') as arquivo_json:
        dados_json = load(arquivo_json)

    funcionarios = dados_json.pop('funcionarios')
    areas = dados_json.pop('areas')

    empregado = DataFrame(funcionarios)
    setor = DataFrame(areas)
    setor.rename(columns={'codigo': 'area'}, inplace=True)
    base_dados = merge(empregado, setor, on='area', suffixes=[None, '_area'])

    return base_dados


def main(json):
    """ Função principal. """

    base = carregar_dados(json)

    dados = Informacoes(base)
    dados.geral()
    dados.area()
    dados.funcionario_area()
    dados.funcionario_sobrenome()

    print(dados.impressao, end='')


if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        raise TypeError('Informe os dois argumentos: arquivo (.py) e o arquivo (.json)')
