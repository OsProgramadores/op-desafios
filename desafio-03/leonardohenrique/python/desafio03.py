#variaveis definindo um range de numeros
numinicio = 100
numfinal = 999

for i in range (numinicio, numfinal):
    #converte o numero em string
    convstrg = str(i)
    #inverte o numero para poder comparar se é palindromo
    inverso = convstrg[::-1]
    #testa e imprime o numero caso seja palindromo
    if  convstrg == inverso:
        print (i ,"é um palíndromo")
