import math


def power2(num):
    if num == 0:
        return (num, False, 0)

    result = math.log2(num)

    if result.is_integer():
        return (num, True, int(result))
    else:
        return (num, False, 0)


def main():
    file = open("d12.txt", "r")

    nums = [int(num) for num in file]
    results = map(power2, nums)

    for (num, has_solution, solution) in results:
        if has_solution:
            print(f"{num} true {solution}")
        else:
            print(f"{num} false")


if __name__ == "__main__":
    main()
