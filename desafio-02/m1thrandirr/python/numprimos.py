primos = []

for i in range(2,10001):
    for j in range(2,i+1):
        if i%j==0:
            if i==j:
                primos.append(i)
            else:
                break

for k in range(len(primos)):
    print(primos[k])
    
