arq = open("d12.txt", 'r+')
cont = 0 
for n in arq.readlines():
    number = int(n)
    while (2 ** cont) < number :
        cont += 1

    if number == (2 ** cont):
        print(number, " true ", cont)
    else:
        print(number, " false ")
