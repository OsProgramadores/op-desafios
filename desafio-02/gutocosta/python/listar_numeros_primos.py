'''
    Programa para listar todos os números primos entre 1 e 10000
'''


def main():
    '''
        função verifica os numeros primos de 1 a 10000
    '''
    valor_limite = 10000
    lista_num_int = [True for i in range(valor_limite+1)]
    primo = 2
    while primo * primo <= valor_limite:
        if lista_num_int[primo]:
            for i in range(primo * 2, valor_limite+1, primo):
                lista_num_int[i] = False
        primo += 1
    for primo in range(2, valor_limite):
        if lista_num_int[primo]:
            print(primo)


if __name__ == "__main__":
    main()
