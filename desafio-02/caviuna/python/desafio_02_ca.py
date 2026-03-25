''' 02 - Primos name '''

def lista(num):
    ''' List number in range 1 to 10000 '''
    numeros = []
    for i in range(1, num+1):
        div = 0
        for j in range(1, i+1):
            if i%j == 0:
                div += 1
        if  div == 2:
            numeros.append(i)
    return print(numeros)
lista(10000)
