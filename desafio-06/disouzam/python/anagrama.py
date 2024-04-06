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
    if len(args) >= 2:
        expressao = args[1]
        expressao = converte_expressao(expressao)
        if not expressao_e_valida(expressao):
            raise ArgumentError("Expressão contém caracteres inválidos")

    if len(args) > 2:
        mensagem1 = f"Você informou um número excessivo de argumentos ({
            len(args) - 1}). "
        mensagem1 += "Apenas um argumento como string é necessário para "
        mensagem1 += "determinar os anagramas existentes."
        print(mensagem1)

        mensagem2 = "Deseja prosseguir ignorando os demais argumentos? (S para Sim e N para não)"
        escolha_do_usuario = input(mensagem2)

        if escolha_do_usuario.lower() != "s":
            print("Programa abortado.")
            return

    letras_expressao_atual = obtem_contagem_de_letras(expressao)
    caminho_do_arquivo_com_as_palavras = obtem_caminho_do_arquivo_com_as_palavras()
    palavras_e_letras = processa_arquivo_de_palavras(
        caminho_do_arquivo_com_as_palavras)

    anagramas = encontrar_anagramas(letras_expressao_atual, palavras_e_letras)
    imprimir_todos_os_anagramas(anagramas)


def encontrar_anagramas(letras_expressao_atual, palavras_e_letras):
    """encontrar_anagramas(letras_expressao_atual, palavras_e_letras):
    Encontra todos os anagramas existentes a partir das letras da expressão atual e
    das palavras e letras do idioma selecionado

    Pârametros:
    letras_expressao_atual: dicionário de letras da expressão atual e sua contagem de ocorrências
    palavras_e_letras: lista de tuplas com as palavras e a respectiva contagem de letras
    """
    lista_candidatos = gera_lista_candidatos(
        letras_expressao_atual, palavras_e_letras)

    candidatos_a_anagramas = []
    lista_anagramas = gera_lista_anagramas(
        letras_expressao_atual, lista_candidatos, candidatos_a_anagramas)

    lista_anagramas_sem_repeticao = gera_lista_anagramas_sem_repeticao(
        lista_anagramas)

    lista_ordenada = obtem_lista_ordenada_como_strings(
        lista_anagramas_sem_repeticao)

    return lista_ordenada


def imprimir_todos_os_anagramas(anagramas):
    """imprimir_todos_os_anagramas(letras_expressao_atual, palavras_e_letras):
    Imprime todos os anagramas existentes

    Pârametros:
    anagramas: Lista ordenada dos anagramas a serem impressos
    """
    for item in anagramas:
        print(item)


def obtem_lista_ordenada_como_strings(lista_anagramas_sem_repeticao):
    """obtem_lista_ordenada_como_strings(lista_anagramas_sem_repeticao):
    Concatena as sublistas como strings e retorna valores ordenados

    Parâmetro:
    lista_anagramas_sem_repeticao: lista de listas de anagramas sem repeticao
    """
    lista_ordenada = []

    for item in lista_anagramas_sem_repeticao:
        lista_ordenada.append(" ".join(item))

    lista_ordenada.sort()

    return lista_ordenada


