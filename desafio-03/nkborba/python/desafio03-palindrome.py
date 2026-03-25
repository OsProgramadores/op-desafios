# Desafio 03 - OsProgramadores
# Nicholas Borba

import time

def numberToList(n):
    lista = [int(numStr) for numStr in str(n)]
    return lista

def invertList(l):
    length = len(l) #To get the length of the list to be able to do a for properly over the list positions
    pos = length-1  #Length should gave us the total number, but we know lists starts at 0, so let's decrease this number by 1

    #We don't need to iterate over all list because we'll move 2 itens each loop
    #then we can divide this by 2 and convert to INT for round porpuses
    #if we have an odd number of elements the middle will always keep the same

    cont = int(length/2)

    for x in range(cont):
        aux = l[x]
        l[x] = l[pos]
        l[pos] = aux
        pos -= 1
    return l

def findPalindrome(start, end):
    finalList = []
    start_time = time.time()

    for num in range(start, end+1):
        lista = numberToList(num)
        #A new list must be created, if we just
        toCompare = invertList(numberToList(num))

        #A new list must be created to avoid any changes on our comparisson list who will be inverted
        pos = len(lista)-1

        if pos <= 0:
            finalList.append(num)
            #print(num) #Uncomment it if you want to print line by line (slower then now)
        else:
            if toCompare == lista:
                finalList.append(num)
                #print(num) #Uncomment it if you want to print line by line (slower then now)

    #If you've uncommented the two prints above remove finalList on return
    return print(finalList, "\n--- Time spent to run: %s seconds ---" % (time.time() - start_time))

start = input("Digite o primeiro numero do intervalo: ")
end = input("Digite o segundo numero do intervalo: ")

findPalindrome(int(start), int(end))
