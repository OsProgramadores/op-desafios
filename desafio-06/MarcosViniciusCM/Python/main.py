import sys

def contar_letras(texto):
    contagem = {}
    for letra in texto:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem

def pode_formar_palavra(contagem_palavra, contagem_disponivel):
    for letra, qtd in contagem_palavra.items():
        if contagem_disponivel.get(letra, 0) < qtd:
            return False
    return True

def main():
    if len(sys.argv) < 2:
        print("Erro: Você precisa passar a palavra ou frase como argumento.")
        sys.exit(1)

    expressao = sys.argv[1].upper().replace(" ", "")

    for caractere in expressao:
        if not 'A' <= caractere <= 'Z':
            print(f"Erro: Caractere inválido encontrado -> '{caractere}'")
            sys.exit(1)

    letras_disponiveis = contar_letras(expressao)
    total_letras = len(expressao)

    try:
        with open("words.txt", "r") as arquivo:
            todas_palavras = [linha.strip().upper() for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        print("Erro: Arquivo 'words.txt' não encontrado na mesma pasta.")
        sys.exit(1)

    palavras_uteis = []
    for palavra in todas_palavras:
        contagem_p = contar_letras(palavra)
        if pode_formar_palavra(contagem_p, letras_disponiveis):
            palavras_uteis.append((palavra, contagem_p))

    resultados = set()

    def buscar_anagramas(index_inicio, letras_restantes, tamanho_atual, anagrama_atual):
        if tamanho_atual == total_letras:
            linha_ordenada = " ".join(sorted(anagrama_atual))
            if linha_ordenada not in resultados:
                resultados.add(linha_ordenada)
                print(linha_ordenada)
            return

        for i in range(index_inicio, len(palavras_uteis)):
            palavra, contagem_p = palavras_uteis[i]

            if pode_formar_palavra(contagem_p, letras_restantes):
                novas_letras = letras_restantes.copy()
                for letra, qtd in contagem_p.items():
                    novas_letras[letra] -= qtd
                anagrama_atual.append(palavra)
                buscar_anagramas(i, novas_letras, tamanho_atual + len(palavra), anagrama_atual)
                anagrama_atual.pop()

    buscar_anagramas(0, letras_disponiveis, 0, [])

if __name__ == "__main__":
    main()
