# Create class for calculating the palindromes
class PalCalc():
    """
    Unique class to store the calculation logic
    """
    def get_pal(self):
        """
        Calculates the palindromes and returns a list of them based on the limit and range.
        """

        # Get the limit and range
        pallimit = self.get_valid_limit()
        palrange = self.get_valid_range()
        pallist = {i for i in range(1, pallimit + 1) if str(i) == str(i)[::-1]}
        return list(pallist)[:palrange] if palrange != 0 else list(pallist)

    def get_valid_limit(self):
        """
        Validates and returns the calculation limit.
        """
        while True:
            pallimit = input("Enter the calculation limit: ")
            try:
                pallimit = float(pallimit)
                if pallimit < 0:
                    print("Please enter a positive number.")
                elif pallimit > 1000000:
                    print("The limit is too high. Please enter a number less than 1000000.")
                else:
                    break
            except ValueError:
                pallimit = pallimit.strip()
                if pallimit == "":
                    pallimit = 100.0
                    print("No given limit. It has been automatically set to 100.")
                    break
                print("Invalid input. Please enter a valid number.")
        if round(pallimit) != pallimit:
            print(f"The limit has been rounded to the nearest integer: {round(pallimit)}")
        pallimit = int(round(pallimit))
        if pallimit == 0:
            print("The limit has been automatically set to 100.")
            pallimit = 100
        return pallimit

    def get_valid_range(self):
        """
        Validates and returns the number of prime numbers to be displayed.
        """
        while True:
            palrange = input("Enter the number of prime numbers to be displayed (0 = all): ")
            try:
                palrange = float(palrange)
                if palrange < 0:
                    print("Please enter a positive number.")
                elif palrange > 1000000:
                    print("The limit is too high. Please enter a number less than 1000000.")
                else:
                    break
            except ValueError:
                palrange = palrange.strip()
                if palrange == "":
                    palrange = 0
                    print("No given limit. All numbers will be printed.")
                    break
                print("Invalid input. Please enter a valid number.")
        if round(palrange) != palrange:
            print(f"The limit has been rounded to the nearest integer: {round(palrange)}")
        palrange = int(round(palrange))
        return palrange