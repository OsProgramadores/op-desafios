for i in range(1, (1 << 64) - 1):
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

        if j in(k, (tamanho / 2) -1):
            if prefixo == sufixo:
                palindromo = True
            break

        j += 1
        k -= 1

    if palindromo:
        print(i)
