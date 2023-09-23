"""
    @Author: Thiago Felix.
    Propósito: Resolução do desafio-2.
"""
def primo(num:int) -> bool:
    """
    Validador de numeros Primos.

    Função conta a quantidade de divisores um numero X possui,
    se o numero possuir apenas 2 divisores é considerado primoa.

    Args:
        num (int): recebe um numero inteiro.

    Returns:
        tipo_de_retorno: retorna falso calso o numero de divisores ultrapasse 2.

    Exemplos:
        >>> primo(5)
        True

        >>> primo(6)
        False
    """
    # Corpo da função aqui
    numDivisores = int(0)
    for apoio in range(1, num+1):
        if numDivisores > 2:
            return False
        if num % apoio == 0:
            numDivisores += 1
    if numDivisores > 2:
        return False
    return True

for numero in range(2,10001):
    if primo(numero):
        print(numero)
