strLimite = ""
i = 1

for i in range(i, 63):
    strLimite += "9"

# definindo numero maximo
limite = int(strLimite)

i = 1
strPalindromos = ""

for i in range(i, limite):
    strNum = str(i)
    tamanho = len(strNum)
    palindromo = False
    j = 0
    k = tamanho - 1
    prefixo = ""
    sufixo = ""

    while True:
        prefixo += strNum[j]
        sufixo += strNum[k]
        
        if j == k:
            if strNum[j] == strNum[k] and prefixo == sufixo[::-1]:
                palindromo = True
            break

        if j > tamanho / 2 and k < tamanho / 2:
            if prefixo == sufixo[::-1]:
                palindromo = True
            break
        
        j += 1
        k -= 1

    if palindromo:
        strPalindromos += strNum + ", "

strPalindromos = strPalindromos.rsplit(", ")

print(strPalindromos)
