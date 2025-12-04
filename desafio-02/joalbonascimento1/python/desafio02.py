def numeroPrimo(num):
    divisoesPossiveis = 0

    for i in range(1,10000):
        if i > num:
            print(f'Parei em {i}')
            break
        if num % i == 0:
            divisoesPossiveis += 1
    if divisoesPossiveis > 2:
        print(f'{num} não é um número primo!')
        return
    print(f'{num} é um número primo!')
    return

numero = input("Digite um número: ")
numero = int(numero)
numeroPrimo(numero)
