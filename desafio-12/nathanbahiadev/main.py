def is_power(number):
    power = 0

    while True:
        result = 2 ** power

        if result == number:
            return f"{number} true {power}"
        
        if result > number:
            return f"{number} false"

        power += 1


def main():
    with open('d12.txt', 'r') as arquivo:
        for n in arquivo.readlines():
            numero = int(n)
            print(is_power(numero))


if __name__ == '__main__':
    main()
