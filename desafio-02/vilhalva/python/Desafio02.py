for i in range(1, 10000):
    primo = 1
    for j in range(2, i-1):
        if i % j == 0:
            primo = 0
            break
    if primo:
        print(i)

