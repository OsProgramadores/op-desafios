"""
Author: Teiji Watanabe
Palindrome Verification
"""


def reverse(text):
    """Return the inverse text"""
    return str(text)[::-1]


def isPalindrome(text):
    """Verify if text is palindrome return true or false"""
    return str(text) == reverse(str(text))


def main():
    """Main function"""
    numbers_list = []
    start = input("Start of period: ")
    end = input("End of period: ")
    for number in range(int(start), int(end)):
        if isPalindrome(number):
            numbers_list.append(number)
    print(*numbers_list, sep="\n")


if __name__ == "__main__":
    main()
