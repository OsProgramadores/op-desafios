#variaveis definindo um range de numeros
num_inicio = int(input("Digite um numero inicial: "))
num_final = int(input("digite o numero final: "))

for i in range (num_inicio, num_final):
    #converte o numero em string
    convert_string = str(i)
    #inverte o numero para poder comparar se é palindromo
    inverso = convert_string[::-1]
    #testa e imprime o numero caso seja palindromo
    if  convert_string == inverso:
        print (i ,"é um palíndromo")
