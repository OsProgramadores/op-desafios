"""
Números palindrômicos.

Neste desafio, a idéia é imprimir todos os números palindrômicos entre
dois outros números. Tal como as palavras, os números palindrômicos mantém o
mesmo valor se lidos de trás para a frente.
Para o desafio, assuma:
    > Apenas inteiros positivos podem ser usados como limites.
    > Números de um algarismo são palíndromos por definição.
    > Máximo número: (1 << 64) - 1 (máximo unsigned int de 64 bits).
"""
def validar_condicao(n_1, n_2):
    """ Função que faz validação das condições impostas:
            - Apenas inteiros positivos podem ser usados como limites.
            - Segundo limite deve ser maior que o primeiro.
            - Máximo número: (1 << 64) - 1 (máximo unsigned int de 64 bits).

    Params:
        n_1: Primeiro número limite do intervalo.
        n_2: Segundo número limite do intervalo.

    Returns:
        bool: Verificando se as condições foram obedecidas.
        string: Mensagem de erro caso haver o mesmo, vazio por default.
    """
    msg = ""
    if n_1 < 0 or n_2 < 0:
        msg = "ERRO: Os números não podem ser negativos."
        return (False, msg)
    if n_2 < n_1:
        msg = "ERRO: O segundo número deve ser maior ou igual ao primeiro."
        return (False, msg)
    if n_1 > NUMERO_MAXIMO or n_2 > NUMERO_MAXIMO:
        msg = "ERRO: Valores ultrapassaram valor máximo de (2^64)-1"
        return (False, msg)
    return (True, msg)


def palidromo(num):
    """ Função que verifica se um número é palíndromo.

    Params:
        num: Número a ser verificado.

    Returns:
        Valor booleano verificando se é ou não palíndromo.
    """
    num = str(num)
    num_inverso = num[::-1]
    if num == num_inverso:
        return True
    return False


NUMERO_MAXIMO = 2**64 - 1

print("="*10, end=' ')
print('Vamos imprimir todos os valores palíndromos de um intervalo.', end=' ')
print("="*10)

num1 = int(input("Informe o valor do primeiro número do intervalo: "))
num2 = int(input("Informe o valor do segundo número do intervalo: "))

condicao, mensagem = validar_condicao(num1, num2)
if not condicao:
    print(f"\n{mensagem}")
else:
    for n in range(num1, num2+1):
        if palidromo(n):
            print(n)
    