def gera_lista_anagramas_sem_repeticao(lista_anagramas):
    """gera_lista_anagramas_sem_repeticao(lista_anagramas):
    Processa a lista final de anagramas obtida e remove duplicatas e transforma a tupla em uma lista
    de listas simples

    Parâmetro:
    lista_anagramas: lista de anagramas válidos contendo repeticao
    """
    lista_sem_repeticao = []

    for anagrama in lista_anagramas:
        if anagrama[0] not in lista_sem_repeticao:
            lista_sem_repeticao.append(anagrama[0])

    return lista_sem_repeticao


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
    """gera_lista_anagramas(letras_expressao_atual, candidatos, candidatos_a_anagrama):
    Gera lista de anagramas a partir de uma lista de candidatos

    Parâmetros:
    letras_expressao_atual: dicionário de letras da expressão atual e sua contagem de ocorrências
    candidatos: lista de palavras candidatas a formar um anagrama
    candidatos_a_anagrama: lista de candidatos a anagrama em construção incremental
    """

    # caso-base: adiciona cada palavra candidata como um possível anagrama
    if len(candidatos_a_anagrama) == 0:
        candidatos_a_anagrama = obtem_candidatos_iniciais(
            letras_expressao_atual, candidatos)

    # caso-geral
    candidatos_continuam_viaveis = [False] * len(candidatos)
    numero_inicial_candidatos_a_anagrama = len(candidatos_a_anagrama)

    candidatos_a_anagrama_nao_filtrado = candidatos_a_anagrama.copy()
    for posicao_candidato_a_anagrama, candidato_inicial in enumerate(candidatos_a_anagrama):
        candidatos_a_anagrama_nao_filtrado = busca_novos_anagramas(
            letras_expressao_atual,
            candidatos,
            candidatos_continuam_viaveis,
            candidatos_a_anagrama_nao_filtrado,
            posicao_candidato_a_anagrama,
            candidato_inicial)

    candidatos_a_anagrama = filtra_candidatos_a_anagrama_invalidos(
        candidatos_a_anagrama_nao_filtrado, numero_inicial_candidatos_a_anagrama)

    # Verifica se há candidatos que necessitam de busca extra
    nova_busca = False
    for candidato in candidatos_a_anagrama:
        if candidato[2] != 0:
            nova_busca = True
            break

    if nova_busca:
        candidatos_filtrados = []

        for posicao, item in enumerate(candidatos):
            if candidatos_continuam_viaveis[posicao]:
                candidatos_filtrados.append(item)

        candidatos = candidatos_filtrados

        candidatos_a_anagrama = gera_lista_anagramas(letras_expressao_atual,
                                                     candidatos, candidatos_a_anagrama)

    return candidatos_a_anagrama


def filtra_candidatos_a_anagrama_invalidos(candidatos_a_anagrama,
                                           numero_inicial_candidatos_a_anagrama):
    """filtra_candidatos_a_anagrama_invalidos(candidatos_a_anagrama,
                                                numero_inicial_candidatos_a_anagrama):
    Filtra os candidatos a anagrama que já estão desatualizados (foram incrementalmente modificados)

    Parâmetros:
    candidatos_a_anagrama: lista de candidatos a anagrama em construção incremental
    numero_inicial_candidatos_a_anagrama: número inicial de candidatos a anagrama
    """
    candidatos_a_anagrama_atualizado = []
    for posicao_candidato_a_anagrama, candidato in enumerate(candidatos_a_anagrama):
        if posicao_candidato_a_anagrama < numero_inicial_candidatos_a_anagrama:
            # Candidatos iniciais podem ser anagramas
            if candidato[2] == 0:
                candidatos_a_anagrama_atualizado.append(candidato)
        else:
            # Os os demais candidatos serão adicionados automaticamente
            candidatos_a_anagrama_atualizado.append(candidato)

    return candidatos_a_anagrama_atualizado


def busca_novos_anagramas(letras_expressao_atual,
                          candidatos,
                          viabilidade_candidatos,
                          candidatos_a_anagrama,
                          posicao_candidato_a_anagrama,
                          candidato_inicial):
    """busca_novos_anagramas(letras_expressao_atual,
                          candidatos,
                          viabilidade_candidatos
                          candidatos_a_anagrama,
                          posicao_candidato_a_anagrama,
                          candidato_inicial):
    Busca novas combinações que possam ser candidatos em potencial de um anagrama

    Parâmetros:
    letras_expressao_atual: dicionário de letras da expressão atual e sua contagem de ocorrências
    candidatos: lista de palavras candidatas a formar um anagrama
    viabilidade_candidatos: registra se houve uso de algum dos candidatos em uma busca completa pela
                            lista de candidatos
    candidatos_a_anagrama: lista de candidatos a anagrama em construção incremental
    posicao_candidato_a_anagrama: posição do último candidato que entrou no anagrama em construção
    candidato_inicial: candidato a anagram em construção
    """
    total_candidatos = len(candidatos)

    if candidato_inicial[2] > 0:
        posicao_ultimo_candidato_inserido = candidato_inicial[1]
        proximo_candidato = posicao_ultimo_candidato_inserido + 1

        for posicao_novo_candidato in range(proximo_candidato, total_candidatos):
            viabilidade_candidatos[posicao_novo_candidato] = True
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
                    (anagrama_potencial,
                     posicao_novo_candidato,
                     total_letras_faltantes,
                     letras_faltantes))

    return candidatos_a_anagrama


