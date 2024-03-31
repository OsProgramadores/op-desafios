"""
    Implementação do comando _tac_ que lê um arquivo e exibe as linhas em ordem inversa
    - da última linha para a primeira a primeira linha
"""
from ctypes import ArgumentError
import os
import sys
import linecache


def main(args):
    """main(args):
    Processa o arquivo texto e retorna as linhas, da última para a primeira, diretamente no
    console.

    Parâmetros:
    args: Lista de argumentos recebido da linha de comando e
          pré-processado na chamada da função main. Deve conter 2 argumentos e
          o segundo é o caminho para o arquivo a ser processado.
    """
    # Análise dos argumentos recebidos em args
    if len(args) <= 1:
        raise ArgumentError("Nenhum argumento foi fornecido.")

    # Validação dos argumentos
    if len(args) == 2:
        caminho_do_arquivo = args[1]
        if not os.path.isfile(caminho_do_arquivo):
            raise FileNotFoundError("Arquivo inexistente ou caminho inválido.")
    else:
        raise ArgumentError(
            "Número excessivo de argumentos. \
            Apenas um argumento com o caminho do arquivo é aceito.")

    imprimir_arquivo_em_ordem_reversa(caminho_do_arquivo)


def imprimir_arquivo_em_ordem_normal(caminho_do_arquivo):
    """imprimir_arquivo_em_ordem_normal(caminho_do_arquivo):
    Abre o arquivo especificado pelo caminho fornecido e imprime seu conteúdo em ordem normal

    Parâmetros:
    caminho_do_arquivo: Caminho do arquivo no disco
    """
    with open(caminho_do_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha, end='')


def imprimir_arquivo_em_ordem_reversa(caminho_do_arquivo):
    """imprimir_arquivo_em_ordem_reversa(caminho_do_arquivo):
    Abre o arquivo especificado pelo caminho fornecido e imprime seu conteúdo em ordem reversa

    Parâmetros:
    caminho_do_arquivo: Caminho do arquivo no disco
    """
    numero_linhas_arquivo = obter_a_ultima_linha_do_arquivo(caminho_do_arquivo)

    numero_da_linha = numero_linhas_arquivo
    while numero_da_linha >= 1:
        conteudo_linha = linecache.getline(
            caminho_do_arquivo, numero_da_linha)
        print(conteudo_linha, end='')
        numero_da_linha -= 1


def obter_a_ultima_linha_do_arquivo(caminho_do_arquivo):
    """obter_a_ultima_linha_do_arquivo(caminho_do_arquivo):
    Obtém através de uma busca pelo método da bisseção o número da última linha do arquivo

    Parâmetros:
    caminho_do_arquivo: Caminho do arquivo no disco
    """
    result = 0
    linha_inexistente = ''

    # Verifica primeira linha do arquivo
    conteudo_linha = linecache.getline(caminho_do_arquivo, 1)

    # Arquivo vazio
    if conteudo_linha == linha_inexistente:
        result = 0

    ultima_linha_potencial = 1
    conteudo_linha = linecache.getline(
        caminho_do_arquivo, ultima_linha_potencial)

    while conteudo_linha != linha_inexistente:
        ultima_linha_potencial *= 2
        conteudo_linha = linecache.getline(
            caminho_do_arquivo, ultima_linha_potencial)

    ultimo = ultima_linha_potencial
    meio = int(ultimo/2)

    while meio < ultimo:
        conteudo_linha_meio = linecache.getline(
            caminho_do_arquivo, meio)

        conteudo_linha_seguinte = linecache.getline(
            caminho_do_arquivo, meio + 1)

        # Caso 1: linha do meio e a seguinte estão no meio do arquivo de fato
        if linha_inexistente not in (conteudo_linha_meio, conteudo_linha_seguinte):
            meio = meio + int((ultimo - meio)/2)

        # Caso 2: linha do meio e a seguinte estão após o final do arquivo
        if conteudo_linha_meio == linha_inexistente and \
                conteudo_linha_seguinte == linha_inexistente:
            ultimo = meio + 1
            meio = int(ultimo/2)

        # Caso 3: linha do meio é a última linha do arquivo
        if conteudo_linha_meio != linha_inexistente and \
                conteudo_linha_seguinte == linha_inexistente:
            break

    result = meio

    return result


def debugger_is_active() -> bool:
    """Return if the debugger is currently active

    # pylint: disable=line-too-long
    Source: https://stackoverflow.com/questions/38634988/check-if-program-runs-in-debug-mode/67065084
    """
    return hasattr(sys, 'gettrace') and sys.gettrace() is not None


if __name__ == "__main__":
    if debugger_is_active():
        print(main.__doc__)
    main(sys.argv)
