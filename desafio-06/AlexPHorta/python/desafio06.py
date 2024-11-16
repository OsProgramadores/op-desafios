import itertools
import string


def find_matches(expression, words_file):
    candidates = shrink_search_field(expression, words_file)
    return candidates

def shrink_search_field(expression, words_file):
    # res = sieve_less_or_equal(expression, words_file)
    # res = sieve_starts_with(expression, res)
    # res = sieve_remaining(expression, res)
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
    e = quant_letters(expression)
    w = quant_letters(word)
    for k, v in w.items():
        if e.get(k) is not None and v > e[k]:
            return False
    return True

def quant_letters(a_word):
    keys = set(a_word)
    quanto = {k:0 for k in keys}
    for l in a_word:
        quanto[l] += 1
    return quanto

def sieve_remaining(expression, word):
    letters = set(expression)
    uppercase = set(string.ascii_uppercase)
    remaining = uppercase - letters
    return not any([(l in remaining) for l in word])

def sieve_starts_with(expression, word):
    letters = set(expression)
    return any([word.startswith(l) for l in letters])

def sieve_less_or_equal(expression, word):
    return len(expression) >= len(word)


if __name__ == "__main__":

    import io
    import unittest


    class TestFindMatches(unittest.TestCase):

        def test_return_with_vermelho(self):
            self.maxDiff = None
            with open('./words.txt') as file:
                self.assertCountEqual(find_matches("VERMELHO", file),
                    [["ELM", "HO", "REV"], ["ELM", "OH", "REV"],
                    ["OHM", "REVEL"], ["LEVER", "OHM"], ["ELM", "HOVER"],
                    ["HOLM", "VEER"], ["HELM", "OVER"], ["HELM", "ROVE"]])


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
