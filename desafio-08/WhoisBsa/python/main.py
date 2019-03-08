
""" Desafio 08 - Frações Simples """


def baixoInteiro(b, i):
    """ mdc entre o divisor e o inteiro """

    if b == 0:  #se b igual a zero retorna apenas o inteiro
        return i
    resto = i % b  #resto da divisao entre o inteiro pelo divisor
    if resto == 0:  #se o resto for igual a zero significa que o inteiro
        return b    #é divisivel por b
    resultado = baixoInteiro(resto, b)  #recursivamente o resultado irá pegar o
    return resultado           #maior divisor comum entre os dois

def main():
    """ main """
    file = open("frac.txt", "r")
    linhas = file.readlines()

    for l in linhas:
        fracao = l.split("/")  #separa a fração por '/'
        fracao = [int(n) for n in fracao]  #separar os n numeros na fraçao

        if len(fracao) == 1:  #se o tamanho da fracao for 1 entao fica apenas
            cima = fracao[0]  #o dividendo
            baixo = 0
        else:
            if fracao[1] == 0:  #se o divisor for 0 printa erro
                print("ERR")
                continue
            if fracao[1] == 1:  #se o divisor for 1 mostra apenas o dividendo
                cima = fracao[0]
                baixo = 0
            if fracao[0] != 0 and fracao[1] == 0:
                cima = fracao[0]
                baixo = 0
            else:  #se nao ocorrer nenhum dos casos acima segue a funcao normal
                cima = fracao[0] // fracao[1]
                baixo = fracao[0] % fracao[1]
                inteiro = fracao[1]
                resul = baixoInteiro(baixo, inteiro) #usando a funcao de mdc
                baixo = baixo // resul
                inteiro = inteiro // resul
            if cima and baixo:  #funcao (inteiro cima/baixo)
                print(cima, " ", baixo, "/", inteiro, sep="")
            elif cima and not baixo:  #funcao cima (apenas um numero)
                print(cima, sep="")
            elif not cima and baixo:  #funcao (baixo/inteiro)
                print(baixo, "/", inteiro, sep="")

if __name__ == "__main__":
    main()
