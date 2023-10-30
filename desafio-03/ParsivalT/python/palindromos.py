"""

Resolução do desafio-03

"""

def verificaPalindromo(num) -> bool:
    if str(num) == str(num)[::-1]:
        return True

    return False

for c in range(1, 100):
    if verificaPalindromo(c):
        print(c, end=' ')
print()
