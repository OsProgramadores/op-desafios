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

    if _start < 1 or _end < 1:
        print("Os limites devem ser números inteiros positivos.")
        return

    # Limites maiores que o máximo suportado
    if _start > MAX_INT and _end > MAX_INT:
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
    print("---- Números Palíndromes sobre um Intervalo ----")
    start = int(input("Digite o valor inicial do intervalo: "))
    end = int(input("Digite o valor final do intervalo: "))
    is_palindrome(start, end)
except ValueError:
    print("Por favor, digite apenas números inteiros!")
except KeyboardInterrupt:
    print("\nProcesso terminado pelo usuário.")
finally:
    print("Fim do Programa! :)")
