import itertools

# Função para ler o arquivo de palavras
def carregar_palavras():
    with open("words.txt") as arquivo:
        palavras = arquivo.read().split()  # Lê todas as palavras e divide em uma lista
    return set(palavras)  # Retorna um conjunto de palavras únicas

# Função para encontrar anagramas
def encontrar_anagramas(expressao, palavras):
    expressao = expressao.upper()  # Converte tudo para maiúsculas
    expressao = "".join(letra for letra in expressao if letra.isalpha())  # Remove espaços e símbolos
    anagramas = set()
    
    # Testa diferentes combinações de letras
    for tamanho in range(1, len(expressao) + 1):
        for combinacao in itertools.permutations(expressao, tamanho):
            palavra = "".join(combinacao)  # Junta as letras para formar palavras
            if palavra in palavras:  # Verifica se a palavra existe na lista
                anagramas.add(palavra)
    
    return anagramas

# Pede uma expressão ao usuário
expressao = input("Digite uma palavra ou frase: ")

# Carrega as palavras do arquivo
palavras = carregar_palavras()

# Encontra os anagramas
anagramas = encontrar_anagramas(expressao, palavras)

# Exibe os anagramas encontrados
print("Anagramas encontrados:")
for anagrama in sorted(anagramas):
    print(anagrama)
