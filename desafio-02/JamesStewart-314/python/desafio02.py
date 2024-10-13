def check_primality(number: int, /) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** (1 / 2)) + 1, 2):
        if not number % i:
            return False

    return True

for currentNumber in range(10001):
    if check_primality(currentNumber):
        print(currentNumber)
