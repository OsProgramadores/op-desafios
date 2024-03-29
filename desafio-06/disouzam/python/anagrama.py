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


def main(args):
    """main(args):
    Processa uma expressão passada na linha de comando, descrita pelo parâmetro args
    e imprime os anagramas existentes a partir de uma busca no arquivo words.txt.

    Parâmetros:
    args: Lista de argumentos recebido da linha de comando e 
          pré-processado na chamada da função main. Deve conter 2 argumentos e 
          o segundo é uma expressão a ser processada em busca dos anagramas.
    """
    expressao = ""

    # Análise dos argumentos recebidos em args
    if len(args) <= 1:
        raise ArgumentError("Nenhum argumento foi fornecido.")

    # Validação dos argumentos
    if len(args) == 2:
        expressao = args[1]
        expressao = converte_expressao(expressao)
        if not e_valida(expressao):
            raise ArgumentError("Expressão contém caracteres inválidos")
    else:
        # pylint: disable=line-too-long
        raise ArgumentError(
            "Número excessivo de argumentos. Apenas um argumento como string é necessário para determinar os anagramas existentes.")

    letras_expressao_atual = obtem_contagem_de_letras(expressao)
    caminho_do_arquivo_com_as_palavras = obtem_caminho_do_arquivo_com_as_palavras()
    palavras_e_letras = processa_arquivo_de_palavras(
        caminho_do_arquivo_com_as_palavras)

    imprimir_todos_os_anagramas(letras_expressao_atual, palavras_e_letras)


def imprimir_todos_os_anagramas(letras_expressao_atual, palavras_e_letras):
    """imprimir_todos_os_anagramas(letras_expressao_atual, palavras_e_letras):
    Imprime todos os anagramas existentes

    Pârametros:
    letras_expressao_atual: dicionário de letras da expressão atual e sua contagem de ocorrências
    palavras_e_letras: lista de tuplas com as palavras e a respectiva contagem de letras
    """
    lista_candidatos = gera_lista_candidatos(
        letras_expressao_atual, palavras_e_letras)

    candidatos_a_anagramas = []
    lista_anagramas = gera_lista_anagramas(
        letras_expressao_atual, lista_candidatos, candidatos_a_anagramas)

    for item in lista_anagramas:
        print(item)


def gera_lista_candidatos(letras_expressao_atual, palavras_e_letras):
    """gera_lista_candidatos(letras_expressao_atual, palavras_e_letras):
    Gera lista de candidatos a compor o anagrama a partir de um dicionário de letras da 
    expressão atual e da lista de palavras do idioma selecionado

    Parâmetros:
    letras_expressao_atual: dicionário de letras da expressão atual e sua contagem de ocorrências
    palavras_e_letras: lista de tuplas com as palavras e a respectiva contagem de letras
    """
    lista_candidatos = []

    for palavra_candidata in palavras_e_letras:
        if palavra_e_candidata(
                letras_expressao_atual, palavra_candidata[1]):

            lista_candidatos.append(palavra_candidata)

    return lista_candidatos


def gera_lista_anagramas(letras_expressao_atual, candidatos, candidatos_a_anagrama):
    """ 
        Gera lista de anagramas a partir de uma lista de candidatos
    """
    # caso-base: adiciona cada palavra candidata como um possível anagrama
    if len(candidatos_a_anagrama) == 0:
        for posicao_candidato_na_lista, candidato in enumerate(candidatos):
            lista = []
            lista.append(candidato[0])
            letras_faltantes = obtem_contagem_letras_faltantes_para_um_anagrama(
                letras_expressao_atual, lista)
            total_letras_faltantes = obtem_total_letras(letras_faltantes)
            candidatos_a_anagrama.append(
                (lista, posicao_candidato_na_lista, total_letras_faltantes, letras_faltantes))

    # caso-geral
    total_candidatos = len(candidatos)
    numero_inicial_candidatos_a_anagrama = len(candidatos_a_anagrama)

    for posicao_candidato_a_anagrama, candidato_inicial in enumerate(candidatos_a_anagrama):

        if candidato_inicial[2] > 0:
            posicao_ultimo_candidato_inserido = candidato_inicial[1]
            proximo_candidato = posicao_ultimo_candidato_inserido + 1

            for posicao_novo_candidato in range(proximo_candidato, total_candidatos):
                novo_candidato = candidatos[posicao_novo_candidato]
                letras_faltantes = candidatos_a_anagrama[posicao_candidato_a_anagrama][3]

                if palavra_e_candidata(letras_faltantes, novo_candidato[1]):
                    temp_list = []
                    temp_list.append(novo_candidato[0])
                    anagrama_potencial = candidatos_a_anagrama[posicao_candidato_a_anagrama][0] + \
                        temp_list
                    letras_faltantes = obtem_contagem_letras_faltantes_para_um_anagrama(
                        letras_expressao_atual, anagrama_potencial)
                    total_letras_faltantes = obtem_total_letras(
                        letras_faltantes)
                    candidatos_a_anagrama.append(
                        (anagrama_potencial, posicao_novo_candidato, total_letras_faltantes, letras_faltantes))

    candidatos_a_anagrama_atualizado = []
    for posicao_candidato_a_anagrama, candidato in enumerate(candidatos_a_anagrama):
        if posicao_candidato_a_anagrama < numero_inicial_candidatos_a_anagrama:
            # Candidatos iniciais podem ser anagramas
            if candidato[2] == 0:
                candidatos_a_anagrama_atualizado.append(candidato)
        else:
            # Os os demais candidatos serão adicionados automaticamente
            candidatos_a_anagrama_atualizado.append(candidato)

    # Verifica se há candidatos que necessitam de busca extra
    nova_busca = False
    for candidato in candidatos_a_anagrama_atualizado:
        if candidato[2] != 0:
            nova_busca = True

    if nova_busca:
        candidatos_a_anagrama_atualizado = gera_lista_anagramas(letras_expressao_atual,
                                                                candidatos, candidatos_a_anagrama_atualizado)

    return candidatos_a_anagrama_atualizado


