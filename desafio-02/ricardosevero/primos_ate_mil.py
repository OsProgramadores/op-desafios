def is_prime(n):
    div = 2
    if n == 2:
        return True
    
    while n % div != 0 and div <= n/2:
        div += 1
    if n % div == 0:
        return False
    return True
    
start = 2
stop = 1000
while start < stop:
    if is_prime(start):
        print(start, end=', ')
    start += 1
