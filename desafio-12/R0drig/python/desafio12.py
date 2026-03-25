#encoding utf-8
'solução desafio 12'
def is_powered_2(number):
    'checks if the number is powered by 2 and if is returns the number'
    count = 0
    while number>=1:
        if number %2==0:
            pass
        elif number == 1:
            return ('true',count)
        elif number % 2 != 0:
            return ('false',count)
        number //=2
        count+=1
    return ('false',count)


def main():
    'main function of the file'
    with open('d12.txt','r',encoding='utf-8') as file:
        file = file.readlines()
    lista_numeros = [int(number.replace('\n','')) for number in file]
  # print(lista_numeros)
    for number_item in lista_numeros:
        if is_powered_2(number_item)[0]=='true':
            print(f'{number_item} {is_powered_2(number_item)[0]} {is_powered_2(number_item)[1]}')
        else:
            print(f'{number_item} {is_powered_2(number_item)[0]}')


if __name__ == '__main__':
    main()
