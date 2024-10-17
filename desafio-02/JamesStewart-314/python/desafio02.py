def check_primality(number: int, /) -> bool:
    assert isinstance(number, int), "\'number\' must be of type \'int\'."

    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if not number % i:
            return False

    return True


# Move o cursor do terminal duas linhas acima para
# corrigir as quebras de linha excedentes:
print("\033[2A")
for currentNumber in range(10):
    if check_primality(currentNumber):
        print(f"\n• \033[32m{currentNumber:,}\033[0m;", end="")
print("\b \r")
