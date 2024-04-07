"""
    Implementação do comando _tac_ que lê um arquivo e exibe as linhas em ordem inversa
    - da última linha para a primeira a primeira linha
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
    # TODO: Adicionar variável para representar o len(args)
    if len(args) <= 1:
        raise ArgumentError("Nenhum argumento foi fornecido.")

    # Validação dos argumentos
    if len(args) >= 2:
        _ = args[1]

    if len(args) > 2:
        mensagem1 = f"Você informou um número excessivo de argumentos({len(args) - 1}). "
        mensagem1 += "Apenas um argumento como string é necessário para "
        mensagem1 += "determinar os anagramas existentes."
        print(mensagem1)

        mensagem2 = "Deseja prosseguir ignorando os demais argumentos? (S para Sim e N para não)"
        escolha_do_usuario = input(mensagem2)

        if escolha_do_usuario.lower() != "s":
            print("Programa abortado.")
            return


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
