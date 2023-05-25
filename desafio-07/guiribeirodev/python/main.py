"""
Main module

Lê o texto invertendo as linhas (igual o comando tac)

 autor: guiribeirodev

 versão: 1.0
"""
import sys


def python_tac(file_path):
    """Função principal tac

    Args:
        file_path (txt): recebe como argumento o arquivo a ser lido
    """
    with open(file_path, 'rb') as file:
        file.seek(0, 2)
        file_size = file.tell()

        block_size = 400000
        position = file_size - block_size

        while position >= 0:
            file.seek(position, 0)
            data = file.read(block_size)

            lines = data.splitlines()

            remainder_line = len(lines[0])
            lines = lines[1:]

            reversed_lines = reversed(lines)
            for line in reversed_lines:
                print(line.decode('utf8'))

            position -= block_size - remainder_line

        position2 = position + block_size
        file.seek(0)
        data = file.read(position2)

        lines = data.splitlines()

        reversed_lines = reversed(lines)
        for line in reversed_lines:
            print(line.decode('utf8'))


def main():
    """Função main, ponto de início  e de controle da execução do programa
    """
    file_path = sys.argv[1]

    python_tac(file_path)


main()
