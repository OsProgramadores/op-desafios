import functools
import io
import operator
import unittest

from desafio06 import (find_in_partition,
                       find_matches,
                       group_by_len,
                       not_solo,
                       prep,
                       sieve_less_or_equal,
                       sieve_starts_with,
                       sieve_number_of_letters,
                       sieve_remaining,
                       shrink_partitions,
                       shrink_search_field,
                       WORDS)


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

    def test_return_with_no_anagrams(self):
        with open(WORDS) as file:
            resp = functools.reduce(operator.iconcat, list(find_matches("X", file)), [])
            self.assertEqual(resp, [])

    def test_return_with_vermelho(self):
        self.maxDiff = None
        with open(WORDS) as file:
            resp = functools.reduce(operator.iconcat, list(find_matches("VERMELHO", file)), [])
            self.assertCountEqual(resp,
                [["ELM", "HO", "REV"], ["ELM", "OH", "REV"],
                ["OHM", "REVEL"], ["LEVER", "OHM"], ["ELM", "HOVER"],
                ["HOLM", "VEER"], ["HELM", "OVER"], ["HELM", "ROVE"]])

    def test_return_with_goa(self):
        self.maxDiff = None
        with open(WORDS) as file:
            resp = functools.reduce(operator.iconcat, list(find_matches("GOA", file)), [])
            self.assertCountEqual(resp,
                [["A", "GO"], ["AGO"], ["GOA"]])

    def test_return_with_aaa(self):
        self.maxDiff = None
        with open(WORDS) as file:
            resp = functools.reduce(operator.iconcat, list(find_matches("AAA", file)), [])
            self.assertCountEqual(resp,
                [["A"]])

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
        self.assertEqual(find_in_partition("GOA",
                                            [1, 2],
                                            {1: ["A"], 2: ["GO"], 3: ["AGO", "GOA"]}),
                         [["A", "GO"]])


class TestGroupByLen(unittest.TestCase):

    def test_goa_group_len(self):
        self.maxDiff = None
        with open(WORDS) as file:
            candidates = shrink_search_field("GOA", file)
            self.assertEqual(group_by_len(candidates), {1: ["A"], 2: ["GO"], 3: ["AGO", "GOA"]})

    def test_vermelho_group_len(self):
        self.maxDiff = None
        with open(WORDS) as file:
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
        with open(WORDS) as file:
            self.assertCountEqual(shrink_search_field("VERMELHO", file), ["ELM", "HELM", "HO",
                "HOLM", "HOVER", "LEVER", "OH", "OHM", "OVER", "REV", "REVEL",
                "ROVE", "VEER", "EEL", "ELMER", "EVE", "HE", "HEE", "HEEL",
                "HEM", "HER", "HERE", "HERO", "HOE", "HOLE", "HOME", "HOVE",
                "HOVEL", "LEER", "LEO", "LOME", "LORE", "LOVE", "ME", "MERE",
                "MERLE", "MOE", "MOHR", "MOLE", "MORE", "MOREL", "MOVE",
                "OLE", "OR", "ORE", "REEL", "ROLE", "ROME",])

    def test_return_with_goa(self):
        self.maxDiff = None
        with open(WORDS) as file:
            self.assertCountEqual(shrink_search_field("GOA", file), ["A", "GO", "AGO", "GOA"])

class TestSieveDuplicateLetters(unittest.TestCase):

    def test_sieve_number_of_letters(self):
        """If the word has more letters of the same type than what's in
        expression, it's not an anagram."""
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


class TestPrep(unittest.TestCase):
    """If expression is not only uppercase characters, convert it."""

    def test_prep_empty_string(self):
        with self.assertRaises(TypeError):
            prep("")

    def test_prep(self):
        self.assertEqual(prep("a"), "A")
        self.assertEqual(prep("A"), "A")
        self.assertEqual(prep("vermelho"), "VERMELHO")
        self.assertEqual(prep("VERMELHO"), "VERMELHO")
        self.assertEqual(prep("oi gente"), "OIGENTE")
        self.assertRaises(SystemExit, prep, "VERMELHO!")
        self.assertRaises(SystemExit, prep, "123456")

if __name__ == "__main__":

    unittest.main(verbosity=3)
