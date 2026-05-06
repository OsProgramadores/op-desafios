  inicio = int(input("Digite o número inicial: "))
  fim = int(input("Digite o número final: "))

  for x in range(inicio, fim + 1):
      numero = str(x)

      if numero == numero[::-1]:
          print(x)
