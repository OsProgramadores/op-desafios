# Desafio 03 - Números Palíndromos

## Descrição

Programa que imprime todos os números palíndromos entre dois valores fornecidos
pelo usuário, incluindo os limites quando também forem palíndromos.

Um número palíndromo mantém o mesmo valor quando lido de trás para frente
(ex.: 101, 1221, 3003). Números de um algarismo são palíndromos por definição.

## Solução

O programa lê o valor inicial e o valor final via terminal e valida as entradas
(apenas inteiros positivos, com o inicial menor ou igual ao final).

Como o desafio permite números de até `2^64 - 1` (máximo unsigned de 64 bits),
a solução utiliza a aritmética unsigned do Java:

- `Long.parseUnsignedLong` para ler os valores;
- `Long.toUnsignedString` para representar corretamente números acima de `2^63 - 1`;
- `Long.compareUnsigned` para comparar os limites.

Para cada número do intervalo, converte-se o valor para texto e verifica-se se o
texto é igual ao seu reverso, utilizando `StringBuilder.reverse()`.

## Como compilar

```bash
javac meuDesafio03.java
```

## Como executar

O programa lê os valores de forma interativa via terminal:

```bash
java meuDesafio03
```

## Exemplos

```bash
$ java meuDesafio03
Digite o valor inicial: 1
Digite o valor final: 20
Números palíndromos entre 1 e 20:
1
2
3
4
5
6
7
8
9
11
```

```bash
$ java meuDesafio03
Digite o valor inicial: 3000
Digite o valor final: 3010
Números palíndromos entre 3000 e 3010:
3003
```

```bash
$ java meuDesafio03
Digite o valor inicial: 101
Digite o valor final: 121
Números palíndromos entre 101 e 121:
101
111
121
```

Testado com OpenJDK 21.
