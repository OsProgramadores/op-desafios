import sys
limite_max = (1 << 64) - 1 # Essa linha define o limite_max como o maior inteiro positivo
#que pode ser armazenado em 64 bits,
#o que é útil para garantir que os números de entrada não ultrapassem esse limite.

#PEDIMOS AO USUÁRIO QUE DIGITE O INTERVALO DE NÚMEROS.
num_inicial = int(input("Digite o número inicial: "))
num_final = int(input("Digite o número final: "))

#AQUI ESTAMOS VENDO SE O NÚMERO É NEGATIVO, SE FOR NÃO DEIXA PROSSEGUIR E DA ERRO.
if num_inicial < 0 or num_final < 0:
    print("Erro: Os números devem ser positivos.")
    sys.exit()

#CASO O NÚMEMO INCIIAL FOR MENOR QUE O FINAL, NÃO TEM COMO VERIFICAR SE É PALINDROM E DA ERRO.
if num_inicial > num_final:
    print("Erro: O número inicial deve ser menor ou igual ao número final.")
    sys.exit()

#BLOCO PARA CONTROLAR O LIMITE DE INTERVALO DE NÚMEROS.
if num_inicial > limite_max or num_final > limite_max:
    print(f"Erro: Os números não podem exceder {limite_max}.")
    sys.exit() #ENCERRA O PROGRAMA APÓS O ERRO, CASO ACONTEÇA.

#PERCORRENDO TODOS OS NÚEROS NO INTERVALO, INICIO E FINAL.
for i in range(num_inicial, num_final +1):
    palindromo = 0 #ARMAZENAMOS O VALOR DO PALÍNDROMO
    temp = i #GERA UMA CÓPIA DO NÚMERO ATUAL PARA SER MANIPULADO.

    #ENQUANTO A COPIA FOR MAIOR QUE 0, VAI BUSCANDO OS NÚMEROS
    while temp > 0:
        palindromo = palindromo * 10 + temp % 10
        temp = temp // 10 #FAZ A REMOÇÃO DO ULTIMO DIGITO DA CÓPIA (TEMP)

    #SE O NÚMERO ORIGINAL FOR IGUAL AO PALÍNDROMO GERADO, O PROGRAMA EXIBE O RESULTADO
    if i == palindromo:
        print(i)
