import sys


def contar_letras(texto):
    contagem = [0] * 26

    for letra in texto:
        posicao = ord(letra) - ord("A")
        contagem[posicao] += 1

    return tuple(contagem)


def validar_expressao(texto):
    texto = texto.upper()
    resultado = ""

    for letra in texto:
        if letra == " ":
            continue

        if letra < "A" or letra > "Z":
            print("Erro: use apenas letras de A a Z e espaços.")
            sys.exit(1)

        resultado += letra

    if resultado == "":
        print("Erro: a expressão precisa ter pelo menos uma letra.")
        sys.exit(1)

    return resultado


def cabe(palavra_contagem, letras_restantes):
    for i in range(26):
        if palavra_contagem[i] > letras_restantes[i]:
            return False

    return True


def subtrair(letras_restantes, palavra_contagem):
    nova_contagem = []

    for i in range(26):
        nova_contagem.append(letras_restantes[i] - palavra_contagem[i])

    return tuple(nova_contagem)


def acabou(letras_restantes):
    for quantidade in letras_restantes:
        if quantidade != 0:
            return False

    return True


def primeira_letra_restante(letras_restantes):
    for i in range(26):
        if letras_restantes[i] > 0:
            return i

    return -1


def carregar_palavras(letras_da_expressao):
    palavras = []
    palavras_repetidas = set()

    with open("words.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavra = linha.strip().upper()

            if palavra == "":
                continue

            if palavra in palavras_repetidas:
                continue

            valida = True

            for letra in palavra:
                if letra < "A" or letra > "Z":
                    valida = False
                    break

            if not valida:
                continue

            contagem = contar_letras(palavra)

            if cabe(contagem, letras_da_expressao):
                palavras.append((palavra, contagem))
                palavras_repetidas.add(palavra)

    palavras.sort()
    return palavras


def procurar_anagramas(letras_restantes, palavras_por_letra, escolhidas, usadas, resultados):
    if acabou(letras_restantes):
        linha = tuple(sorted(escolhidas))
        resultados.add(linha)
        return

    letra_obrigatoria = primeira_letra_restante(letras_restantes)

    for palavra, contagem in palavras_por_letra[letra_obrigatoria]:
        if palavra in usadas:
            continue

        if cabe(contagem, letras_restantes):
            usadas.add(palavra)

            procurar_anagramas(
                subtrair(letras_restantes, contagem),
                palavras_por_letra,
                escolhidas + [palavra],
                usadas,
                resultados
            )

            usadas.remove(palavra)


if len(sys.argv) < 2:
    print('Uso: python anagrama.py "oi gente"')
    sys.exit(1)


expressao = " ".join(sys.argv[1:])
expressao = validar_expressao(expressao)

letras_da_expressao = contar_letras(expressao)

palavras = carregar_palavras(letras_da_expressao)

palavras_por_letra = [[] for _ in range(26)]

for palavra, contagem in palavras:
    for i in range(26):
        if contagem[i] > 0:
            palavras_por_letra[i].append((palavra, contagem))

resultados = set()

procurar_anagramas(
    letras_da_expressao,
    palavras_por_letra,
    [],
    set(),
    resultados
)

for linha in sorted(resultados):
    print(" ".join(linha))