#!/usr/bin/python
# author: Alison gh: imalisoon


def is_power(num: int):
    bitmask = 1
    shift = 0

    while bitmask <= num:
        if bitmask ^ num == 0:
            return (True, shift)

        bitmask = bitmask << 1
        shift += 1

    return (False, 0)

if __name__ == "__main__":
    with open("d12.txt", "r") as _file:
        for line in _file:
            try:
                number = int(line)
                (power, s) =  is_power(number)
                if power:
                    print(f"{number} true {s}")
                else:
                    print(f"{number} false")
            except ValueError:
                print(f"numero {line} invalido")
