import itertools

# Função para ler o arquivo de palavras
def carregar_palavras():
    with open("words.txt") as arquivo:
        palavras_unicas = arquivo.read().split()  # Lê todas as palavras e divide em uma lista
    return set(palavras_unicas)  # Retorna um conjunto de palavras únicas

# Função para encontrar anagramas
def encontrar_anagramas(expressao_usuario, palavras_disponiveis):
    expressao_usuario = expressao_usuario.upper()  # Converte tudo para maiúsculas
    expressao_usuario = "".join(letra for letra in expressao_usuario if letra.isalpha())  # Remove espaços e símbolos
    anagramas_encontrados = set()

    # Testa diferentes combinações de letras
    for tamanho in range(1, len(expressao_usuario) + 1):
        for combinacao in itertools.permutations(expressao_usuario, tamanho):
            palavra = "".join(combinacao)  # Junta as letras para formar palavras
            if palavra in palavras_disponiveis:  # Verifica se a palavra existe na lista
                anagramas_encontrados.add(palavra)

    return anagramas_encontrados

# Pede uma expressão ao usuário
expressao_usuario = input("Digite uma palavra ou frase: ")

# Carrega as palavras do arquivo
palavras_disponiveis = carregar_palavras()

# Encontra os anagramas
anagramas_encontrados = encontrar_anagramas(expressao_usuario, palavras_disponiveis)

# Exibe os anagramas encontrados
print("Anagramas encontrados:")
for anagrama in sorted(anagramas_encontrados):
    print(anagrama)
