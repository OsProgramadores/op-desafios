def check_primality(number: int, /) -> bool:
    assert isinstance(number, int), "\'number\' must be of type \'int\'."

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

for currentNumber in range(10_001):
    if check_primality(currentNumber):
        print(f"\n• \033[32m{currentNumber:,}\033[0m;", end="")
print("\b ")
