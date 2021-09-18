""" Módulo para testes. """
import unittest

from desafio_03 import validar_condicao, palindromo


class TestDesafio03(unittest.TestCase):
    """ Testes dp desafio 03. """

    def setUp(self):
        """ Configuração incial. """
        self.valor_maximo = 2**64 - 1

    def test_validar_condicao_sucesso(self):
        """ Testa a função validar_condição com os parâmetros corretos. """
        num1 = 5
        num2 = 7
        self.assertTrue(validar_condicao(num1, num2, self.valor_maximo)[0])

    def test_validar_condicao_somente_um_numero_positivo(self):
        """ Testa a função validar_condição com somente um
            parâmetro positivo.
        """
        num1 = -10
        num2 = 10
        msg_error = "ERRO: Os números não podem ser não positivos."
        condicao, msg = validar_condicao(num1, num2, self.valor_maximo)
        self.assertFalse(condicao)
        self.assertEqual(msg, msg_error)

    def test_validar_condicao_entrada_valor_zero(self):
        """ Testa a função validar_condição com um tendo valor zero. """
        num1 = 0
        num2 = 5
        msg_error = "ERRO: Os números não podem ser não positivos."
        condicao, msg = validar_condicao(num1, num2, self.valor_maximo)
        self.assertFalse(condicao)
        self.assertEqual(msg, msg_error)

    def test_validar_condicao_segundo_limite_menor_primeiro(self):
        """ Testa função validar_condicao com o segundo limite menor que
            o primeiro.
        """
        num1 = 11
        num2 = 3
        msg_error = "ERRO: O segundo limite deve ser maior que o primeiro."
        condicao, msg = validar_condicao(num1, num2, self.valor_maximo)
        self.assertFalse(condicao)
        self.assertEqual(msg, msg_error)

    def test_validar_condicao_segundo_limite_igual_primeiro(self):
        """ Testa função validar_condicao com os dois limites iguais. """
        num1 = 11
        num2 = 11
        msg_error = "ERRO: O segundo limite deve ser maior que o primeiro."
        condicao, msg = validar_condicao(num1, num2, self.valor_maximo)
        self.assertFalse(condicao)
        self.assertEqual(msg, msg_error)

    def test_validar_condicao_numero_maior_limite(self):
        """ Testa função validar_condicao com um parâmetro maior que
            o valor limite.
        """
        num1 = 2
        num2 = 2**64
        msg_error = "ERRO: Valores ultrapassaram valor máximo de (2^64)-1"
        condicao, msg = validar_condicao(num1, num2, self.valor_maximo)
        self.assertFalse(condicao)
        self.assertEqual(msg, msg_error)

    def test_validar_condicao_entrada_string(self):
        """ Testa função validar_condicao com uma entrada do tipo string. """
        num1 = 2
        num2 = 'a'
        with self.assertRaises(TypeError):
            validar_condicao(num1, num2, self.valor_maximo)

    def test_palindromo_verdadeiro(self):
        """ Testa função palindromo com valor palíndromo como entrada. """
        num = 2112
        self.assertTrue(palindromo(num))

    def test_palindromo_falso(self):
        """ Testa função palindromo com valor não palíndromo como entrada. """
        num = 211
        self.assertFalse(palindromo(num))

    def test_palindromo_range(self):
        """ Testa comportamento da função palindromo com uma lista de valores
            inteiros como entrada.
        """
        _range = range(6, 26)
        saida_esperada = [True, True, True, True, False,
                          True, False, False, False, False,
                          False, False, False, False, False,
                          False, True, False, False, False]
        saida = [palindromo(v) for v in _range]
        self.assertListEqual(saida, saida_esperada)

    def test_palindromo_entrada_string(self):
        """ Testa função palindromo com uma entrada do tipo string. """
        entrada = 'a'
        with self.assertRaises(ValueError):
            palindromo(entrada)

if __name__ == '__main__':
    unittest.main()
