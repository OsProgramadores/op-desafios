# Desafio 03 - Palíndromos
Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado.

Este programa recebe dois números naturais e verifica quais números entre os dois seguem a regra de palíndromo.
Se o número é considerado palíndromo, é impresso na tela.

Se as entradas não forem números naturais, um erro é lançado.

## Como rodar
Para rodar, use Python na versão 3.12 ou superior e utilize o comando:

`python desafio-03.py`

## Algoritmo
```
def is_palindrome(word: str) -> bool:
    return word == word[::-1]
```
Função que verifica se uma palavra é igual ao seu inverso, ou seja, é palíndromo.

Em python, é possível fazer *slicing* ou "fatiamento" de strings usando a notação `string[começo:fim:passo]`.

Quando *começo* e *fim* estão em branco, python entende como pegar a palavra toda e, aqui, onde passo é negativo, significa que ele irá ler a string do fim ao começo.

```
def all_palindromes_between(start: int, end: int):
    for i in range(start, end + 1):
        if is_palindrome(str(i)):
            print(i)
```
A função recebe dois inteiros e percorre todos os números entre eles
verificando se cada um desses números é palíndromo.

Se sim, imprime o número na tela

```
def read_int() -> int:
    while True:
        try:
            string = input("Digite um número natural [S ou 0 para sair]: ")

            if string.upper() == "S":
                return 0

            assert string.isnumeric(), "Por favor, digite apenas números naturais."

            return int(string)
        except AssertionError as error:
            print(error)
```
Função que lê uma string e verifica se os caracteres são numéricos.
Neste caso, isso significa que não aceitará letras, símbolos, pontos, sinais, etc.

Se sim, a converte em inteiros e retorna.

Se não, dá a opção para o usuário tentar novamente ou sair do programa, digitando "S" ou 0 (zero).


```
def main():
    start = read_int()
    if not start:
        return

    end = read_int()
    if not end:
        return

    if start > end:
        start, end = end, start

    all_palindromes_between(start, end)
```
Função que lê as entradas do usuário e as valida.

Se as entradas estiverem corretas e não forem nulas, as ordena e roda o algoritmo principal para gerar os palíndromos.