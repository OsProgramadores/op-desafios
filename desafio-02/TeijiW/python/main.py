numbers_to_print = ""
for n1 in range(1, 10000):
    matches = 0
    for n2 in range(1, n1):
        if n1 % n2 == 0:
            matches += 1
    if matches <= 2:
        string_concat = "{} \n"
        numbers_to_print += string_concat.format(n1)

print(numbers_to_print)
