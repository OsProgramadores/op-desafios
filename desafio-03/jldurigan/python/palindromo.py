for i in range(1, (1 << 64) - 1):
    strNum = str(i)
    tamanho = len(strNum)
    j = 0
    k = tamanho - 1
    prefixo = ""
    sufixo = ""

    while True:
        prefixo += strNum[j]
        sufixo += strNum[k]

        if prefixo != sufixo:
            break

        if j in(k, (tamanho / 2) -1):
            print(i)
            break

        j += 1
        k -= 1
