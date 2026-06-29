import sys
from collections import Counter

PALAVRAS = "words.txt"


def normaliza_expressao(expressao):
    """Tira espaços e deixa todos os caracteres da expressão maiúsculos"""
    letras = []
    for letra in expressao:
        if letra != " ":
            letras.append(letra.upper())
    return letras


def cabe(palavra, letras_disponiveis):
    """Diz se dá pra montar a palavra com as letras disponíveis"""
    letras_palavra = Counter(palavra)
    for letra in letras_palavra:
        if letras_palavra[letra] > letras_disponiveis[letra]:
            return False
    return True


def guarda_candidatas(letras):
    """Só guarda as palavras que dá pra montar com as letras da expressão"""
    letras_disponiveis = Counter(letras)
    candidatas = []

    arquivo = open(PALAVRAS)

    for linha in arquivo:
        palavra = linha.strip()
        if cabe(palavra, letras_disponiveis):
            candidatas.append(palavra)
    return candidatas


def busca_anagramas(candidatas, letras_disponiveis, pivo, combinacao_atual, anagramas):
    """Percorre as candidatas e, para cada uma que cabe nas letras disponíveis, adiciona à
    combinação atual. Quando não sobrar letra nenhuma, a combinação forma um anagrama
    """
    if sum(letras_disponiveis.values()) == 0:
        # ordena as palavras dentro da linha pra não depender do arquivo estar em ordem alfabética
        anagramas.append(" ".join(sorted(combinacao_atual)))
        return

    for i in range(pivo, len(candidatas)):
        palavra = candidatas[i]
        if cabe(palavra, letras_disponiveis):
            combinacao_atual.append(palavra)
            busca_anagramas(
                candidatas,
                letras_disponiveis - Counter(palavra),
                i + 1,
                combinacao_atual,
                anagramas,
            )
            combinacao_atual.pop()


def main():
    expressao = sys.argv[1]
    letras = normaliza_expressao(expressao)
    print("buscando anagramas de:", expressao)

    candidatas = guarda_candidatas(letras)
    anagramas = []
    busca_anagramas(candidatas, Counter(letras), 0, [], anagramas)

    if len(anagramas) > 0:
        for anagrama in anagramas:
            print(anagrama)
    else:
        print("nenhum anagrama encontrado")


if __name__ == "__main__":
    main()
