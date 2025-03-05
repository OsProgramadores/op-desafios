""" algoritmo
1. receber os dois números.
2. criar um for que vai do início até o fim dos números.
3. transformar tudo em string com uma variavel auxiliar
4. verificar se as duas são iguais, se for dar print, se não, segue
"""

# recebe os dois numeros
a = input("digite o primeiro numero ");
b = input("digite o segundo numero ");
c = "";
a = int(a)
b = int(b)

# loop de verificação
for x in range(a, b+1):
    c = str(x)
    d = str(x)
    d = d[::-1]
    if d == c:
        print(c);
    else:
        d = ""
        c = "";
