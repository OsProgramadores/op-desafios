"""Challenge 12 written in Python."""
from math import log2
from sys import argv


def main():
    """Main function."""
    filename = argv[1]
    with open(filename) as f:
        for line in f:
            number = int(line)
            try:
                exponent = log2(number)
            except ValueError:
                print(f"{number} false")
            else:
                if exponent.is_integer():
                    exponent = int(exponent)
                    print(f"{number} true {exponent}")
                else:
                    print(f"{number} false")


if __name__ == "__main__":
    main()
