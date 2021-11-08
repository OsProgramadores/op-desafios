'Solução desafio 7'
import sys

def main():
    'função principal do arquivo'
    with open(sys.argv[1],'r', encoding='utf-8') as file:
        file = file.readlines()
    file.reverse()
    file_reversed = ''
    file[-1] = file[-1][:-1]
    for linha in file:
        file_reversed += linha
    print(file_reversed)

if __name__ == "__main__":
    main()
