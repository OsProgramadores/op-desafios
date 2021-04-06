"""
Desafio 8 - Adriano Roberto de Lima
"""

def mdc(numa, numb):
    """
    Calcula o Máximo Divisor Comum de forma recursiva
    """
    if numa == 0:
        return numb
    resto = numb % numa
    if resto == 0:
        return numa
    ret = mdc(resto, numa)
    return ret

def main():
    """
    Main Function
    """

    file = open("frac.txt", "r")
    linhas = file.readlines()

    for linha in linhas:
        fracao = linha.split("/")
        fracao = [int(x) for x in fracao]

        if len(fracao) == 1:
            parte1 = fracao[0]
            parte2 = 0
        else:
            if fracao[1] == 0:
                print("ERR")
                continue
            if fracao[1] == 1:
                parte1 = fracao[0]
                parte2 = 0
            else:
                parte1 = fracao[0] // fracao[1]
                parte2 = fracao[0] % fracao[1]
                parte3 = fracao[1]
                #Agora vamos usar o MDC para simplificar a fração parte2/parte3
                cmdc = mdc(parte2, parte3)
                parte2 = parte2 // cmdc
                parte3 = parte3 // cmdc

        if parte1 and parte2:
            print(parte1, " ", parte2, "/", parte3, sep="")
        elif parte1 and not parte2:
            print(parte1, sep="")
        elif not parte1 and parte2:
            print(parte2, "/", parte3, sep="")

if __name__ == "__main__":
    main()
