def is_palindrome(_start: int, _end: int) -> None:
    """
    Identifica e imprime todos os números palíndromos no intervalo de 'start' a 'end'.
    Um número palíndromo é um número que permanece o mesmo quando seus dígitos são invertidos.

    Parâmetros:
        _start (int): O valor inicial do intervalo.
        _end (int): O valor final do intervalo.

    Levanta:
        ValueError: Se 'start' ou 'end' for menor que 1, ou se ambos excederem o valor máximo
        para um inteiro sem sinal de 64 bits.
    """

    MAX_INT = (1 << 64) - 1

    if (_start > MAX_INT) or (_end > MAX_INT):
        print("Algum Limite > Máximo Inteiro Suportado")
        return

    # Trocar valores se start > end
    _start, _end = (_end, _start) if _start > _end else (_start, _end)

    for num in range(_start, _end + 1):
        if num < 10:
            print(num)
        else:
            inverse = int(str(num)[::-1])
            if inverse == num:
                print(num)


try:
    print("------- Números Palíndromes em um Intervalo ------\n" + '-' * 50)
    while True:
        MSG_INT_ERROR = 'Apenas números inteiros positivos!'

        start = input("Digite o valor inicial do intervalo: ")

        if not start.isdigit() or start == '0':
            print(MSG_INT_ERROR)
            continue

        end = input("Digite o valor final do intervalo: ")

        if not end.isdigit() or end == '0':
            print(MSG_INT_ERROR)
            continue

        break

    print('-'*50)
    is_palindrome(int(start), int(end))
    print('-'*50)

except KeyboardInterrupt:
    print("\nProcesso terminado pelo usuário.")

finally:
    print("Fim do Programa! :)")
