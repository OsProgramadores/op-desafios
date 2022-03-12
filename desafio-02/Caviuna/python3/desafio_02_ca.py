'''
Desafio 02 
Escreva um programa para listar todos os números primos entre 1 e 10000, na linguagem de sua preferência. 
'''

numeros = [] 
class __main__():   
    def lista(x):
        for i in range(1, x+1):
            div = 0
            for j in range(1, i+1):
                if(i%j == 0):
                    div += 1
            if (div == 2):
                numeros.append(i)
        return print(numeros)
if __name__ == "__main__":
    __main__.lista(10)