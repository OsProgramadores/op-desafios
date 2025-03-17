num01 = int(input('Digite o primeiro valor: '))
num02 = int(input('Digite o segundo valor: '))
palindromos = []

for i in range(num01, num02 + 1):
    if str(i) == str(i)[::-1]: 
        palindromos.append(str(i))

if palindromos:
    print(f'Os números palíndromos entre {num01} e {num02} são: {" ".join(palindromos)}')
else:
    print(f'Não há números palíndromos entre {num01} e {num02}.')