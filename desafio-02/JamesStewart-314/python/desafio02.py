def check_primality(number: int, /) -> bool:
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    for i in range(3, int(number ** (1 / 2)) + 1, 2):
        if not number % i:
            return False
        
    return True

[ print("• Prime Number Detected:\033[32m", number, "\033[0m") for number in range(10001) if check_primality(number) ]
