def eratosthenes(num):
    primo = [True for _ in range(num+1)]
    p = 2
    while p*p<=num:
        if primo[p]:
            for i in range(p*p,num+1,p):
                primo[i] = False
        p+=1
    for p in range(2,num+1):
        if primo[p]:
            print(p)

eratosthenes(10000)