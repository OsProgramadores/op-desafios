"""System module."""
[min_in, max_in] = input('').split(' ')
result = []

for number in range(int(min_in), int(max_in)):
    if str(number)[::-1] == str(number):
        result.append(number)

print(result)
