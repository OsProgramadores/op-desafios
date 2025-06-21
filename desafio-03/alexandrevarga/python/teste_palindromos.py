"""Testes automatizados para o módulo numeros_palindromos.

Utiliza pytest para validar as funções de identificação de números palíndromos.
"""

import numeros_palindromos

def test_eh_palindromo():
    """Testa a função eh_palindromo com diferentes casos."""
    assert numeros_palindromos.eh_palindromo(121) is True
    assert numeros_palindromos.eh_palindromo(123) is False
    assert numeros_palindromos.eh_palindromo(1) is True
    assert numeros_palindromos.eh_palindromo(22) is True
    assert numeros_palindromos.eh_palindromo(10) is False

def test_palindromos_entre():
    """Testa a função palindromos_entre para diferentes intervalos."""
    assert numeros_palindromos.palindromos_entre(10, 22) == [11, 22]
    assert numeros_palindromos.palindromos_entre(100, 105) == [101]
    assert numeros_palindromos.palindromos_entre(1, 9) == [1,2,3,4,5,6,7,8,9]
