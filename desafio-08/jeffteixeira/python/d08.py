"""Challenge 08 written in Python."""
from math import gcd
from sys import argv


def main():
    """Main function."""
    filename = argv[1]
    with open(filename) as f:
        for line in f:
            if "/" in line:
                numerator, denominator = map(int, line.split("/"))
                if denominator == 0:
                    print("ERR")
                elif numerator % denominator == 0:
                    print(numerator // denominator)
                elif numerator // denominator > 0:
                    print(f"{numerator // denominator} {numerator % denominator}/{denominator}")
                else:
                    greatest_common_divisor = gcd(numerator, denominator)
                    new_numerator = numerator // greatest_common_divisor
                    new_denominator = denominator // greatest_common_divisor
                    print(f"{new_numerator}/{new_denominator}")
            else:
                print(int(line))


if __name__ == "__main__":
    main()
