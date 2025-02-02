import sys
import itertools
from collections import Counter

def is_valid_expression(expression):
    """
    Verifica se a expressão contém apenas letras de A a Z e espaços.

    Args:
        expression (str): A string que representa a expressão a ser verificada.

    Returns:
        bool: True se a expressão for válida, False caso contrário.
    """
    for char in expression:
        if not ('A' <= char <= 'Z' or char == ' '):
            return False
    return True

def get_letter_counts(expression):
    """
    Conta a ocorrência de cada letra na expressão (convertendo para maiúsculas).

    Args:
        expression (str): A string que representa a expressão.

    Returns:
        dict: Um dicionário onde as chaves são as letras (maiúsculas) e os
              valores são suas contagens.
    """
    counts = {}
    for char in expression:
        if 'A' <= char <= 'Z':
            counts[char] = counts.get(char, 0) + 1
    return counts

def find_anagrams(expressao_parametro, lista_de_palavras_parametro):
    """
    Encontra e imprime todos os anagramas possíveis da expressão,
    usando palavras da lista fornecida.

    Args:
        expressao_parametro (str): A string que representa a expressão.
        lista_de_palavras_parametro (list): Uma lista de strings representando
                                          as palavras válidas.
    """
    expressao_parametro = expressao_parametro.upper().replace(" ", "")
    if not is_valid_expression(expressao_parametro):
        print("Erro: Expressão contém caracteres inválidos.", file=sys.stderr)
        return

    letter_counts = get_letter_counts(expressao_parametro)
    # Tamanho máximo das palavras (ajuste conforme necessário)
    max_word_length = 16

    valid_words = {}
    for word in lista_de_palavras_parametro:
        if len(word) <= max_word_length:
            word_counts = Counter(get_letter_counts(word))
            if all(word_counts.get(char, 0) <= letter_counts.get(char, 0) for char in word_counts):
                valid_words[word] = word_counts

    anagrams = set()
    for i in range(1, len(letter_counts) + 1):
        for combination in itertools.combinations(valid_words, i):
            total_length = sum(len(word) for word in combination)
            if total_length > len(expressao_parametro):
                continue

            combo_counts = sum((Counter(word) for word in combination), Counter())
            if combo_counts == letter_counts:
                sorted_combo = tuple(sorted(combination))
                anagrams.add(sorted_combo)

    for anagram in sorted(anagrams):
        print(*anagram)

# Verifica se o script está sendo executado diretamente (e não importado como um módulo).
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python anagrama.py <expressão>", file=sys.stderr)
        sys.exit(1)

    expressao_principal = sys.argv[1]
    #Abre o arquivo words.txt para leitura.
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            lista_de_palavras_principal = [line.strip() for line in f]
    except FileNotFoundError:
        print("Erro: Arquivo words.txt não encontrado.", file=sys.stderr)
        sys.exit(1)

    find_anagrams(expressao_principal, lista_de_palavras_principal)
