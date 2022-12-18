"""Module providingFunction printing python version."""
#!/usr/bin/env python3
start = int(input('número inicial: '))
end = int(input('número final: '))
print('Os números palindrômicos entre este intervalo são:')
for i in range(start,end):
    ix = str(i)
    if ix == ix[::-1]:
        print(i)
    
