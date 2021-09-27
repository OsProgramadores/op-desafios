for i in range(1,10002):
    if i == 1:
        resp = 1
    else:
        resp = 0
    for j in range(1,i+1):
        if i % j == 0:
            resp +=1
    if resp == 2:
        print (i)
        