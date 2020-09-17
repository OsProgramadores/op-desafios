"""
##
## Desafio-03: Palíndromos ---- OsProgramadores
## Desenvolvido por: Magnu Windell A Santos (@maagwiin)
## Data: 17/09/2020
## Descrição: listar os números palíndromos entre dois números
##
"""

def verify(n_min, n_max):
    """ Verifica se os números informados são válidos """
    if n_max < n_min:
        print("-- ERRO: O segundo valor deve ser maior que o primeiro!!\n")
        main()
    elif n_max == n_min:
        print("-- ERRO: Os valores devem ser diferentes!!\n")
        main()

    if abs(n_min) > ((1 << 64) - 1) or abs(n_max) > ((1 << 64) - 1):
        print("-- ERRO: Digite números menores!!\n")
        main()
    else:
        betweenPalindromes(n_min, n_max)


def betweenPalindromes(n_min, n_max):
    """ Compara os números em busca de palíndromos """
    for n in range(n_min, n_max + 1):
        aux = int(str(n)[::-1])
        if n == aux:
            print('-- {}'.format(n))


def main():
    """ Função Principal """
    print("Digite 2 números para listar os palíndromos entre eles!")
    start = int(input('Entre com o primeiro número: '))
    end = int(input('Entre com o último número: '))
    verify(start, end)



if __name__ == "__main__":
    main()
