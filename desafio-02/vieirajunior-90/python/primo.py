def prime(end=10000):
    n = 1
    while n <= end:
        div = 0
        for c in range(1, n + 1):
            if n % c == 0:
                div += 1
        if div == 2:
            print(f'[{n}]', end='')
        n += 1
    print()
prime()