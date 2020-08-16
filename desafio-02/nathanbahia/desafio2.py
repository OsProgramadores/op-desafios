"""
Github: github.com/nathanbahia
LinkedIn: linkedi.com/in/nathanbahia
"""

primos = []


def checa_numeros_primos(num):
    """ Recebe um número e o avalia como primo ou não """
    divisores = list(range(2, num))
    if num > 1:
        for d in divisores:
            if num != d and num % d == 0:
                return

        primos.append(num)


for i in range(10000):
    checa_numeros_primos(i)

print(primos)
