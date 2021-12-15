"""
Solução do desafio 02 do site os programadores
"""
def verifica_primo(numero):
    """
    metodo pra verificar se o numero é primo
    """
    numero_divisoes = 0
    for inc in range(1, numero+1):
        if numero%inc == 0:
            numero_divisoes += 1
            if(numero_divisoes > 2):
                return False

    if(numero_divisoes==2):
        return True

def listar_primos(primos, numero_teto):
    """
    lista os numeros primos do inicio até o numero teto
    """
    for inc in range(1, numero_teto):
        if verifica_primo(inc):
            primos.append(inc)


def main():
    """
    função main
    """
    primos = []
    listar_primos(primos, 10000)
    print(primos)

if __name__ == "__main__":
    main()
