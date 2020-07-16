aux = 2

while aux < 1000:
    cont = 0
    for x in range(aux):
        if aux%(x+1) == 0:
            cont+=1
    if cont == 2:
        print(aux)
    aux += 1