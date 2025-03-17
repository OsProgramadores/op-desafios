numero = 2
primos = []

while numero <= 10000:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):  
        if numero % i == 0:
            primo = False
            break
    if primo:
        primos.append(str(numero))  # Adiciona o número primo como string na lista
    numero += 1

# Exibe todos os primos em uma linha, separados por espaço
print(f'Os números primos de 1 a 10.000 são: {" ".join(primos)}')