def obtem_total_letras(letras_faltantes):
    """
        Calcula o total de letras faltantes
    """
    total = 0
    for letra in letras_faltantes:
        total += letras_faltantes[letra]

    return total


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
    letras_anagrama_potencial = obtem_contagem_de_letras(string_concatenada)

    if len(letras_expressao_atual) != len(letras_anagrama_potencial):
        return False

    for letra in letras_expressao_atual:
        if letras_expressao_atual[letra] != letras_anagrama_potencial[letra]:
            return False

    return True


def obtem_caminho_do_arquivo_com_as_palavras():
    """obtem_caminho_do_arquivo_com_as_palavras:
    Obtém o caminho para o arquivo com as palavras do idioma selecionado para a busca dos anagramas
    """
    # Execução como script através do VS Code
    file_path = os.path.join("desafio-06", "disouzam", "python", "words.txt")

    if not os.path.isfile(file_path):
        # Execução como módulo via linha de comando a partir do diretório do desafio
        file_path = os.path.join("words.txt")

    return file_path


def processa_arquivo_de_palavras(file_path):
    """processa_arquivo_de_palavras(file_path):
    Processa o arquivo 'words.txt' e retorna um vetor de tuplas com a palavra como primeiro item e 
    a contagem de letras como segundo item

    Parâmetros:
    file_path: Caminho do arquivo contendo as palavras do idioma selecionado
    """
    palavras_e_letras = []

    with open(file_path, "r", encoding='UTF-8') as words_file:
        for word in words_file:
            word = word.strip()
            contagem_de_letras = obtem_contagem_de_letras(word)
            palavras_e_letras.append((word, contagem_de_letras))

    return palavras_e_letras


def palavra_e_candidata(letras_expressao_atual, letras_palavra_candidata):
    """
        Verifica se palavra_candidata pode compor anagrama da expressão atual
        representada por sua versão em contagem de letras
    """
    if not isinstance(letras_palavra_candidata, dict):
        raise ArgumentError("letras_palavra_candidata deve ser um dicionário")

    for letra in letras_palavra_candidata:
        if letra not in letras_expressao_atual or \
                letras_palavra_candidata[letra] > letras_expressao_atual[letra]:
            return False

    return True


def obtem_contagem_de_letras(expressao):
    """obtem_contagem_de_letras(expressao):
    Processa a `expressao` e conta o número de ocorrências de cada letra da palavra ou frase
    e retorna o resultado como um dicionário onde a chave é a letra e o valor é o número
    de ocorrências.

    Parâmetros:
    expressao: Uma palavra ou frase contendo somente letras e espaços. 
               Acentos e pontuação não são permitidos.
    """
    contagem_letras = {}
    for letra in expressao:
        if letra in contagem_letras:
            contagem_letras[letra] += 1
        else:
            contagem_letras[letra] = 1
    return contagem_letras


def obtem_contagem_letras_faltantes_para_um_anagrama(letras_expressao_atual, lista_de_strings):
    """
        Processa a expressao e calcula o número de letras faltantes para formação de um anagrama
        a partir da lista fornecida
    """
    letras_da_lista_atual = conta_letras_de_uma_lista(lista_de_strings)
    letras_faltantes = {}

    for letra in letras_expressao_atual:
        if letra in letras_da_lista_atual:
            letras_faltantes[letra] = letras_expressao_atual[letra] - \
                letras_da_lista_atual[letra]
        else:
            letras_faltantes[letra] = letras_expressao_atual[letra]

    return letras_faltantes


def conta_letras_de_uma_lista(lista_de_strings):
    """
        Processa a expressao e conta o número de ocorrências de cada letra da palavra ou frase em
        uma lista de strings
    """
    string_concatenada = "".join(lista_de_strings)
    contagem_letras = {}
    for letra in string_concatenada:
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
    print(main.__doc__)
    print(obtem_contagem_de_letras.__doc__)
    print(obtem_caminho_do_arquivo_com_as_palavras.__doc__)
    print(processa_arquivo_de_palavras.__doc__)
    print(gera_lista_candidatos.__doc__)
    print(imprimir_todos_os_anagramas.__doc__)
    main(sys.argv)
