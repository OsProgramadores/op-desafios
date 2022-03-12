""" Searching pow. """

def existsPot(number):
    """ Searching pow. """
    initialNumber = number
    count = 0
    finalized = False
    while not finalized:
        if (number % 2 == 1 or number == 0) and number != 1:
            finalized = True
            print(f"Number: {initialNumber}\nIs power of 2: false\n")
        if number == 1:
            finalized = True
            print(f"Number: {initialNumber}\nIs power of 2: true\nExponent: {count}\n")
        number //= 2
        count += 1

with open("./d12.txt", "r", encoding="utf-8") as file:
    for l in file:
        existsPot(int(l))
