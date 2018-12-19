
def is_primo(n, primos):
    if n < 2:
        return False

    for primo in primos:
        if n % primo == 0:
            return False
    return True
    
def numeros():
    yield 2
    for x in range(3, 10001, 2):
        yield x

def main():
    primos = []
    for n in (n for n in numeros() if is_primo(n, primos)):
        primos.append(n)
        print(n)

if __name__ == '__main__':
    main()
