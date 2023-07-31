#função onde irá verificar se a lista de numeros determinados no argumento da função são primos
def numsprimos(n):
#cria uma lista e define como verdadeira
    primos = [True] * (n + 1)
#define os números 0 e 1 como falso já que não são primos
    primos[0] = primos[1] = False

#utiliza o algorítimo "Crivo de Eratóstenes" para verificar números não primos
    for i in range(2, int(n**0.5) + 1):
        if primos[i]:
            for j in range(i * i, n + 1, i):
                primos[j] = False
#chama a lista de numeros restantes e imprime todos numeros primos
    for num in range(n + 1):
        if primos[num]:
            print(num ,"é um numero primo!")

#inicia a função com o valor de 10000 números conforme o desafio
numsprimos(10000)
