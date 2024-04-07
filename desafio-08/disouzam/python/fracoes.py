"""
    Implementação do comando _tac_ que lê um arquivo e exibe as linhas em ordem inversa
    - da última linha para a primeira a primeira linha
"""
from ctypes import ArgumentError
import os
import sys


def main(args):
    """main(args):
    Processa o arquivo texto passado como parâmetro contendo frações a serem analisadas e retorna
    no console 

    Parâmetros:
    args: Lista de argumentos recebido da linha de comando e
          pré-processado na chamada da função main. Deve conter 1 argumento apenas indicando
          o caminho relativo ou absoluto do arquivo contendo frações a serem analisadas.
    """
    # Análise dos argumentos recebidos em args
    nargs = len(args)
    if nargs == 0:
        raise ArgumentError("Nenhum argumento foi fornecido.")

    elementos_fracoes = []
    # Validação dos argumentos
    if nargs >= 1:
        caminho_do_arquivo_fracoes = args[0]

        if not os.path.isfile(caminho_do_arquivo_fracoes):
            mensagem1 = "Arquivo não encontrado. Caminho fornecido ou nome do arquivo incorreto."
            print(mensagem1)
            return
        else:
            with open(caminho_do_arquivo_fracoes, "r", encoding='utf-8') as arquivo:
                for linha in arquivo:
                    linha_processada = linha.split("\n")
                    numerador_e_denominador = linha_processada[0].split("/")
                    elementos_fracoes.append(numerador_e_denominador)

    if nargs >= 2:
        mensagem1 = f"Você informou um número excessivo de argumentos ({nargs}). "
        mensagem1 += "Apenas um argumento que aponte o caminho (relativo ou absoluto) "
        mensagem1 += "do arquivo contendo frações a serem processadas é necessário."
        print(mensagem1)

        mensagem2 = "Deseja prosseguir ignorando os demais argumentos? (S para Sim e N para não)"
        escolha_do_usuario = input(mensagem2)

        if escolha_do_usuario.lower() != "s":
            print("Programa abortado.")
            return

    fracoes_simples = obtem_fracoes_simples(elementos_fracoes)

    for fracao in fracoes_simples:
        print(fracao)


def obtem_fracoes_simples(elementos_fracoes):
    """obtem_fracoes_simples(elementos_fracoes):
    Processa uma lista contendo listas com elementos de frações e retorna uma lista de strings
    com as frações transformadas em frações simples, números inteiros ou ERR quando houver erro como
    por exemplo divisão por zero.

    Parâmetro:
    elementos_fracoes: Lista de listas onde cada sublista tem 1 ou 2 elementos, 1 quando é um número
                       inteiro, 2 quando existe numerador e denominador
    """
    fracoes_simples = []

    for fracao in elementos_fracoes:
        if len(fracao) == 1:
            fracoes_simples.append(str(fracao[0]))
        elif len(fracao) == 2:
            if int(fracao[1]) == 0:
                fracoes_simples.append("ERR")
            else:
                numerador = int(fracao[0])
                denominador = int(fracao[1])

                parte_inteira = int(numerador/denominador)
                resto = numerador % denominador

                if resto == 0:
                    fracoes_simples.append(str(parte_inteira))
                else:
                    fracao_como_string = f"{parte_inteira} {resto}/{denominador}"
                    fracoes_simples.append(fracao_como_string)

    return fracoes_simples

# TODO: Remover antes da submissão do PR


def debugger_is_active() -> bool:
    """Return if the debugger is currently active

    # pylint: disable=line-too-long
    Source: https://stackoverflow.com/questions/38634988/check-if-program-runs-in-debug-mode/67065084
    """
    return hasattr(sys, 'gettrace') and sys.gettrace() is not None


if __name__ == "__main__":
    # TODO: Remover antes da submissão do PR
    if debugger_is_active():
        print(main.__doc__)
        print(obtem_fracoes_simples.__doc__)

    filtered_args = sys.argv[1:]
    main(filtered_args)
