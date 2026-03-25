""" Solução do Desafio 08 em Python por @ikkebr """
def gcd(a, b):
    """ MDC... """
    if b == 0:
        return a
    return gcd(b, a%b)

with open('frac.txt', 'r') as f:
    for line in f:
        parsed = line.strip().split('/')
        #print(parsed)
        #print(line, end='= ')
        if len(parsed) == 0:
            print('ERR')
        elif len(parsed) == 1:
            print(parsed[0])
        else:
            if parsed[1] == '0':
                print('ERR')
                continue
            divisor, dividendo = list(map(int, parsed))
            quociente = divisor // dividendo
            resto = divisor % dividendo

            _gcd = gcd(resto, dividendo)
            resto = resto//_gcd
            dividendo = dividendo//_gcd


            if quociente and resto:
                print("{} {}/{}".format(quociente, resto, dividendo))
            elif resto:
                print("{}/{}".format(resto, dividendo))
            else:
                print("{}".format(quociente))
