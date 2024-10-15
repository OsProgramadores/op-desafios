def eh_primo(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 10001):
    if eh_primo(num):
        print(num)
