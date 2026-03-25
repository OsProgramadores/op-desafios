"""
Testes unitários do Desafio 02
"""
import unittest
import random

from desafio_02 import verificar_numero_primo


class TestDesafio02(unittest.TestCase):
    """ Realização de testes unitários com o unittest. """

    def setUp(self):
        """ Configurações iniciais. """
        # Lista como os números primos no intervalo [1, 20]
        self.numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19]
        self._range = range(11)

    def test_funcao_verificar_numero_primo(self):
        """ Teste de validade da função verificar_numero_primo. """
        numero_primo_01 = random.choice(self.numeros_primos)
        numero_primo_02 = random.choice(self.numeros_primos)
        self.assertTrue(verificar_numero_primo(numero_primo_01))
        self.assertTrue(verificar_numero_primo(numero_primo_02))

    def test_funcao_verificar_numero_primo_falso(self):
        """ Teste de validade da função verificar_numero_primo.
            Entrada de número não primo.
        """
        numero1 = 10
        numero2 = 0
        numero3 = -5
        self.assertFalse(verificar_numero_primo(numero1))
        self.assertFalse(verificar_numero_primo(numero2))
        self.assertFalse(verificar_numero_primo(numero3))

    def test_verificar_numero_primo_intervalo(self):
        """ Teste de validade de um intervalo numérico aplicado à função
            verificar_numero_primo.
        """
        valores_esperados = [False, False, True, True, False, True,
                             False, True, False, False, False]
        valores_obtidos = [verificar_numero_primo(v) for v in self._range]
        self.assertListEqual(valores_esperados, valores_obtidos)


if __name__ == '__main__':
    unittest.main()
