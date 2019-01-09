numero1 = 1
numero2 = 20

for i in range(numero1, numero2+1):
    if str(i) == (''.join(reversed(str(i)))):
        print(i, 'eh palidronomo')
