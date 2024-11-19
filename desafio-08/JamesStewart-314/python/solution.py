import os

def GCD(number_1: int, number_2: int) -> int:
    # Euclid's Algorithm :
    aux_number_1 = max(number_1, number_2)
    aux_number_2 = min(number_1, number_2)

    remainder = aux_number_1 % aux_number_2

    while remainder:  # Remainder != 0
        aux_number_1 = aux_number_2
        aux_number_2 = remainder
        remainder = aux_number_1 % aux_number_2

    return aux_number_2

if __name__ == '__main__':
    filePath = os.path.join(os.path.dirname(__file__), "frac.txt")

    with open(filePath, "r") as fractionsFile:
        while (fractionContent := fractionsFile.readline().strip()):
            fractionSplitted = list(map(int, fractionContent.split('/')))

            if len(fractionSplitted) == 1 or fractionSplitted[1] == 1:
                print(fractionSplitted[0])
                continue
            if fractionSplitted[1] == 0:
                print("ERR")
                continue
            if fractionSplitted[0] == 0:
                print(0)
                continue

            fractionSimplified = divmod(*fractionSplitted)

            if fractionSimplified[1] == 0:
                print(fractionSimplified[0])
                continue

            mdcFromRemainingPart = GCD(fractionSimplified[1], fractionSplitted[1])

            remainNum = str(fractionSimplified[1] // mdcFromRemainingPart)
            remainDen = str(fractionSplitted[1] // mdcFromRemainingPart)

            remainingPart = f"{remainNum}/{remainDen}"

            if fractionSimplified[0] == 0:
                print(remainingPart)
                continue

            print(fractionSimplified[0], remainingPart)
