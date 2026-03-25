MAX_INTEGER = 18446744073709551615

def print_palindromes(begin, end, print_output=True):
    """Imprime todos os palíndromos encontrados entre begin e end, inclusive.

    Argumentos:
    - begin - Str
    - end - Str
    - print_output - Boolean
    """
    if not begin.isdigit() and end.isdigit():
        raise ValueError("Argumentos devem ser números inteiros")
    begin = int(begin)
    end = int(end)
    positive = (begin >=0 and end >=0)\
                or "Argumentos devem ser números positivos"
    less_than_max = (begin <= MAX_INTEGER and end <= MAX_INTEGER)\
                or "Argumento excede MAX_INTEGER"
    begin_less_than_end = (begin < end)\
                or "Os argumentos devem ser fornecidos em ordem crescente"

    err = first_true(
        (positive, less_than_max, begin_less_than_end),
        predicate=lambda x: isinstance(x, str))

    if err:
        raise ValueError(f"{err}")

    palindromes = []

    for n in range(begin, end+1):
        if is_palindrome(n):
            palindromes.append(n)
        else:
            pass

    if print_output:
        for p in palindromes:
            print(p)

    return palindromes


def is_palindrome(candidate):
    """Retorna True se o argumento é um palíndromo, False se não for.

    Argumento:
    - candidate - Str
    """
    candidate = str(candidate)
    palindrome = False

    if len(candidate) < 2:
        palindrome = True
    else:
        if candidate[0] == candidate[-1]:
            palindrome = is_palindrome(candidate[1:-1])

    return palindrome

# Peguei de https://docs.python.org/3.8/library/itertools.html
def first_true(iterable, default=False, predicate=None):
    """Returns the first true value or the *default* if there is no true value."""
    # first_true([a,b,c], x) → a or b or c or x
    # first_true([a,b], x, f) → a if f(a) else b if f(b) else x
    return next(filter(predicate, iterable), default)


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
        description="Lista todos os números palíndromos existentes entre dois extremos."
    )

    parser.add_argument(
        "extremos",
        nargs="*",
        help="Os números inicial e final para a busca."
    )

    parser.add_argument(
        '-n',
        '--noprint',
        dest="noprint",
        action='store_false',
        help="Somente retorna os resultados."
    )

    parser.add_argument(
        "-t",
        "--test",
        dest="test",
        action="store_true",
        help="Executa os testes."
    )

    args = parser.parse_args()

    if len(args.extremos) == 0 and not args.test:
        parser.print_help()

    if args.extremos:
        try:
            assert len(args.extremos) == 2, "Número excessivo de argumentos."
            print_palindromes(*args.extremos, print_output=args.noprint)
        except Exception as exc:
            raise ValueError(f"{exc}") from exc

    if args.test:

        import builtins
        import contextlib
        import io
        import unittest

        from unittest.mock import Mock

        class TestPrintPalindromes(unittest.TestCase):

            def test_limits_are_positive_integers(self):
                self.assertRaises(ValueError, print_palindromes, "-1", "-10")

            def test_limits_are_ints(self):
                self.assertRaises(ValueError, print_palindromes, "1.5", "10")
                self.assertRaises(ValueError, print_palindromes, "1", "10.5")

            def test_begin_must_be_lower_than_end(self):
                self.assertRaises(ValueError, print_palindromes, "10", "1")

            def test_begin_and_end_must_be_lower_than_max_integer(self):
                self.assertRaises(ValueError, print_palindromes,
                    str(MAX_INTEGER+1), str(MAX_INTEGER+2))
                self.assertRaises(ValueError, print_palindromes, "0", str(MAX_INTEGER+1))

            def test_include_limits(self):
                self.assertEqual(print_palindromes("0", "1", print_output=False),
                    [0, 1])
                self.assertEqual(print_palindromes("0", "9", print_output=False),
                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                self.assertEqual(print_palindromes("9", "11", print_output=False),
                    [9, 11])
                self.assertEqual(print_palindromes("1", "20", print_output=False),
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
                self.assertEqual(print_palindromes("3000", "3010", print_output=False),
                    [3003])
                self.assertEqual(print_palindromes("101", "121", print_output=False),
                    [101, 111, 121])
                self.assertEqual(print_palindromes("101", "121", print_output=False),
                    [101, 111, 121])

            # Roubei de https://stackoverflow.com/a/62360735
            def test_really_print_palindromes(self):
                mock = Mock()
                mock.side_effect = print  # ensure actual print is called to capture its txt
                print_original = print
                builtins.print = mock

                try:
                    str_io = io.StringIO()
                    with contextlib.redirect_stdout(str_io):
                        print_palindromes("5", "11", print_output=True)
                    output = str_io.getvalue()

                    self.assertTrue(print.called)  # `called` is a Mock attribute
                    self.assertEqual(output, "5\n6\n7\n8\n9\n11\n")
                finally:
                    builtins.print = print_original  # ensure print is "unmocked"


        class TestPalindromes(unittest.TestCase):

            def test_single_digit_always_palindrome(self):
                self.assertTrue(is_palindrome("0"))
                self.assertTrue(is_palindrome("5"))
                self.assertTrue(is_palindrome("9"))

            def test_two_digits(self):
                self.assertTrue(is_palindrome("99"))
                self.assertFalse(is_palindrome("19"))

            def test_more_than_two_digits(self):
                self.assertTrue(is_palindrome("101"))
                self.assertTrue(is_palindrome("1001"))
                self.assertTrue(is_palindrome("3003"))
                self.assertTrue(is_palindrome("18446744066044764481"))
                self.assertFalse(is_palindrome(1.5))
                self.assertFalse(is_palindrome([0]))
                self.assertFalse(is_palindrome("119"))
                self.assertFalse(is_palindrome("1191"))
                self.assertFalse(is_palindrome("5025"))
                self.assertFalse(is_palindrome(MAX_INTEGER))

        unittest.main(argv=[sys.argv[0]])
