"""
Esse progama mostrar todos os números palindrômicos entre um número e outro
"""
# Mostra todos os números palindrômicos entre start e end
palindromo = lambda start,end: [i for i in range(start, end + 1) if str(i) == str(i)[::-1]]
print(palindromo(0, 10000), end='')

