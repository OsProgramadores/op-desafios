# README

## Desafio 3 (Linguagem: Python)

Nesse desafio fiz duas funções. Uma delas, `is_palindrome`, testa se uma _string_ é um palíndromo e retorna um Bool. A outra, `print_palindromes`, recebe dois argumentos inteiros e testa o intervalo entre os dois, ambos incluídos, à procura de palíndromos. Ainda, `print_palindromes` recebe um terceiro argumento opcional, _print_output_, que faz com que os resultados sejam impressos ao invés de apenas retornar o conjunto de palíndromos encontrados.

## Modo de Usar

Abra um terminal e execute o programa, assim:

```bash
$ python desafio03.py 101 121
101
111
121
$
```

## 1, 2, 3, Testando

Os testes vêm integrados no próprio arquivo. Usei a biblioteca unittest. É só chamar o interpretador com o nome do arquivo.

```bash
$ python desafio03.py --test
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
$
```

## Ajuda

Para consultar todas as opções do programa, é só executá-lo com a opção `--help`.

```bash
$ ./desafio03.py --help
usage: desafio03.py [-h] [-n] [-t] [extremes ...]

Lista todos os números palíndromos existentes entre dois extremos.

positional arguments:
  extremes       Os números inicial e final para a busca.

options:
  -h, --help     show this help message and exit
  -n, --noprint  Somente retorne os resultados.
  -t, --test     Roda os testes.
```
