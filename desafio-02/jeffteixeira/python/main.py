"""Show all prime numbers between 1 and 1000"""


def main():
    """Function main of the program"""
    inferior_limit = 1
    superior_limit = 10000
    prime_numbers = get_prime_numbers(inferior_limit, superior_limit)
    show_numbers(prime_numbers)


def get_prime_numbers(inferior_limit, superior_limit):
    """Function that returns a list of prime numbers"""
    prime_numbers = []
    for number in range(inferior_limit, superior_limit + 1):
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers


def is_prime(number):
    """Function that checks if a number is prime or not"""
    number_of_dividers = 0
    for i in range(1, number + 1):
        if number % i == 0:
            number_of_dividers += 1
    return number_of_dividers == 2


def show_numbers(numbers):
    """Function that prints a list of numbers"""
    for number in numbers:
        print(number)


if __name__ == '__main__':
    main()
