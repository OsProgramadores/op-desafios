## ENCONTRAR NÚMEROS PRIMOS DE 1 A 1000

for num in range (2, 1000):
    num_primos = True
    
    for divisor in range (2, num):
        if num % divisor == 0:
            num_primos = False
    
    if num_primos:
        print (num)