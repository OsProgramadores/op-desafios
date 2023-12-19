"""
Prime calculation based on the Sieve of Eratosthenes algorithm.
"""
class PrimeCalc():
    """
    Unique class to store the calculation logic
    """
    def get_primes(self):
        """
        Implements the Sieve of Eratosthenes to find all prime numbers up to the given limit.
        Args:
        - primelimit (float): The calculation limit.
        - primerange (float): The number of prime numbers to be displayed.
        Returns:
        - primelist (list): List of prime numbers up to the user's nth given range.
        """
        primelimit = self.get_valid_limit()
        primerange = self.get_valid_range()

        primelist = set(range(2, primelimit))

        for i in range(2, int(primelimit**0.5) + 1):
            for j in range(i*2, primelimit, i):
                if j in primelist:
                    primelist.remove(j)

        return list(primelist)[:primerange] if primerange != 0 else list(primelist)

    def get_valid_limit(self):
        """
        Validates and returns the calculation limit.
        """
        while True:
            primelimit = input("Enter the calculation limit: ")
            try:
                primelimit = float(primelimit)
                if primelimit < 0:
                    print("Please enter a positive number.")
                elif primelimit > 1000000:
                    print("The limit is too high. Please enter a number less than 1000000.")
                else:
                    break
            except ValueError:
                primelimit = primelimit.strip()
                if primelimit == "":
                    primelimit = 100.0
                    print("No given limit. It has been automatically set to 100.")
                    break
                print("Invalid input. Please enter a valid number.")
        if round(primelimit) != primelimit:
            print(f"The limit has been rounded to the nearest integer: {round(primelimit)}")
        primelimit = int(round(primelimit))
        if primelimit == 0:
            print("The limit has been automatically set to 100.")
            primelimit = 100
        return primelimit

    def get_valid_range(self):
        """
        Validates and returns the number of prime numbers to be displayed.
        """
        while True:
            primerange = input("Enter the number of prime numbers to be displayed (0 = all): ")
            try:
                primerange = float(primerange)
                if primerange < 0:
                    print("Please enter a positive number.")
                elif primerange > 1000000:
                    print("The limit is too high. Please enter a number less than 1000000.")
                else:
                    break
            except ValueError:
                primerange = primerange.strip()
                if primerange == "":
                    primerange = 0
                    print("No given limit. All primes will be printed.")
                    break
                print("Invalid input. Please enter a valid number.")
        if round(primerange) != primerange:
            print(f"The limit has been rounded to the nearest integer: {round(primerange)}")
        primerange = int(round(primerange))
        return primerange
    