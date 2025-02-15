init_num = 1
final_num = 10000
lista = ''

def primo(num):
    nums = []
    num = int(num)
    for n in range(num):
        n += 1
        sum = (num / n) - int(num / n)
        if sum == 0.0:
            nums.append(1)
    if nums.count(1) == 2:
        return True
    else:
        return False

for num in range(final_num):
    num += 1
    if primo(num):
        lista += f'{num} '

print(lista)