# list to store the input number
listNumber = []

# inicial number
inicio = int(input("Numero Inicial: "))

# finally number
fim = int(input("Numero Final: "))
print("\n\n")

# verifying if the start is great than the end number

if inicio > fim:
	for x in range(fim,inicio+1):
		listNumber.append(x)
elif fim > inicio:
	for x in range(inicio,fim+1):
		listNumber.append(x)

for x in listNumber:
	reverse = str(x)[::-1]
	if str(x) == reverse:
		print(x,end=" ")

	


