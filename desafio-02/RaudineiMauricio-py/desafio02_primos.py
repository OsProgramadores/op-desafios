
def eh_primo(n):
    if n % 2 == 0 and n != 2:  # NÚMEROS PARES MAIORES QUE 2 NAO NÃO SÃO PRIMOS
        return False
    # VERIFICANDO OS ÍMPARES
    for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0: 
                return False 
    return True

#SÓ O 2 É PRIMO E PAR AO MESMO TEMPO
print(2, end=" ") 

for numero in range(3, 10001, 2):  #COMECEI A PROCURAR APENAS ÍMAPARES COMEÇANDO PELO 3
    if eh_primo(numero):
        print(numero, end=" ")
