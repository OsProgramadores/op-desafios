"""
Esse modulo tem como objetivo de processar determinados dados de funcionarios
atraves de um arquivo "json".
"""

import json
from heapq import (nsmallest, nlargest)
import sys
import time
from collections import Counter
from statistics import mean
import numpy as np


class ParserDesafio5:
    """
    Classe realiza a leitura de um arquivo de funcionarios em json e "printa"
    determinados dados referentes a esse arquivo.
    """

    def __init__(self, arquivo):
        dado_geral = self.leitura_arquivo(arquivo)
        self._dicionario_funcionarios = dado_geral['funcionarios']
        self._dicionario_areas = self.converter_chave_valor_dicionario_areas(dado_geral['areas'])
        self._funcionario_maior_salario = None
        self._funcionario_menor_salario = None

    @classmethod
    def converter_chave_valor_dicionario_areas(cls, dicionario):
        """
        Converte uma lista dicionarios em dicionario sendo o codigo como a chave e
        e o nome como valor.
        """

        return {
            dicionario_chave_valor['codigo']:
            dicionario_chave_valor['nome']
            for dicionario_chave_valor in dicionario
        }

    @classmethod
    def leitura_arquivo(cls, path_arquivo):
        """
        Metodo realiza a leitura do arquivo json.
        """

        with open(path_arquivo) as arquivo:
            dados_arquivo = json.load(arquivo)

        return dados_arquivo

    def _questao_1_ranking_media_funcionario(self):
        # start = time.time()
        self._funcionario_menor_salario = nsmallest(
            len(
                self._dicionario_funcionarios
            ),
            self._dicionario_funcionarios,
            key=lambda s: s['salario']
        )

        self._funcionario_maior_salario = nlargest(
            len(
                self._dicionario_funcionarios
            ),
            self._dicionario_funcionarios,
            key=lambda s: s['salario']
        )

        lista_salarios = np.array([d['salario'] for d in self._dicionario_funcionarios])

        salario_menor = self._funcionario_menor_salario[0].get('salario')
        for funcionario in self._funcionario_menor_salario:
            if salario_menor == funcionario.get("salario"):
                print(f'global_min|{funcionario.get("nome")} '
                      f'{funcionario.get("sobrenome")}|'
                      f'{funcionario.get("salario")}')
                continue

            break


        salario_maior = self._funcionario_maior_salario[0].get('salario')
        for funcionario in self._funcionario_maior_salario:
            if salario_maior == funcionario.get("salario"):
                print(f'global_max|'
                      f'{funcionario.get("nome")} '
                      f'{funcionario.get("sobrenome")}|'
                      f'{funcionario.get("salario")}')
                continue

            break

        print(f'global_avg|{"{0:.2f}".format(mean(lista_salarios.shape))}')

        # end = time.time()
        # print(f'Part 1 - Tempo: {end - start}')

    def _questao_2_ranking_media_area(self):
        # start = time.time()
        salario_maior = self._funcionario_maior_salario[0].get('salario')
        for funcionario in self._funcionario_maior_salario:
            if salario_maior == funcionario.get("salario"):
                print(f'area_max|'
                      f'{self._dicionario_areas[funcionario.get("area")]}|'
                      f'{funcionario.get("nome")} {funcionario.get("sobrenome")}|'
                      f'{funcionario.get("salario")}')
                continue

            break


        salario_menor = self._funcionario_menor_salario[0].get('salario')
        for funcionario in self._funcionario_menor_salario:
            if salario_menor == funcionario.get("salario"):
                print(f'area_min|'
                      f'{self._dicionario_areas[funcionario.get("area")]}|'
                      f'{funcionario.get("nome")} {funcionario.get("sobrenome")}|'
                      f'{funcionario.get("salario")}')
                continue
            break


        lista_area = [d['area'] for d in self._dicionario_funcionarios]

        for item in set(lista_area):
            lista_salario = [
                                d['salario']
                                for d in self._dicionario_funcionarios
                                if d.get("area") == item
            ]

            print(f'area_avg|'
                  f'{self._dicionario_areas[item]}|'
                  f'{"{0:.2f}".format(mean(lista_salario))}')

        # end = time.time()
        # print(f'Part 2 - Tempo: {end - start}')

    def _questao_3_maior_menor_numero_funcionarios(self):
        lista_area = [d['area'] for d in self._dicionario_funcionarios]
        # start = time.time()
        word_counts = Counter(lista_area)
        area_mais_funcionario = word_counts.most_common(len(lista_area))[0]
        area_menos_funcionario = word_counts.most_common(len(lista_area)).pop()

        print(f'least_employees|'
              f'{self._dicionario_areas[area_menos_funcionario[0]]}|'
              f'{area_menos_funcionario[1]}')
        print(f'most_employees|'
              f'{self._dicionario_areas[area_mais_funcionario[0]]}|'
              f'{area_mais_funcionario[1]}')

        # end = time.time()
        # print(f'Part 3 - Tempo: {end - start}')

    def _questao_4_maiores_salarios_pelo_sobrenome(self):
        # start = time.time()
        todos_sobrenomes = [d['sobrenome'] for d in self._dicionario_funcionarios]

        word_counts = Counter(todos_sobrenomes)
        sobrenome = word_counts.most_common()[0]
        sobrenome_usuario_maior_salario = [
            funcionario
            for funcionario in self._funcionario_maior_salario
            if funcionario.get('sobrenome') == sobrenome[0]
        ]

        salario_maior = sobrenome_usuario_maior_salario[0].get('salario')
        for funcionario in sobrenome_usuario_maior_salario:
            if funcionario.get("salario") == salario_maior:
                print(f'last_name_max|'
                      f'{funcionario.get("sobrenome")}|'
                      f'{funcionario.get("nome")} {funcionario.get("sobrenome")}|'
                      f'{funcionario.get("salario")}')
                continue
            break

        # end = time.time()
        # print(f'Part 4 - Tempo: {end - start}')

    def output_geral(self):
        """
        Metodo chama todos os outros metodos referentes as questoes com seus
        respectivos dados printados.
        """
        self._questao_1_ranking_media_funcionario()
        self._questao_2_ranking_media_area()
        self._questao_3_maior_menor_numero_funcionarios()
        self._questao_4_maiores_salarios_pelo_sobrenome()

    def output_geral_com_tempo(self):
        """
        Metodo calcula o tempo de execucao do metodo "output_geral" e printa o tempo
        total. Seu uso es somente para fins de analise de perfomance.
        """
        start = time.time()
        self.output_geral()
        end = time.time()
        print(f'Tempo: {end - start}')


if __name__ == '__main__':
    ARQUIVO = sys.argv[1]
    PARSER = ParserDesafio5(ARQUIVO)
    PARSER.output_geral()
