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

if __name__ == "__main__":
    n_inicial = 101
    m_final = 121
    resultado = num_palindromico(n_inicial, m_final)

    for numero in resultado:
        print(numero)
