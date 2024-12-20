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
    print(grouped_by_len)
    valid_partitions = shrink_partitions(expression, grouped_by_len)
    print("Partitioned")
    print(valid_partitions)

    for v in valid_partitions:
        res.extend(find_in_partition(expression, v, grouped_by_len))
    print("Separated by partition")

    return res

def find_in_partition(expression, partition, grouped):
    letters_in_expression = quant_letters(expression)
    res = []
    iterator = [grouped[p] for p in partition]

    for prod in itertools.product(*iterator):
        letters_in_prod = quant_letters(''.join(prod))
        if letters_in_prod == letters_in_expression:
            prod = sorted(prod)
            if prod not in res:
                res.append(prod)

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


if __name__ == "__main__":

    import io
    import unittest

    VERMELHO_GROUPED = { 2: ['HE', 'HO', 'ME', 'OH', 'OR'],
                         3: ['EEL', 'ELM', 'EVE', 'HEE', 'HEM', 'HER', 'HOE', 'LEO',
                             'MOE', 'OHM', 'OLE', 'ORE', 'REV'],
                         4: ['HEEL', 'HELM', 'HERE', 'HERO', 'HOLE', 'HOLM', 'HOME',
                             'HOVE', 'LEER', 'LOME', 'LORE', 'LOVE', 'MERE', 'MOHR',
                             'MOLE', 'MORE', 'MOVE', 'OVER', 'REEL', 'ROLE', 'ROME',
                             'ROVE', 'VEER'],
                         5: ['ELMER', 'HOVEL', 'HOVER', 'LEVER', 'MERLE', 'MOREL', 'REVEL']}

    VERMELHA_GROUPED = {1: ['A'], 2: ['AH', 'AM', 'HA', 'HE', 'MA', 'ME'],
                        3: ['ALE', 'ARE', 'ARM', 'AVE', 'EAR', 'EEL', 'ELM',
                            'ERA', 'EVA', 'EVE', 'HAM', 'HEE', 'HEM', 'HER',
                            'LAM', 'MAR', 'RAE', 'RAH', 'RAM', 'REV'],
                        4: ['AHEM', 'AVER', 'EARL', 'EAVE', 'HALE', 'HARE',
                            'HARM', 'HAVE', 'HEAL', 'HEAR', 'HEEL', 'HELM',
                            'HERA', 'HERE', 'LAME', 'LEAR', 'LEER', 'MALE',
                            'MARE', 'MEAL', 'MERE', 'RAVE', 'REAL', 'REAM',
                            'REEL', 'RHEA', 'VALE', 'VEAL', 'VEER', 'VERA'],
                        5: ['ELMER', 'HALVE', 'HAREM', 'HEAVE', 'LEAVE', 'LEVER',
                            'MERLE', 'RAVEL', 'REALM', 'REAVE', 'REVEL', 'VELAR'],
                        6: ['HARLEM', 'MARVEL', 'REVEAL']}

    VERMELHO_GROUPED_NO_V_IN_3 = { 2: ['HE', 'HO', 'ME', 'OH', 'OR'],
                         3: ['EEL', 'ELM', 'HEE', 'HEM', 'HER', 'HOE', 'LEO',
                             'MOE', 'OHM', 'OLE', 'ORE'],
                         4: ['HEEL', 'HELM', 'HERE', 'HERO', 'HOLE', 'HOLM', 'HOME',
                             'HOVE', 'LEER', 'LOME', 'LORE', 'LOVE', 'MERE', 'MOHR',
                             'MOLE', 'MORE', 'MOVE', 'OVER', 'REEL', 'ROLE', 'ROME',
                             'ROVE', 'VEER'],
                         5: ['ELMER', 'HOVEL', 'HOVER', 'LEVER', 'MERLE', 'MOREL', 'REVEL']}


    class TestFindMatches(unittest.TestCase):

        def test_return_with_vermelho(self):
            self.maxDiff = None
            with open('./words.txt') as file:
                self.assertCountEqual(find_matches("VERMELHO", file),
                    [["ELM", "HO", "REV"], ["ELM", "OH", "REV"],
                    ["OHM", "REVEL"], ["LEVER", "OHM"], ["ELM", "HOVER"],
                    ["HOLM", "VEER"], ["HELM", "OVER"], ["HELM", "ROVE"]])

    class TestFindInPartition(unittest.TestCase):

        def test_find_in_partition(self):
            self.maxDiff = None
            self.assertEqual(find_in_partition("VERMELHO",
                                                [2, 2, 4],
                                                VERMELHO_GROUPED),
                             [])
            self.assertEqual(find_in_partition("VERMELHO",
                                                [2, 3, 3],
                                                VERMELHO_GROUPED),
                             [["ELM", "HO", "REV"], ["ELM", "OH", "REV"]])
    class TestGroupByLen(unittest.TestCase):

        def test_vermelho_group_len(self):
            self.maxDiff = None
            with open('./words.txt') as file:
                candidates = shrink_search_field("VERMELHO", file)
                self.assertEqual(group_by_len(candidates), VERMELHO_GROUPED)

    class TestNotSolo(unittest.TestCase):

        def test_vermelho(self):
            self.assertEqual(not_solo("VERMELHO", VERMELHO_GROUPED), [2])
            self.assertEqual(not_solo("VERMELHO", VERMELHO_GROUPED_NO_V_IN_3), [2, 3])

    class TestShrinkPartitions(unittest.TestCase):

        def test_vermelho(self):
            self.assertEqual(shrink_partitions("VERMELHO", VERMELHO_GROUPED),
                             [[2, 2, 4], [2, 3, 3], [3, 5], [4, 4]])
            self.assertEqual(shrink_partitions("VERMELHO", VERMELHO_GROUPED_NO_V_IN_3),
                             [[2, 2, 4], [3, 5], [4, 4]])
            self.assertEqual(shrink_partitions("VERMELHA", VERMELHA_GROUPED),
                             [[1, 2, 2, 3], [1, 2, 5], [1, 3, 4], [2, 2, 4],
                              [2, 3, 3], [2, 6], [3, 5], [4, 4]])

    class TestShrinkSearchField(unittest.TestCase):

        def test_return_with_single(self):
            with io.StringIO('A\nAB\nAC\nD\nDEF\nAFG\n') as file:
                self.assertEqual(shrink_search_field('A', file), ['A'])

        def test_return_with_two(self):
            with io.StringIO('A\nAB\nAC\nD\nDEF\nAFG\nCV\nCAF\nDC\nC') as file:
                self.assertCountEqual(shrink_search_field('AC', file), ['A', 'AC', 'C'])

        def test_return_with_many(self):
            self.maxDiff = None
            with open('./words.txt') as file:
                self.assertCountEqual(shrink_search_field("VERMELHO", file), ["ELM", "HELM", "HO",
                    "HOLM", "HOVER", "LEVER", "OH", "OHM", "OVER", "REV", "REVEL",
                    "ROVE", "VEER", "EEL", "ELMER", "EVE", "HE", "HEE", "HEEL",
                    "HEM", "HER", "HERE", "HERO", "HOE", "HOLE", "HOME", "HOVE",
                    "HOVEL", "LEER", "LEO", "LOME", "LORE", "LOVE", "ME", "MERE",
                    "MERLE", "MOE", "MOHR", "MOLE", "MORE", "MOREL", "MOVE",
                    "OLE", "OR", "ORE", "REEL", "ROLE", "ROME",])


    class TestSieveDuplicateLetters(unittest.TestCase):

        def test_sieve_number_of_letters(self):
            """If the word has more letters of the same type than what's in expression, it's not an anagram."""
            self.assertTrue(sieve_number_of_letters("AC", "A"))
            self.assertTrue(sieve_number_of_letters("AC", "C"))
            self.assertTrue(sieve_number_of_letters("AC", "CA"))
            self.assertTrue(sieve_number_of_letters("ACA", "A"))
            self.assertTrue(sieve_number_of_letters("ACA", "AA"))
            self.assertTrue(sieve_number_of_letters("ACA", "AC"))
            self.assertFalse(sieve_number_of_letters("AC", "AA"))
            self.assertFalse(sieve_number_of_letters("AC", "CC"))


    class TestSieveRemainingLetters(unittest.TestCase):
        """If the word contains any letters that aren't in expression, it's not an anagram."""

        def test_sieve_remaining(self):
            self.assertTrue(sieve_remaining("AC", "A"))
            self.assertTrue(sieve_remaining("AC", "AC"))
            self.assertTrue(sieve_remaining("AC", "C"))
            self.assertFalse(sieve_remaining("AC", "D"))
            self.assertFalse(sieve_remaining("AC", "AB"))
            self.assertFalse(sieve_remaining("AC", "DEF"))


    class TestSieveStartsWith(unittest.TestCase):
        """If the word starts with a letter that isn't in the expression, it's not an anagram."""

        def test_return_with_single(self):
            self.assertTrue(sieve_starts_with("A", "A"))
            self.assertTrue(sieve_starts_with("A", "AB"))
            self.assertTrue(sieve_starts_with("A", "AC"))
            self.assertTrue(sieve_starts_with("A", "AFG"))
            self.assertFalse(sieve_starts_with("A", "C"))
            self.assertFalse(sieve_starts_with("A", "CA"))
            self.assertFalse(sieve_starts_with("A", "CAA"))

        def test_return_with_two(self):
            self.assertTrue(sieve_starts_with("AD", "A"))
            self.assertTrue(sieve_starts_with("AD", "AB"))
            self.assertTrue(sieve_starts_with("AD", "AC"))
            self.assertTrue(sieve_starts_with("AD", "AFG"))
            self.assertTrue(sieve_starts_with("AD", "DEF"))
            self.assertFalse(sieve_starts_with("AD", "MEF"))

    class TestSieveLessOrEqual(unittest.TestCase):
        """If the word is longer than expression it's not an anagram."""

        def test_empty_return_empty(self):
            self.assertFalse(sieve_less_or_equal("", "A"))
            self.assertFalse(sieve_less_or_equal("", "AA"))

        def test_one_return_one(self):
            self.assertFalse(sieve_less_or_equal("A", "AA"))
            self.assertFalse(sieve_less_or_equal("A", "AAA"))
            self.assertTrue(sieve_less_or_equal("A", "A"))
            self.assertTrue(sieve_less_or_equal("A", "D"))

        def test_two_return_one_or_two(self):
            self.assertFalse(sieve_less_or_equal("AA", "AAA"))
            self.assertFalse(sieve_less_or_equal("AA", "DDD"))
            self.assertTrue(sieve_less_or_equal("AA", "AA"))
            self.assertTrue(sieve_less_or_equal("AA", "DD"))
            self.assertTrue(sieve_less_or_equal("AA", "A"))
            self.assertTrue(sieve_less_or_equal("AA", "D"))

    unittest.main()
