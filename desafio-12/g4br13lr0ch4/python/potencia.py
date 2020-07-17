"""
    Resolução do Desafio 04,
    Por: Gabriel Rocha,
    Github: github.com/g4br13lr0ch4
"""
doc = []
with open('d12.txt') as file_object:
    for line in file_object:
        doc.append(int(line))

def verifica(valor):
    """Verifica se o valor é uma potência de 2"""
    aux = 1
    x = 0
    while x >= 0:
        if aux > valor:
            return "FALSE", ""
        if aux == valor:
            return "TRUE", str(x)
        aux *= 2
        x += 1

for item in doc:
    status, p = verifica(item)
    print(str(item) + " " + status + " " + p)
