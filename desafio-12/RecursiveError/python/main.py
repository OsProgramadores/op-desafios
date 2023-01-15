"""
Autor: Guilherme Silva Schultz (RecursiveError)
Data: 14-01-2023
Explicação, o desafio consiste em varificar se o numero é uma potencia de 2, esse processo usa calculos matematicos com log para resolver.
porem por ser uma base de 2 podemos simplificar usando binario, binario é uma notação numerica de base 2, numeros são formados pela soma de potencias de 2
ex: 
0b0001 = 2^0 = 1
0b0010 = 2^1 = 2 
0b0011 = 2^1 + 2^0 = 3
0b0100 = 2^2 = 4

como podemos ver, quando um numero pertence a potencia 2, só existe um "1" em toda cadeia de bits, então podemos usar operações de bitwise para resolver o desafio
usando a operação XOR e bitshifts podemos verificar facilmente

primeiro criamos um bitmask usando bitshift a cada operação
ex:
1<<0 = 0b0001
1<<1 = 0b0010
1<<2 = 0b0100

depois usamos esse bitmask para realizar uma operação XOR no numero, se ele for uma potencia de 2 o resultado vai ser 0
ex
4 = 2^2 = 0b0100 XOR 0b0100 = 0b000 = 0
8 = 2^3 = 0b1000 XOR 0b1000 = 0b000 = 0 
10 = 0b1010 XOR 0b1000 = 0b0010 = 2
"""

def check_num(num: int):
    bitmask = 1
    shift = 0
    while bitmask <= num:
        if bitmask ^ num == 0:
            return (True, shift)
        bitmask = bitmask << 1
        shift += 1
    return (False, 0)

with open("d12.txt", "r", encoding="utf-8") as num_file:
    for line in num_file:
        try:
            number = int(line)
            (potencia, s) =  check_num(number)
            if potencia:
                print(f"{number} true {s}")
            else:
                print(f"{number} false")
        except ValueError:
            print(f"numero {line} invalido")
