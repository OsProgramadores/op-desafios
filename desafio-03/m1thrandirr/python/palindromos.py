""" Algoritmo para verificar números palindromicos em um intervalo. """


while True:
    intervalo = input("Digite o intervalo de inteiros a ser analisado: ").split() # variavel que recebe o intervalo.
    palind_lista = [] # lista que armazena os palindromos dentro do intervalo.
    palind = "" # variavel que verifica se o número é um palindromo.

    if len(intervalo) == 2:
        num_1 = int(intervalo[0]) # variavel que recebe o começo do intervalo.
        num_2 = int(intervalo[1]) # variavel que recebe o fim do intervalo.

        for i in range(num_1, num_2+1): # loop que percorre o intervalo.
            palind = str(i)             # palind recebe o iterador em string.
            if int(palind[::-1]) == i:  # condição que compara se i é palindromo.
                palind_lista.append(i)  # adiciona i em palind_lista.

        print(palind_lista) # imprime todos os palindromos do intervalo.
        break

    else:
        print("Por favor, insira 2 números inteiros.")
