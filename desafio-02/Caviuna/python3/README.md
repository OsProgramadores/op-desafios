# Listando números primos 
- Programa que lista os números primos entre 1 e 10000 escrito em Python.
- O programa tenta simplificar os laços para que seja feita uma interação mais dinámica.	

- Baseado em resposta contida no link: https://pt.stackoverflow.com/questions/205458/obter-a-lista-de-n%C3%BAmeros-primos-menores-que-n



- Vale-se destacar que para o pensamento computacional por mais que pareça simples ele tem uma nuança de complexidade. Abordagem interessante descrita abaixo: 

```	 
- To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

    1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    2. Initially, let p equal 2, the smallest prime number.
    3. Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
    4. Find the smallest number in the list greater than p that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
    5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.

```	 

- Fonte: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes 


### Ainda pretendo voltar a esse desafio para melhorar a minha resposta de acordo com o tentado: 

``` python

# Original code: 
numeros = []
def lista(x):
    for i in range(1, x+1):
        div = 0
        for j in range(1, i+1):
             if(i%j == 0):
                 div += 1
        if (div == 2):
             numeros.append(i)
    print(numeros)
lista(100)


# tentativa de implementar 
# Error: Returna apenas um lista vazia. 
def lista(x):
    for i, j in enumerate(range(1, x+1)):
        div = 0
        if(i%j == 0):
            div += 1
        if (div == 2):
            numeros.append(i)
    print(numeros)
lista(100)


# Outra forma tentada: 
# Error: Retorna apenas uma lista com 10000 zeros. 

def lista (x):
    div = 0
    numeros = [div for i in range(1, x+1) for j in range(1, i+1) if i%j == 0]
    div += 1 
    if (div == 2):
        numeros.append(i)
    print(numeros)

lista(10000)  


``` 