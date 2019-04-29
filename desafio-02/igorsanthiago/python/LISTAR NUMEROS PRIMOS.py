
def is_prime(numeros):
    div = 2
    if numeros == 2:
        return True
    while numeros % div != 0 and div <= numeros/2:
        div += 1
    if numeros % div == 0:
        return False
    return True

def main():
    start = 2
    stop = 10000
    while start < stop:
        if is_prime(start):
            print(start, end=', ')
        start += 1

if __name__ == "__main__":
    main()


numerosmanual = int(input('. Caso queira saber manualmente escreva um número:'))
tot = 0
for c in range(1, numerosmanual + 1):
    if numerosmanual % c == 0:
        print('\033[32m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} é dividido somente {} vez'.format(numerosmanual, tot))
if tot == 2:
    print('Isso torna ele um número primo!')
else:
    print('E por isso ele não se torna um numero primo!')
