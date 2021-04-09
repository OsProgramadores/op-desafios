""" Algoritmo para verificar números palindromicos em um intervalo. """

ver = 0
while ver == 0:
    intervalo = input("Digite o intervalo de inteiros a ser analisado: ").split()
    palind_lista = []
    palind = ""

    if len(intervalo) == 2:
        num_1 = int(intervalo[0])
        num_2 = int(intervalo[1])

        for i in range(num_1, num_2+1):
            palind = str(i)
            if int(palind[::-1]) == i:
                palind_lista.append(i)

        print(palind_lista)
        ver+=1

    else:
        print("Por favor, insira 2 números inteiros.")
