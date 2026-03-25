def primo(num: int) -> bool:
    """
    Verifica se um número é primo.

    Esta função verifica se um número é primo ou não. Um número primo é aquele
    que só é divisível por 1 e por ele mesmo.

    Args:
        num (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Exemplos:
        >>> primo(5)
        True

        >>> primo(6)
        False
    """
    # Caso o número seja menor ou igual a 1, não é primo
    if num <= 1:
        return False

    # Pegando a raiz quadrada do número informado
    raiz = int(num ** 0.5)

    # Como um número primo é divisível apenas por 1 e por ele mesmo.
    # vamos começar o laço a partir de 2 e verificar se há algum divisor.
    # Se encontrarmos um divisor antes de chegar à raiz quadrada, o número não é primo.
    for divisor in range(2, raiz + 1):
        if num % divisor == 0:
            return False
    return True

for numero in range(2, 10001):
    if primo(numero):
        print(numero)
