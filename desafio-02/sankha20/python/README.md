# Desafio 02 - Primos
Programa que irá listar todos os números primos até 10.000

## Como rodar
Para rodar, use Python na versão 3.12 ou superior e utilize o comando: 
`python desafio-02.py`

## Como funciona
```
    if n in primes: return True
    if n < 2: return False
    if n % 2 == 0: return False
```
Realiza testes rápidos para detectar se é ou não primo

```
if prime > n ** 0.5:
``` 

Seguindo a teoria dos pares de divisores, por exemplo os de 100:
* 1 e 100
* 2 e 50
* 4 e 25
* 5 e 20
* etc

Não faz sentido tentar dividir por um primo maior que a raiz quadrada do número, pois ele já teria sido dividido pelo par menor.

```
"\n".join(map(str, primes))
```
A função `join` junta os elementos de uma lista, separando-os pela string determinada. Ela só funciona com lista de strings, e não com números, por isso é preciso transformar todos os números da lista ***primes*** em strings.

Para facilitar essa transformação, utilizamos a função `map`, que aplicará a função indicada, nesse caso `str` em todos os elementos da lista *primes*.
