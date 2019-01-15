"""Calculate palindrome numbers between two numbers"""

def palindromo(start, end):
    """Returns a list of palindrome numbers between start and end"""
    return [i for i in range(start, end + 1) if str(i) == str(i)[::-1]]


if __name__ == '__main__':
    print(palindromo(1, 1500))
