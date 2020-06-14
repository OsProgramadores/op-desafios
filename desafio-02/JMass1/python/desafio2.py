"""
CODIGO PARA LISTAR NUMEROS PRIMOS DE 1 A 10000
"""

print('-=-=-=-=-=-=-=--=- Desafio-02 - Juliano Massanetto -=-=-=-=-=-=-=--=-')


#DECLARANDO VARIAVEIS
primos = [2]
N = int()
COUNT = int()

#ITERACAO DOS NUMEROS DE 3 - 10000
for N in range(3, 10000, 2):
    i = int(1)

#TESTE DE HIPOTESE PARA DETERMINAR NUM. PRIMOS
    while i <= N:
        if N%i == 0:
            COUNT += 1
        if COUNT > 2:
            break
        i += 1
    if COUNT <= 2:
        primos.append(N)
    COUNT = 0

#IMPRESSAO DOS RESULTADOS
print(primos)
