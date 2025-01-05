import collections
import functools
import itertools
import operator
import string


def anagrams(expression, words_file):
    expression = prep(expression)
    with open(words_file) as words:
        print("Searching...")
        anagrams = find_matches(expression, words)
        print("Found!")
        for anagram in anagrams:
            print(' '.join(anagram))

def prep(expression):
    if expression == "":
        return expression

    res = ""

    for c in expression:
        if c not in string.ascii_letters:
            continue
        res += c.upper()

    return res

def find_matches(expression, words_file):
    candidates = shrink_search_field(expression, words_file)
    print("Search field ok")
    res = []
    grouped_by_len = group_by_len(candidates)
    print("Everything grouped")
    valid_partitions = shrink_partitions(expression, grouped_by_len)
    print(f"Partitioned: {len(valid_partitions)} partitions")

    for v in valid_partitions:
        print(f"Partition {v}")
        res.extend(find_in_partition(expression, v, grouped_by_len))
    print("Separated by partition")

    return res

# def find_in_partition(expression, partition, grouped):
#     letters_in_expression = quant_letters(expression)
#     res = []
#     iterator = [grouped[p] for p in partition]
# 
#     for prod in itertools.product(*iterator):
#         letters_in_prod = quant_letters(''.join(prod))
#         if letters_in_prod == letters_in_expression:
#             prod = sorted(prod)
#             if prod not in res:
#                 res.append(prod)
# 
#     return res

def find_in_partition(expression, partition, grouped):
    letters_in_expression = quant_letters(expression)
    group_lengths = [range(len(grouped[p])) for p in partition]
    res = []
    counter = 0

    for g in itertools.product(*group_lengths):
        letters_in_prod = dict(letters_in_expression)
        words = []
        fits = True
        for i, j in enumerate(g):
            word = grouped[partition[i]][j]
            word_sum = quant_letters(word)
            for k, v in word_sum.items():
                letters_in_prod[k] -= v
                if letters_in_prod[k] < 0:
                    fits = False
                    break
            if not fits:
                break
            else:
                words.append(word)
        if not fits:
            continue
        else:
            res.append(words)

    return res

def group_by_len(candidates):
    """Group the words by length."""
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
    """Remove all partitions that need not be checked."""
    partitions = [p for p in accel_asc(len(expression))]
    available = list(grouped.keys())
    res = []

    # If a partition includes words whose length is not in one of the available partitions, don't include it.
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
    """Return length groups that don't include all the letters in expression."""
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
    """Shrink the search field for possible anagrams, before considering partitions of expression."""
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
    """Check if a word is contained in expression. Remove those that can't be."""
    e = quant_letters(expression)
    w = quant_letters(word)
    for k, v in w.items():
        if e.get(k) is not None and v > e[k]:
            return False
    return True

def quant_letters(a_word):
    """Return the number of the different letters in a word."""
    keys = set(a_word)
    quanto = {k:0 for k in keys}
    for l in a_word:
        quanto[l] += 1
    return quanto

def sieve_remaining(expression, word):
    """Remove any word that has letters that are not in expression."""
    letters = set(expression)
    uppercase = set(string.ascii_uppercase)
    remaining = uppercase - letters
    return not any([(l in remaining) for l in word])

def sieve_starts_with(expression, word):
    """Return only words that begin with one of the letters in expression."""
    letters = set(expression)
    return any([word.startswith(l) for l in letters])

def sieve_less_or_equal(expression, word):
    """Exclude words that are lengthier than expression."""
    return len(expression) >= len(word)


# Peguei de https://jeromekelleher.net/generating-integer-partitions.html
def accel_asc(n):
    """Yield all partitions of a given integer.

    E.g.: The partitions of three are: 1,1,1; 1,2; 2,1; 3
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

