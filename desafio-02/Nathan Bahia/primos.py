'''
Resolução do Desafio 2

GitHub: github.com/nathanbahia
Linkedin: linkedin.com/in/nathanbahia
E-mail: nathanbabahia@gmail.com

'''

primos = []

def checa_numeros_primos(num):
    divisores = list(range(2, num))
    if num > 1:
        for d in divisores:
            if num != d:
                if num % d == 0:
                    return
                
        primos.append(num)


for i in range(10000):
    checa_numeros_primos(i)

print(primos)
    
