# README

## Desafio 3 (Linguagem: Python)

Nesse desafio fiz duas funções. Uma delas, `is_palindrome`, testa se uma _string_ é um palíndromo e retorna um Bool. A outra, `print_palindromes`, recebe dois argumentos inteiros e testa o intervalo entre os dois, ambos incluídos, à procura de palíndromos. Ainda, `print_palindromes` recebe um terceiro argumento opcional, _print_output_, que faz com que os resultados sejam impressos ao invés de apenas retornar o conjunto de palíndromos encontrados.

## Modo de Usar

Para os fins a que se propõe o desafio, importe o arquivo e chame a função `print_palindromes` com os números para _begin_ e _end_ como argumentos. Abra um terminal e inicie uma sessão do interpretador Python, assim:


```pycon
$ python
>>> import desafio03
>>> desafio03.print_palindromes(101, 121)
[101, 111, 121]
```

Outra maneira é imprimir os resultados no terminal, usando _print_output_:

```pycon
$ python
>>> import desafio03
>>> desafio03.print_palindromes(101, 121, print_outpur=True)
101
111
121
>>>
```

## 1, 2, 3, Testando

Os testes vêm integrados no próprio arquivo. Usei a biblioteca unittest. É só chamar o interpretador com o nome do arquivo.

```bash
$ python desafio03.py
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
$
```
