from collections import Counter
import re
import os

def validar_entrada(expressao):
    expressao = expressao.upper().replace(" ", "")
    if not re.match("^[A-Z]+$", expressao):
        raise ValueError("Use apenas letras de A-Z.")
    return expressao

def ler_palavras_validas(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        palavras = [linha.strip().upper() for linha in file if linha.strip().isalpha()]
    return palavras

def filtrar_palavras(palavras, expressao):
    letras_expressao = Counter(expressao)
    palavras_filtradas = []
    for palavra in palavras:
        letras_palavra = Counter(palavra)
        if all(letras_palavra[letra] <= letras_expressao.get(letra, 0)
               for letra in letras_palavra):
            palavras_filtradas.append(palavra)
    return palavras_filtradas

def gerar_anagramas(expressao, palavras, anagrama_atual=None, resultados=None):
    if anagrama_atual is None:
        anagrama_atual = []
    if resultados is None:
        resultados = set()
    if not expressao:
        resultados.add(" ".join(sorted(anagrama_atual)))
        return
    for palavra in palavras:
        letras_palavra = Counter(palavra)
        if all(letras_palavra[letra] <= Counter(expressao).get(letra, 0)
               for letra in letras_palavra):
            nova_expressao = subtrair_letras(expressao, palavra)
            gerar_anagramas(nova_expressao, palavras, anagrama_atual + [palavra], resultados)

def subtrair_letras(expressao, palavra):
    expressao_contador = Counter(expressao) - Counter(palavra)
    return ''.join([letra * expressao_contador[letra] for letra in expressao_contador])

def exibir_resultados(resultados):
    for anagrama in sorted(resultados):
        print(anagrama)

def main():
    expressao = input("Digite a expressão para gerar anagramas: ")
    try:
        expressao = validar_entrada(expressao)
    except ValueError as e:
        print(e)
        return

    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'words.txt')
    palavras = ler_palavras_validas(caminho_arquivo)

    palavras_filtradas = filtrar_palavras(palavras, expressao)

    resultados = set()
    gerar_anagramas(expressao, palavras_filtradas, [], resultados)

    if resultados:
        exibir_resultados(resultados)
    else:
        print("Nenhum anagrama encontrado para essa frase ou palavra.")

if __name__ == "__main__":
    main()
