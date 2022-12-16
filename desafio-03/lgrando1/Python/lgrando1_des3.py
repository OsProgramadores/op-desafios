start = int(input('número inicial: '))
end = int(input('número final: '))


for i in range(start,end):
    ix = str(i)
    if ix == ix[::-1]:
        print(i)