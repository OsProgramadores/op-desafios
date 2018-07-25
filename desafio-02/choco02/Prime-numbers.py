#!/usr/bin/python
test = [2, 3, 5, 7]
prime = []

for a in range(2, 10000):
      if (a == 2) or (a == 3) or (a == 5) or (a == 7):
            prime.append(a)
      else:
            if (a % 2 == 0) or (a % 3 == 0) or (a % 5 == 0) or (a % 7 == 0):
                  continue
            else:
                  prime.append(a) #Numeros nao divisiveis por 2, 3, 5 e 7 serao add a um array prime para uma verificacao final
                  if (a <= 100): #Numeros primos anteriores a raiz do numero alvo serao add a um array de test para encontrar primos restantes
                        test.append(a)
print("Numeros adicionados em test \n")
print(test)
print("################################################")
print("\n")

for z in test:
      for x in prime:
            if (x % z == 0):
                  prime.remove(x)
#Nesse bloco todos os números nao divisiveis por 2, 3, 5 e 7 serao divididos por cada elemento no array test, se divisivel sera removido do array prime
print(test + prime)
	#by Choco02
	#Utilizado o Crivo de Eratostenes