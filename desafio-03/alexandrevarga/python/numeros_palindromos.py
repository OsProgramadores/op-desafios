"""Módulo para identificar números palíndromos em um intervalo.

Fornece funções para verificar se um número é palíndromo e para listar todos os
palíndromos em um intervalo especificado.
"""

def eh_palindromo(numero):
    """Verifica se um número é palíndromo comparando com sua inversão."""
    s = str(numero)
    return s == s[::-1]

def palindromos_entre(inicio, fim):
    """Retorna uma lista de palíndromos no intervalo [inicio, fim]."""
    return [
        num for num in range(inicio, fim + 1)
        if eh_palindromo(num)
    ]

def solicitar_numero(mensagem, tipo='inicial', minimo=None):
    """Solicita um número ao usuário e realiza validações."""
    entrada = input(mensagem)
    if entrada.lower() == 'q':
        print("Encerrando o programa.")
        return None
    try:
        valor = int(entrada)
        if tipo == 'final' and minimo is not None and valor < minimo:
            print("Erro: O número final tem que ser maior ou igual ao número inicial.")
            return None
        if valor == 0:
            if tipo == 'final':
                print("Erro: O número final tem que ser maior ou igual ao número inicial.")
            else:
                print(f"Erro: O número {tipo} tem que ser maior que zero.")
            return None
        if valor < 0:
            print(f"Erro: O número {tipo} não pode ser negativo.")
            return None
        return valor
    except ValueError:
        print(
            "Entradas inválidas. Certifique-se de que ambos são positivos e final >= inicial."
        )
        return None

def main():
    """Executa o programa principal."""
    inicio = solicitar_numero("Digite o número inicial (ou 'q' para sair): ", tipo='inicial')
    if inicio is None:
        return
    fim = solicitar_numero(
        "Digite o número final (ou 'q' para sair): ",
        tipo='final',
        minimo=inicio
    )
    if fim is None:
        return
    resultado = palindromos_entre(inicio, fim)
    print("Números palíndromos no intervalo:")
    for num in resultado:
        print(num)

if __name__ == "__main__":
    main()
