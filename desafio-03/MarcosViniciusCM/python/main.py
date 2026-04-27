def num_palindromico(n, m):
    palindromos = []
    for num in range(n, m + 1):
        if 0 <= num <= 9:
            palindromos.append(num)
        else:
            str_num = str(num)
            if str_num == str_num[::-1]:
                palindromos.append(num)
    return palindromos

# ex:
n = 101
m = 121
resultado = num_palindromico(n, m)
for num in resultado:
    print(num)