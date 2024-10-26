# README

## Desafio 2 (Linguagem: Python)

Fiz uma função usando o crivo de Eratóstenes, com a otimização de iniciar os cortes pelo quadrado do número inicial. Tentei uma versão fazendo a extração dos elementos _in place_, mas ficou essa daí mesmo, só substituindo por _None_ e reduzindo a lista no final.

## Modo de Usar

Importe o arquivo e chame a função `list_primes` com o número de limite superior como argumento. Ela retorna um _generator_. Abra um terminal e inicie uma sessão do interpretador Python, assim:


```pycon
$ python
>>> import desafio02
>>> list(desafio02.list_primes(100))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

Outra maneira é usar um loop `for`:

```pycon
$ python
>>> import desafio02
>>> for prime in desafio02.list_primes(100):
...		print(prime)
...
2
3
5
(...)
89
97
```

## 1, 2, 3, Testando

Os testes vêm integrados no próprio arquivo. Usei a biblioteca unittest. É só chamar o interpretador com o nome do arquivo.

```bash
$ python desafio02.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.009s

OK
$
```
