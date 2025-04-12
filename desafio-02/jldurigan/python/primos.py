i = 1
stringNumeros = ""

for i in range(1, 1000):
    j = 1
    primo = True
    
    while j <= i:
        if i != j and i % j == 0 and j != 1:
            primo = False
            break
        j += 1
        
    if primo:
        stringNumeros += str(i) + ", "

stringNumeros = stringNumeros.rstrip(", ")

print(stringNumeros)