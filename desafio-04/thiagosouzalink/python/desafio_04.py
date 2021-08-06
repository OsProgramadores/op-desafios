"""
Contabilizar Peças de Xadrez.

Neste desafio, você deverá contabilizar e exibir a quantidade de cada peça em
um tabuleiro de xadrez sem usar estruturas condicionais ou de múltipla
escolha (sem *if*s, else, switch case ou operadores ternários).
"""
def calcular_quantidade_pecas(dict_pecas_codigo, tabuleiro):
    """ Função para calcular quantidade de peças de xadrez no tabuleiro.

    Params:
        dict_pecas_codigo: Dicionário contendo o código númerico de cada peça.
        tabuleiro: Matriz contendo código númerico correspondente as peças em
        suas respectivas casas.

    Returns:
        Dicionário informando a quantidade de cada peça presente no tabuleiro.
    """
    pecas_quantidade = {}
    for peca, codigo in dict_pecas_codigo.items():
        soma = 0
        for linha in tabuleiro:
            soma += linha.count(codigo)
        pecas_quantidade[peca] = soma
    return pecas_quantidade


def imprimir_quantidade_pecas(dict_pecas_quantidade):
    """ Função para imprimir a quantidade de cada peça presente no tabuleiro.

    Params:
        dict_pecas_quantidade: Dicionário contendo a quantidade de cada peça
        presente no tabuleiro verificado.
    """
    print(f"Peão: {dict_pecas_quantidade['peao']} peças(s)")
    print(f"Bispo: {dict_pecas_quantidade['bispo']} peças(s)")
    print(f"Cavalo: {dict_pecas_quantidade['cavalo']} peças(s)")
    print(f"Torre: {dict_pecas_quantidade['torre']} peças(s)")
    print(f"Rainha: {dict_pecas_quantidade['rainha']} peças(s)")
    print(f"Rei: {dict_pecas_quantidade['rei']} peças(s)")


def imprimir_tabuleiro(tabuleiro):
    """ Função para imprimir tabuleiro.

    Params:
        tabuleiro: Tabuleiro que será imprimido.
    """
    for linha in tabuleiro:
        print()
        for casa in linha:
            print(casa, end=' ')
    print("\n")


def imprimir_resultado(dict_pecas_codigo, tabuleiro, num_id):
    """ Função para imprimir resultado do desafio do xadrez.

    Params:
        dict_pecas_codigo: Dicionário contendo o código númerico de cada peça.
        tabuleiro: Matriz contendo código númerico correspondente as peças em
        suas respectivas casas.
        n: Identificação do tabuleiro.
    """
    id_tabuleiro = f" Tabuleiro 0{num_id} "
    quantidade_pecas = calcular_quantidade_pecas(dict_pecas_codigo, tabuleiro)
    print(f"\n\n{id_tabuleiro.center(30, '#')}")
    imprimir_tabuleiro(tabuleiro)
    imprimir_quantidade_pecas(quantidade_pecas)
    print(f"\n{'#'*30}")


# Main
CODIGO_PECAS = {'peao': 1, 'bispo':2, 'cavalo': 3,
                'torre': 4, 'rainha': 5, 'rei': 6,
                'vazio': 0}

TABULEIRO_01 = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

TABULEIRO_02 = [[4, 3, 2, 5, 6, 2, 3, 4],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [4, 3, 2, 5, 6, 2, 3, 4]]

imprimir_resultado(CODIGO_PECAS, TABULEIRO_01, 1)
imprimir_resultado(CODIGO_PECAS, TABULEIRO_02, 2)
