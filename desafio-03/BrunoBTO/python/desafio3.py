
''' identificar numeros palindromos '''
print('Seja bem vindo ao identificador de numeros palindromicos\nInsira o MENOR valor:')
men = int(input())

print("insira o MAIOR valor")
mai = int(input())

palind = []


# Se os valores estiverem na ordem correta
if mai >= men:
    i = men
    while i <= mai:
        stri = str(i)
        inv = stri[::-1]
        if stri == inv:
            palind.append(i)
        i = i + 1
# Se os valores estiverem na ordem incorreta
elif mai < men:
    i = mai
    while i <= men:
        stri = str(i)
        inv = stri[::-1]
        if stri == inv:
            palind.append(i)
        i = i + 1

# Imprime a lista com os resultados
print(palind)
