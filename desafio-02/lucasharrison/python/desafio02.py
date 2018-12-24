numeros = range(10000)
for numero in numeros:
    div = 1
    count = 0
    while div <= numero:
        if numero%div == 0:
          count += 1
        if div >= numero:
          break
        div += 1
    if count >= 2:
        if count >= 3:
          pass
        else:
          print(numero)