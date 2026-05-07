import sys


movimentos = [
    (2, 1),
    (1, 2),
    (-1, 2),
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, -1)
]

colunas = "abcdefgh"


def dentro_do_tabuleiro(x, y):
    return 0 <= x < 8 and 0 <= y < 8


def casa_para_posicao(casa):
    casa = casa.lower()

    if len(casa) != 2:
        return None

    coluna = casa[0]
    linha = casa[1]

    if coluna not in colunas:
        return None

    if linha not in "12345678":
        return None

    x = colunas.index(coluna)
    y = int(linha) - 1

    return x, y


def posicao_para_casa(x, y):
    return colunas[x] + str(y + 1)


def resolver(inicio_x, inicio_y):
    visitado = []
    caminho = []

    for i in range(8):
        linha = []
        for j in range(8):
            linha.append(False)
        visitado.append(linha)

    def grau(x, y):
        total = 0

        for dx, dy in movimentos:
            novo_x = x + dx
            novo_y = y + dy

            if dentro_do_tabuleiro(novo_x, novo_y):
                if not visitado[novo_y][novo_x]:
                    total = total + 1

        return total

    def buscar(x, y, passo):
        visitado[y][x] = True
        caminho.append((x, y))

        if passo == 64:
            return True

        proximas = []

        for dx, dy in movimentos:
            novo_x = x + dx
            novo_y = y + dy

            if dentro_do_tabuleiro(novo_x, novo_y):
                if not visitado[novo_y][novo_x]:
                    proximas.append((grau(novo_x, novo_y), novo_x, novo_y))

        proximas.sort()

        for item in proximas:
            novo_x = item[1]
            novo_y = item[2]

            if buscar(novo_x, novo_y, passo + 1):
                return True

        visitado[y][x] = False
        caminho.pop()

        return False

    if buscar(inicio_x, inicio_y, 1):
        return caminho

    return None


if len(sys.argv) != 2:
    print("ERR")
    sys.exit(1)

posicao_inicial = casa_para_posicao(sys.argv[1])

if posicao_inicial is None:
    print("ERR")
    sys.exit(1)

resultado = resolver(posicao_inicial[0], posicao_inicial[1])

if resultado is None:
    print("ERR")
else:
    for x, y in resultado:
        print(posicao_para_casa(x, y))