primos_list = []

for i in range(2,1001):
    for j in range(2,i+1):
        if i%j==0:
            if j==i:
                primos_list.append(i)
            else:
                break

for k in range(len(primos_list)):
    print(primos_list[k])
             
