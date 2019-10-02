arq = open("d12.txt", 'r')
for n in arq.readlines():
    number = int(n)
    cont = 0
    while (2 ** cont) < number:
        cont += 1
    if number == (2 ** cont):
        print(number, " true ", cont)
    else:
        print(number, " false ")
