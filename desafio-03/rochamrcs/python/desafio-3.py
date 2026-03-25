"""Minha solução para imprimir todos palindromos de 1 a 64"""

palindromos = []

for p in range(1, 65):
    p_str = str(p)
    if p_str[::-1] == p_str:
        palindromos.append(p_str)

print(palindromos)
