"""
    Processa uma palavra ou frase e retorna todas as combinações possíveis de anagramas com palavras
    presentes no arquivo desafio-06/disouzam/python/words.txt (cópia local do arquivo disponível em
    https://osprogramadores.com/desafios/d06/words.txt)
"""
from ctypes import ArgumentError
import os
import string
import sys
import re
import traceback
import numpy as np


def main(args):
    """
        Processa os valores passados na linha de comando, descritos pelo parâmetro args
        e retorna todos os palíndromos entre o limite inferior e o limite superior, ambos
        inclusos na avaliação de números palíndromos
    """
    expressao = ""

    # Análise dos argumentos recebidos em args
    if len(args) <= 1:
        print("Nenhum argumento foi fornecido.")
        return

    if len(args) == 2:
        expressao = args[1]
        expressao = converte_expressao(expressao)
        if not e_valida(expressao):
            raise ArgumentError("Expressão contém caracteres inválidos")

    letras_expressao_atual = conta_letras(expressao)
    palavras_e_letras = processa_arquivo_de_palavras()

    imprimir_todos_os_anagramas(letras_expressao_atual, palavras_e_letras)


def imprimir_todos_os_anagramas(letras_expressao_atual, palavras_e_letras):
    """
        Imprime todos os anagramas existentes
    """
    lista_candidatos = gera_lista_candidatos(
        letras_expressao_atual, palavras_e_letras)
    lista_anagramas = gera_lista_anagramas(
        letras_expressao_atual, lista_candidatos)

    for anagrama in lista_anagramas:
        print(" ".join(anagrama))


def gera_lista_candidatos(letras_expressao_atual, palavras_e_letras):
    """
        Gera lista de candidatos a compor o anagrama
    """
    lista_candidatos = []

    for _, palavra_candidata in enumerate(palavras_e_letras):
        if palavra_e_candidata(
                letras_expressao_atual, palavra_candidata[1]):

            lista_candidatos.append(palavra_candidata)

    return lista_candidatos


def gera_lista_anagramas(letras_expressao_atual, candidatos):
    """ 
        Gera lista de anagramas a partir de uma lista de candidatos
    """
    lista_anagramas = []
    anagrama = []

    # pylint: disable=consider-using-enumerate
    for i in range(0, len(candidatos)):
        anagrama = obter_anagrama_for_candidato_comecando_no_indice_i(
            letras_expressao_atual, candidatos, i)

        if anagrama is not None:
            lista_anagramas.append(anagrama)

    return lista_anagramas


def obter_anagrama_for_candidato_comecando_no_indice_i(letras_expressao_atual, candidatos, i):
    """
        Obtem um anagrama comecando com candidatos[i]
    """
    tb = traceback.extract_stack()
    list_tb = list(tb)
    new_list = list(filter(lambda x: x.name ==
                    "get_anagrama_for_candidato_starting_at_index_i", list_tb))
    recursive_calls_length = len(new_list)

    anagrama = []
    antigas_letras_expressao_atual = letras_expressao_atual
    novas_letras_expressao_atual = {}
    candidato = candidatos[i]
    anagrama.append(candidato[0])

    # pylint: disable=line-too-long
    print(
        f"\n\nChamada: {recursive_calls_length} - i: {i} - candidato: {candidato[0]} - Num de Candidatos: {len(candidatos)}")

    candidato_valido = True
    letras_remanescentes = 0
    for letra in antigas_letras_expressao_atual:

        # Calculate a quantidade de letras remanescentes se o candidato atual for incluído
        # no anagrama
        if letra in candidato[1]:
            novas_letras_expressao_atual[letra] = antigas_letras_expressao_atual[letra] - \
                candidato[1][letra]
        else:
            novas_letras_expressao_atual[letra] = antigas_letras_expressao_atual[letra]

        letras_remanescentes += novas_letras_expressao_atual[letra]
        if novas_letras_expressao_atual[letra] < 0:
            candidato_valido = False
            break

    # Candidato ainda não foi invalidado por ter letras a mais do que o necessário
    if candidato_valido:
        for letra in candidato[1]:
            # Candidato será invalidado por ter letras que não estão na expressão original
            if letra not in antigas_letras_expressao_atual:
                candidato_valido = False
                break

    if not candidato_valido:
        anagrama.pop()

    if not candidato_valido or letras_remanescentes == 0:
        return anagrama

    sub_anagrama_encontrado = False

    for j in range(i+1, len(candidatos)):
        print(
            f"j: {j} - candidato: {candidatos[j][0]} - Num de Candidatos: {len(candidatos)}")
        sub_anagrama = obter_anagrama_for_candidato_comecando_no_indice_i(
            novas_letras_expressao_atual, candidatos, j)

        if sub_anagrama == [] or sub_anagrama is None:
            continue

        sub_anagrama_encontrado = True
        anagrama = anagrama + sub_anagrama

        if e_um_anagrama(letras_expressao_atual, anagrama):
            break

    if sub_anagrama_encontrado:
        return anagrama


