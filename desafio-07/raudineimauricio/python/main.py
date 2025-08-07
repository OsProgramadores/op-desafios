import os
import sys

def tac(nome_arquivo: str) -> None:
    """
    Função que simula o comando 'tac' (que imprime o conteúdo de um arquivo em ordem inversa).
    Lê o arquivo e escreve as linhas na saída padrão (terminal), da última linha para a primeira.
    """

    # Abre o arquivo no modo binário para garantir que não haja conversão de dados
    with open(nome_arquivo, 'rb') as arquivo:
        arquivo.seek(0, os.SEEK_END)
        posicao = arquivo.tell()

        # Armazena a "sobra" de dados que não foram processados.
        sobra = b''

        while posicao > 0:
            voltar = min(4096, posicao)

            #Decrementa a posição para ir voltando para ler do final para o início
            posicao -= voltar
            arquivo.seek(posicao)

            buffer = arquivo.read(voltar) + sobra
            linhas = buffer.splitlines(keepends=True)

            sobra = linhas.pop(0) if linhas else b''

            # Imprime as linhas na ordem reversa, já decodificando para UTF-8
            for linha in reversed(linhas):
                # Remover CR (se houver)
                linha = linha.replace(b'\r', b'')
                sys.stdout.buffer.write(linha)

        if sobra:
            # Remove qualquer 'Carriage Return' (CR) e escreve a última linha
            sobra = sobra.replace(b'\r', b'')
            sys.stdout.buffer.write(sobra)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Uso: python main.py [ARQUIVO]...")
        sys.exit()

    tac(sys.argv[1]) # Chama a função tac para processar o arquivo informado
