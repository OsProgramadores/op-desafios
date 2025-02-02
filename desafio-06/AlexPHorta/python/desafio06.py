import functools
import itertools
import operator
import string
import sys


WORDS = 'words.txt'


def print_anagrams(expression, words_file):
    """Print all anagrams from expression, found in words_file.

    Positional arguments
    expression -- The expression to be analysed
    words_file -- The path to the file with words
    """
    _expression = prep(expression)
    with open(words_file) as words:
        _anagrams = list(m for m in find_matches(_expression, words))
        if len(_anagrams) == 1 and len(_anagrams[0]) == 0:
            print(f"Nenhum anagrama encontrado para a expressão: {expression}")
        for anagram in _anagrams:
            for a in anagram:
                print(' '.join(a))

def prep(expression):
    """Prepare expression to be analysed.

    Positional arguments
    expression -- The expression to be analysed
    """
    if expression == "":
        return expression

    _expression = expression
    res = ""

    for c in string.whitespace:
        _expression = _expression.replace(c, '')

    for c in _expression:
        if c not in string.ascii_letters:
            sys.exit("A expressão deve conter somente caracteres alfabéticos. "
                  "Números, pontuação e outros caracteres não são permitidos. Abortando.")
        res += c.upper()

    return res

def find_matches(expression, words_file):
    """Find the anagrams for expression in the file.

    Positional arguments
    expression -- The expression to be analysed
    words_file -- The path to the file with words
    """
    candidates = shrink_search_field(expression, words_file)
    res = []
    grouped_by_len = group_by_len(candidates)
    valid_partitions = shrink_partitions(expression, grouped_by_len)

    for v in valid_partitions:
        res.extend(find_in_partition(expression, v, grouped_by_len))

    yield res

def find_in_partition(expression, partition, grouped):
    """Search possible matches in each partition group.

    Positional arguments
    expression -- The expression to be analysed
    partition -- One partition of the number of letters in expression
    grouped -- All possible anagrams grouped by length
    """
    letters_in_expression = quant_letters(expression)
    group_lengths = [range(len(grouped[p])) for p in partition]

    group_letters = {}
    for k, v in grouped.items():
        letters = [quant_letters(w) for w in v]
        group_letters.update({k:letters})

    res = []

    for g in itertools.product(*group_lengths):
        letters_in_prod = dict(letters_in_expression)
        words = []
        fits = True
        selected_words = sorted([grouped[partition[i]][j] for i, j in enumerate(g)])
        if selected_words in words:
            continue
        for i, j in enumerate(g):
            word = grouped[partition[i]][j]
            word_sum = group_letters[partition[i]][j]
            for k, v in word_sum.items():
                letters_in_prod[k] -= v
                if letters_in_prod[k] < 0:
                    fits = False
                    break
            if not fits:
                break
            words.append(word)
        if not fits:
            continue
        words = sorted(words)
        if words not in res:
            res.append(words)

    return res

def group_by_len(candidates):
    """Group the words by length.

    Positional arguments
    candidates -- The single word anagrams found in the file
    """
    candidates = sorted(candidates, key=len)
    res = {}
    grouped = []
    for _, g in itertools.groupby(candidates, len):
        grouped.append(list(g))
    lengths = [len(l[0]) for l in grouped]
    for l, g in zip(lengths, grouped):
        res[l] = g
    return res

def shrink_partitions(expression, grouped):
    """Remove all partitions that dont't need to be checked.

    Positional arguments
    expression -- The expression to be analysed
    grouped -- All possible anagrams grouped by length
    """
    partitions = list(accel_asc(len(expression)))
    available = list(grouped.keys())
    res = []

    # If a partition includes words whose length is not in one of the available
    # partitions, don't include it.
    for partition in partitions:
        for e in partition:
            if e not in available:
                break
        else:
            res.append(partition)

    rem = []
    no_solo = not_solo(expression, grouped)

    for r in res:
        if set(r) <= set(no_solo):
            rem.append(r)

    # If there's a group 1, remove all partitions that have more ones than the length of group 1.
    ones = 1 in available
    if ones:
        gg = grouped.get('1')
        len_ones = len(gg) if gg is not None else 1
        for r in res:
            if r.count(1) > len_ones:
                rem.append(r)

    for r in rem:
        try:
            remover = res.index(r)
            del res[remover]
        except ValueError:
            continue

    return res

