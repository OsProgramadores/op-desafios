def num_palindromico(n, m):
    palindromos = []
    for num in range(n, m + 1):
        str_num = str(num)
        if str_num == str_num[::-1]:
            palindromos.append(num)
    return palindromos

#ex:
n = 101
m = 121
resultado = num_palindromico(n, m)
print(f"Os números palindrômicos entre {n} e {m} são: {resultado}")
