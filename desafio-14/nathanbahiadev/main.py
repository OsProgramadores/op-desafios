def desafio_14():
    with open('d14.txt', 'r') as arquivo:
    
        for linha in arquivo.readlines():
            expressao = linha.replace('^', '**')
    
            try:
                print(int(eval(expressao)))
            
            except ZeroDivisionError:
                print('ERR DIVBYZERO')
            
            except SyntaxError:
                print('ERR SYNTAX')


if __name__ == '__main__':
    desafio_14()