def obtem_candidatos_iniciais(letras_expressao_atual, candidatos):
    """obtem_candidatos_iniciais(letras_expressao_atual, candidatos):
    Obtém a lista inicial de candidatos a anagrama a partir de uma lista simples de palavras
    candidatas e as letras da expressão atual

    Parâmetros:
    letras_expressao_atual: dicionário de letras da expressão atual e sua contagem de ocorrências
    candidatos: lista de palavras candidatas a formar um anagrama
    """
    candidatos_a_anagrama = []
    for posicao_candidato_na_lista, candidato in enumerate(candidatos):
        lista = []
        lista.append(candidato[0])
        letras_faltantes = obtem_contagem_letras_faltantes_para_um_anagrama(
            letras_expressao_atual, lista)
        total_letras_faltantes = obtem_total_letras(letras_faltantes)
        candidatos_a_anagrama.append(
            (lista, posicao_candidato_na_lista, total_letras_faltantes, letras_faltantes))

    return candidatos_a_anagrama


def obtem_total_letras(letras_faltantes):
    """obtem_total_letras(letras_faltantes):
    Calcula o total de letras faltantes

    Parâmetro:
    letras_faltantes: dicionário com o número de letras faltantes por letra
    """
    total = 0
    for letra in letras_faltantes:
        total += letras_faltantes[letra]

    return total


def e_um_anagrama(letras_expressao_atual, anagrama):
    """e_um_anagrama(letras_expressao_atual, anagrama):
    Verifica se um anagrama está correto

    Parâmetros:
    letras_expressao_atual: dicionário de letras da expressão atual e sua contagem de ocorrências
    anagrama: anagrama em potencial para ser checado
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
    """palavra_e_candidata(letras_expressao_atual, letras_palavra_candidata):
    Verifica se palavra_candidata pode compor anagrama da expressão atual
    representada por sua versão em contagem de letras

    Parâmetros:
    letras_expressao_atual: dicionário de letras da expressão atual e sua contagem de ocorrências
    letras_palavra_candidata: dicionário de letras da palavra candidata com sua
                              contagem de ocorrências
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
    """obtem_contagem_letras_faltantes_para_um_anagrama(letras_expressao_atual, lista_de_strings):
    Processa a expressao e calcula o número de letras faltantes para formação de um anagrama
    a partir da lista fornecida

    Parâmetros:
    letras_expressao_atual: dicionário de letras da expressão atual e sua contagem de ocorrências
    lista_de_strings: lista de palavras que podem formar um anagrama
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
    """conta_letras_de_uma_lista(lista_de_strings):
    Processa a expressao e conta o número de ocorrências de cada letra da palavra ou frase em
    uma lista de strings

    Parâmetro:
    lista_de_strings: lista de palavras que podem formar um anagrama
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
    """converte_expressao(expressao):
    Converte expressão para letras maiúsculas e remove os espaços existentes

    Parâmetro:
    expressao: palavra ou frase a ser processada em busca de anagramas
    """
    # Primeiro converte todas as letras em maiúsculas
    result = expressao.upper()

    # pylint: disable=line-too-long
    # Depois remove os espaços em branco https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string#remove-all-spaces-using-the-replace-method
    result = result.replace(" ", "")

    return result


def expressao_e_valida(expressao):
    """expressao_e_valida(expressao):
    Verifica se a expressão fornecida como argumento contém caracteres inválidos

    Parâmetro:
    expressao: palavra ou frase a ser processada em busca de anagramas
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
