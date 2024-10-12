isPalindromic = lambda x: (strNumber := str(x)) == strNumber[::-1]

def impressPalindromicNumbersInRange(start: int, end: int) -> None:
    for number in range(start, end + 1):
        if isPalindromic(number):
            print(number, ", ", sep="", end="")
    else: print("\b\b.")

impressPalindromicNumbersInRange(1, 20)