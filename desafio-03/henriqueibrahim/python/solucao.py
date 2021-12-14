"""Check for palindrome numbers"""
input1 = int(input())
input2 = int(input())

numbers = list(range(input1, input2 + 1)) # +1 para poder incluir o último número

for n in numbers:
    temp = n # Var temporária para salvar valor de n
    reverseNum = 0
    while n > 0:
        lastDigit = n % 10 # Retirar último dígito
        reverseNum = reverseNum * 10 + lastDigit # Add o último dígito para o lado esquerdo do n
        n = n // 10 # Divide para deixar o último dígito
    if temp == reverseNum:
        print(reverseNum)

