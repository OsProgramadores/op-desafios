try:
    # Variáveis definindo um range de números
    num_inicio = int(input("Digite um número inicial: "))
    num_final = int(input("Digite o número final: "))
    if num_inicio >= num_final:
        print ("O número inicial deve ser menor que o final.")

    elif num_inicio < 0 or num_final < 0:
        print("Os números precisam ser maior que 0.")
    else:

        for i in range(num_inicio, num_final +1 ):
            # Converte o número em string
            convert_string = str(i)
            # Inverte o número para poder comparar se é palíndromo
            inverso = convert_string[::-1]
            # Testa e imprime o número caso seja palíndromo
            if convert_string == inverso:
                print(i, "é um palíndromo")
except ValueError:
    print("Por favor, insira somente números válidos.")
