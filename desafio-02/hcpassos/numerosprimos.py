num = 1
while num <= 1000:
    div = num - 1
    while div > 1:
        if num % div == 0:
            break
        div = div - 1
    else:
        print(num)
    num = num + 1
