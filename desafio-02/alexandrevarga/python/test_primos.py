from primos import encontrar_primos

def test_primos_intervalo_pequeno():
    assert encontrar_primos(1, 10) == [2, 3, 5, 7]
