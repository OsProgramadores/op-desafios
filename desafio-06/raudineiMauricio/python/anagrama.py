import sys
from collections import Counter

def expressao_valida(expression):
    """
    Verifica se a expressão contém apenas letras maiúsculas e espaços.
    Args:
        expressao: A string a ser validada.
    Returns:
        True se a expressão for válida, False caso contrário.
    """
    return all(char.isupper() or char.isspace() for char in expression)

def contagens_de_letras(expression):
    """
    Conta a ocorrência de cada letra na expressão, ignorando espaços.
    Args:
        expression (str): A string de entrada.
    Returns:
        Counter: Um dicionário com a contagem de cada letra.
    """
    return Counter(char for char in expression)

def todas_letras_iguais(expression):
    """
    Verifica se todas as letras na expressão são iguais.
    Args:
        expression (str): A string de entrada.
    Returns:
        bool: True se todas as letras forem iguais, False caso contrário.
    """
    return len(set(expression.replace(" ", ""))) == 1

def encontrar_anagramas(expressao_parametro, palavras_validas,
                         parcial=None, contagem_restante=None, resultados=None):
    """
    Encontra e imprime os anagramas possíveis da expressão dada uma lista de palavras.
    Args:
        expressao_parametro (str): A string original.
        palavras_validas (dict): Um dicionário de palavras válidas e suas contagens de letras.
        parcial (list, optional): Lista acumulada das palavras em formação.
        contagem_restante (Counter, optional): Contagem das letras que ainda precisam ser usadas.
        resultados (set, optional): Conjunto para evitar repetições de anagramas.
    """
    if contagem_restante is None:
        contagem_restante = contagens_de_letras(expressao_parametro)

    if parcial is None:
        parcial = []

    if resultados is None:
        resultados = set()

    # Se não há mais letras para combinar, imprime o anagrama encontrado
    if not contagem_restante:
        anagrama = " ".join(sorted(parcial))
        if anagrama not in resultados:
            print(anagrama)
            resultados.add(anagrama)
        return
    #Se todas as letras forem iguais.
    if todas_letras_iguais(expressao_parametro):
        letra = expressao_parametro[0]
        if letra in palavras_validas and letra not in resultados:
            print(letra)
            resultados.add(letra)
            return

    # Percorre as palavras válidas e verifica se podem ser usadas na combinação
    for palavra, contagem_palavra in palavras_validas.items():
        if all(contagem_palavra[char] <= contagem_restante.get(char, 0)
            for char in contagem_palavra):
            nova_contagem = contagem_restante.copy()
            # Reduz a contagem das letras da palavra usada

            for char in list(nova_contagem):
                nova_contagem[char] -= contagem_palavra[char]
                if nova_contagem[char] == 0:
                    del nova_contagem[char]
            # Chamada recursiva com a nova contagem e palavra adicionada
            encontrar_anagramas(expressao_parametro, palavras_validas,
            parcial + [palavra], nova_contagem, resultados)

def possiveis_anagramas(expressao_parametro, lista_de_palavras_parametro):
    """
    Filtra as palavras possíveis e inicia a busca por anagramas.
    Args:
        expressao_parametro (str): A string original.
        lista_de_palavras_parametro (list): Lista de palavras disponíveis.
    """
    expressao_parametro = expressao_parametro.upper().replace(" ", "")
    if not expressao_valida(expressao_parametro):
        print("Erro: Expressão contém caracteres inválidos.", file=sys.stderr)
        return

    cont_letras = contagens_de_letras(expressao_parametro)
    tamanho_expressao = len(expressao_parametro)
    # Filtra palavras que podem ser usadas nos anagramas
    palavras_validas = {
        word: contagens_de_letras(word)
        for word in set(lista_de_palavras_parametro)
        if len(word) <= tamanho_expressao and all(char in cont_letras for char in word)
    }
    # Inicia a busca por anagramas
    encontrar_anagramas(expressao_parametro, palavras_validas)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python anagrama.py <expressão>", file=sys.stderr)
        sys.exit(1)

    expressao_principal = sys.argv[1]
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            lista_de_palavras_principal = [line.strip() for line in f if line.strip().isalpha()]
    except FileNotFoundError:
        print("Erro: Arquivo words.txt não encontrado.", file=sys.stderr)
        sys.exit(1)

    possiveis_anagramas(expressao_principal, lista_de_palavras_principal)
