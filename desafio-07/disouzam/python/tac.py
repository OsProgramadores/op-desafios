"""
    Implementação do comando _tac_ que lê um arquivo e exibe as linhas em ordem inversa - da última para a primeira
"""
from ctypes import ArgumentError
import os
import sys


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

    imprimir_arquivo_em_ordem_normal(caminho_do_arquivo)


def imprimir_arquivo_em_ordem_normal(caminho_do_arquivo):
    """imprimir_arquivo_em_ordem_normal(caminho_do_arquivo):
    Abre o arquivo especificado pelo caminho fornecido e imprime seu conteúdo em ordem normal

    Parâmetros:
    caminho_do_arquivo: Caminho do arquivo no disco
    """
    with open(caminho_do_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha, end='')


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
