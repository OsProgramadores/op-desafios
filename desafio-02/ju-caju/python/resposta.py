for x in range(0, 10001):
    y = x - 1
    primo = True

    if x < 2:
        primo = False

    while y > 1:
        if x % y == 0:
            primo = False
            break
        y = y - 1

    if primo:
        print(x)