def e_um_anagrama(letras_expressao_atual, anagrama):
    """
        Verifica se um anagrama está correto
    """
    string_concatenada = "".join(anagrama)
    letras_anagrama_potencial = conta_letras(string_concatenada)

    if len(letras_expressao_atual) != len(letras_anagrama_potencial):
        return False

    for letra in letras_expressao_atual:
        if letras_expressao_atual[letra] != letras_anagrama_potencial[letra]:
            return False

    return True


def processa_arquivo_de_palavras():
    """
        Processa o arquivo 'words.txt' e retorna um dicionário com a palavra e a contagem de letras 
        nela
    """
    # Execução como script através do VS Code
    file_path = os.path.join("desafio-06", "disouzam", "python", "words.txt")

    if not os.path.isfile(file_path):
        # Execução como módulo via linha de comando a partir do diretório do desafio
        file_path = os.path.join("words.txt")

    palavras_e_letras = {}

    with open(file_path, "r", encoding='UTF-8') as words_file:
        for word in words_file:
            word = word.strip()
            palavras_e_letras[word] = conta_letras(word)

    items = palavras_e_letras.items()
    data = list(items)
    palavras_e_letras_como_array = np.array(data)

    return palavras_e_letras_como_array


def palavra_e_candidata(letras_expressao_atual, letras_palavra_candidata):
    """
        Verifica se palavra_candidata pode compor anagrama da expressão atual
        representada por sua versão em contagem de letras
    """

    for letra in letras_palavra_candidata:
        if letra not in letras_expressao_atual or \
                letras_palavra_candidata[letra] > letras_expressao_atual[letra]:
            return False

    return True


def conta_letras(expressao):
    """
        Processa a expressao e conta o número de ocorrências de cada letra da palavra ou frase
    """
    contagem_letras = {}
    for letra in expressao:
        if letra in contagem_letras:
            contagem_letras[letra] += 1
        else:
            contagem_letras[letra] = 1
    return contagem_letras


def converte_expressao(expressao):
    """
        Converte expressão para letras maiúsculas e remove os espaços existentes
    """
    # Primeiro converte todas as letras em maiúsculas
    result = expressao.upper()

    # pylint: disable=line-too-long
    # Depois remove os espaços em branco https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string#remove-all-spaces-using-the-replace-method
    result = result.replace(" ", "")

    return result


def e_valida(expressao):
    """
        Verifica se a expressão fornecida como argumento contém caracteres inválidos
    """
    # https://www.geeksforgeeks.org/string-punctuation-in-python/
    for letra in expressao:
        if letra in string.punctuation:
            return False

    # https://stackoverflow.com/a/22162423
    if not re.match('^[a-zA-Z]+$', expressao):
        return False

    return True


if __name__ == "__main__":
    main(sys.argv)
