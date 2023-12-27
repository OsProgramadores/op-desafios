"""
This module is used to calculate palindromes in a given range.
"""

class PalCalc():
    """
    This class is used to calculate palindromes.
    """
    def get_init_num(self):
        """ 
        Validates and returns the initial number.
        """
        while True:
            num1 = input('Insert first number:')
            try:
                num1 = int(num1)
                if num1 < 0:
                    print("Please enter a positive number.")
                elif num1 > 1000000:
                    print("The number is too high. Please enter a number less than 100001.")
                else:
                    break
            except ValueError:
                num1 = num1.strip()
                if num1 == "":
                    num1 = 0
                    print("No given number. It has been automatically set to 0.")
                    break
                print("Invalid input. Please enter a valid number.")
            if round(num1) != num1:
                print(f"The number has been rounded to the nearest integer: {round(num1)}")
            num1 = int(round(num1))
            if num1 == 0:
                print("The number has been automatically set to 1.")
                num1 = 1
                break
        return num1

    def get_final_num(self):
        """ 
        Validates and returns the final number.
        """
        while True:
            num2 = input('Insert second number:')
            try:
                num2 = int(num2)
                if num2 < 0:
                    print("Please enter a positive number.")
                elif num2 > 1000000:
                    print("The number is too high. Please enter a number less than 100001.")
                else:
                    break
            except ValueError:
                num2 = num2.strip()
                if num2 == "":
                    num2 = 100
                    print("No given number. It has been automatically set to 100.")
                    break
                print("Invalid input. Please enter a valid number.")
            if round(num2) != num2:
                print(f"The number has been rounded to the nearest integer: {round(num2)}")
            num2 = int(round(num2))
            if num2 == 0:
                print("The number has been automatically set to 100.")
                num2 = 100
                break
        return num2

    def show_palindromes(self):
        """
        Shows the palindromes.
        """
        num1 = self.get_init_num()
        num2 = self.get_final_num()
        palist = set(range(num1, num2))
        for num in range(num1, num2):
            # If its a one digit number, it is a palindrome.
            if num < 10:
                continue
            # If its betweeen two and 6 digits:
            if num < 100000:
                # If its a two digit number, check if its a palindrome.
                if num < 100:
                    if num % 11 != 0:
                        palist.remove(num)
                # If its a three digit number, check if its a palindrome.
                elif num < 1000:
                    if num % 10 != num // 100:
                        palist.remove(num)
                # If its a four digit number, check if its a palindrome.
                elif num < 10000:
                    if num % 10 != num // 1000 or num % 100 // 10 != num // 100 % 10:
                        palist.remove(num)
                # If its a five digit number, check if its a palindrome.
                elif num < 100000:
                    if num % 10 != num // 10000 or num % 100 // 10 != num // 1000 % 10:
                        palist.remove(num)
        return list(palist)
#     if num < 100:
#         if num % 11 != 0:
#             palist.remove(num)
#     elif num < 1000:
#         if num % 10 != num // 100:
#             palist.remove(num)
#     elif num < 10000:
#         if num % 10 != num // 1000 or num % 100 // 10 != num // 100 % 10:
#             palist.remove(num)
#     elif num < 100000:
#         if num % 10 != num // 10000 or num % 100 // 10 != num // 1000 % 10:
#             palist.remove(num)
#     elif num < 1000000:
#         if num % 10 != num // 100000:
#             palist.remove(num)
#         elif  num % 100 // 10 != num // 10000 % 10 or num % 1000 // 100 != num // 1000 % 10:
#             palist.remove(num)
# return list(palist)
