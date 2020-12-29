listNumber = []
inicio = int(input("Numero Inicial: "))
fim = int(input("Numero Final: "))
print("\n\n")
if inicio > fim:
    for x in range(fim,inicio+1):
        listNumber.append(x)
elif fim > inicio:
    for x in range(inicio,fim+1):
        listNumber.append(x)
for x in listNumber:
    REVERSE = str(x)[::-1]
    if str(x) == REVERSE:
        print(x,end=" ")
