import sys

def potencia2(n):
    if n <= 0:
        return False, 0
    count = 0
    while n % 2 == 0:
        n = n // 2
        count += 1
    if n == 1:
        return True, count
    else:
        return False, 0

def main():
    for linha in sys.stdin:
        linha = linha.strip()
        if linha:
            numero = int(linha)
            
            e_potencia, exp = potencia2(numero)
            
            if e_potencia:
                print(f"{numero} true {exp}")
            else:
                print(f"{numero} false")

if __name__ == "__main__":
    main()