## ENCONTRAR NÚMEROS PRIMOS DE 1 A 10000

for num in range (2, 10001):
    num_primos = True
    
    for divisor in range (2, num):
        if num % divisor == 0:
            num_primos = False
            break
    
    if num_primos:
        print (num)
