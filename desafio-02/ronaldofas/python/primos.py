def verifica_se_eh_primo(numero: int) -> bool:
    quantidade_divisores: int = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            quantidade_divisores += 1

        if quantidade_divisores > 2 or numero == 1:
            return False

    return True


def imprime_primos(numeros: list[int]):
    linha: list[int] = []

    for i in numeros:
        linha.append(i)
        if len(linha) % 10 == 0:
            print(linha)
            linha = []

    if len(linha) > 0:
        print(linha)


def main():
    # Desafio - imprimir números primos entre 1 e 10.000
    numeros_primos: list[int] = []
    numero_inicial: int = 1
    numero_final: int = 10000

    for i in range(numero_inicial, numero_final + 1):
        if verifica_se_eh_primo(i):
            numeros_primos.append(i)

    print('=' * 23 + ' Números primos entre 1 e 10.000  ' + '=' * 23)
    imprime_primos(numeros_primos)
    print('=' * 31 + ' Fim da execução! ' + '=' * 31)


if __name__ == '__main__':
    main()
