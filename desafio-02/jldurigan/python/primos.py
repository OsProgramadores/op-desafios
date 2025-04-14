stringNumeros = ""

for i in range(1, 10000):
    primo = True
    j = 1

    while j <= i and primo:
        if i != j and i % j == 0 and j != 1:
            primo = False

        j += 1

    if primo:
        stringNumeros += str(i) + ", "

stringNumeros = stringNumeros.rstrip(", ")

print(stringNumeros)
