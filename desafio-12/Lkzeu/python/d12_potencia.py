def main():
    try:
        with open("d12.txt", "r") as f:
            numbers = f.readlines()
            for n in numbers:
                number = int(n)
                e_par  = not number & 1

                if e_par or number == 1:
                    expoentes = contar_exp(number)
                    if (1 << expoentes) == number: # ou if (2 ** expoentes) == number:
                        print(f"{number} true {expoentes}")
                        continue
                print(f"{number} false")

    except FileNotFoundError:
        print("d12.txt não encontrado!\n" +
              "Verifique se o arquivo d12.txt está na mesma pasta do programa.\n" +
              "você pode baixa-lo em: https://osprogramadores.com/desafios/d12/")

    except OSError as e:
        print(f"{type(e).__name__}: {e}")

def contar_exp(number: int) -> int:
    counter = 0
    while number > 1:
        counter += 1
        number >>= 1
    return counter

if __name__ == "__main__":
    main()