def not_solo(expression, grouped):
    """Return length groups that don't include all the letters in expression.

    Positional arguments
    expression -- The expression to be analysed
    grouped -- All possible anagrams grouped by length
    """
    in_expression = set(expression)
    res = []
    for k, g in grouped.items():
        g = [list(i) for i in g]
        available = set(functools.reduce(operator.iconcat, g, []))
        remaining = in_expression - available
        if len(remaining) > 0:
            res.append(k)
    return res

def shrink_search_field(expression, words_file):
    """Shrink the search field for possible anagrams, before considering
    partitions of expression.

    Positional arguments
    expression -- The expression to be analysed
    words_file -- The path to the file with words
    """
    res = []
    for w in words_file:
        w = w.strip()
        le = sieve_less_or_equal(expression, w)
        sw = sieve_starts_with(expression, w)
        rm = sieve_remaining(expression, w)
        ql = sieve_number_of_letters(expression, w)
        if all((le, sw, rm, ql)):
            res.append(w)
    return res

def sieve_number_of_letters(expression, word):
    """Check if a word is contained in expression. Remove those that can't be.

    Positional arguments
    expression -- The expression to be analysed
    word -- The word to be checked against expression
    """
    expression_quant = quant_letters(expression)
    word_quant = quant_letters(word)
    for k, v in word_quant.items():
        if expression_quant.get(k) is not None and v > expression_quant[k]:
            return False
    return True

def quant_letters(a_word):
    """Return a mapping of the number of the different letters in a word.

    Positional arguments
    a_word -- The word to be mapped
    """
    keys = set(a_word)
    quanto = {k:a_word.count(k) for k in keys}
    return quanto

def sieve_remaining(expression, word):
    """Remove any word that has letters that are not in expression.

    Positional arguments
    expression -- The expression to be analysed
    word -- The word to be checked against expression
    """
    letters = set(expression)
    uppercase = set(string.ascii_uppercase)
    remaining = uppercase - letters
    return not any((l in remaining) for l in word)

def sieve_starts_with(expression, word):
    """Return only words that begin with one of the letters in expression.

    Positional arguments
    expression -- The expression to be analysed
    word -- The word to be checked against expression
    """
    letters = set(expression)
    return any(word.startswith(l) for l in letters)

def sieve_less_or_equal(expression, word):
    """Exclude words that are lengthier than expression.

    Positional arguments
    expression -- The expression to be analysed
    word -- The word to be checked against expression
    """
    return len(expression) >= len(word)


# Peguei de https://jeromekelleher.net/generating-integer-partitions.html
def accel_asc(n):
    """Yield all partitions of a given integer.
    E.g.: The partitions of three are: 1,1,1; 1,2; 2,1; 3

    Positional arguments
    n -- The integer to be partitioned
    """
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


if __name__ == "__main__":

    import gettext
    import sys

    def translate(text):
        text = text.replace("usage", "modo de usar")
        text = text.replace("positional arguments", "argumentos posicionais")
        text = text.replace("show this help message and exit",
                            "Exibe esta mensagem de ajuda e termina a execução.")
        text = text.replace("error", "erro")
        text = text.replace("options", "opções")
        text = text.replace("the following arguments are required",
                            "os seguintes argumentos são obrigatórios")
        return text
    gettext.gettext = translate

    import argparse

    parser = argparse.ArgumentParser(
        description="Imprime todos os anagramas de TERMO encontrados no\
        arquivo 'words.txt' (Que deve estar na mesma pasta do programa.)."
    )

    parser.add_argument(
        "termo",
        nargs = 1,
        help="O termo a ser usado para a busca de anagramas."
    )

    args = parser.parse_args()

    if len(args.termo) == 0:
        parser.print_help()

    if args.termo:
        try:
            assert len(args.termo) == 1, "Número excessivo de argumentos."
            print_anagrams(sys.argv[1], WORDS)
        except Exception as exc:
            raise ValueError(f"{exc}") from exc

