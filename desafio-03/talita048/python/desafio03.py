print("\nBem-vindo(a) ao detector de números palíndromos!")
print("Um número palíndromo é aquele que permanece igual quando lido de trás para frente.")
print("Insira dois números e vou te informar todos os palíndromos que existem entre eles :D")

limite_a = int(input("Digite o primeiro número: "))
limite_b = int(input("Digite o segundo número: "))

lista_pal = []

while limite_a < limite_b+1 :
    reverso = int(str(limite_a)[::-1])
    if limite_a == reverso :
        lista_pal.append(limite_a)
    limite_a += 1

print("Números palíndromos encontrados:")
for palindromo in lista_pal:
    print(palindromo)
