import itertools

# Função para ler o arquivo de palavras
def carregar_palavras():
    with open("words.txt") as arquivo:
        palavras_arquivo = arquivo.read().split()
    return set(palavras_arquivo)  # Retorna um conjunto de palavras únicas

# Função para encontrar anagramas
def encontrar_anagramas(expressao, palavras):
    expressao = expressao.upper()  # Converte tudo para maiúsculas
    expressao = "".join(letra for letra in expressao if letra.isalpha())
    anagramas_resultado = set()

    # Testa diferentes combinações de letras
    for tamanho in range(1, len(expressao) + 1):
        for combinacao in itertools.permutations(expressao, tamanho):
            palavra = "".join(combinacao)  # Junta as letras
            if palavra in palavras:
                anagramas_resultado.add(palavra)

    return anagramas_resultado

# Pede uma expressão ao usuário
entrada_usuario = input("Digite uma palavra ou frase: ")

# Carrega as palavras do arquivo
palavras_carregadas = carregar_palavras()

# Encontra os anagramas
anagramas_final = encontrar_anagramas(entrada_usuario, palavras_carregadas)

# Exibe os anagramas encontrados
print("Anagramas encontrados:")
for anagrama in sorted(anagramas_final):
    print(anagrama)
