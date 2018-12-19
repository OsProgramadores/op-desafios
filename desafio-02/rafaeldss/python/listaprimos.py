def primo(numero):
    if numero == 2:
        print(numero)
    elif numero < 2:
	pass
    else:
	for num in range(2, numero):
	    if numero % num == 0:
		break
	else:
	    print(numero)


for x in range(10000):
    primo(x)
