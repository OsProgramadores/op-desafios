# Números Primos até 10000

## Apresentação

Projeto desenvolvido em Python utilizando o algoritmo Crivo de Eratóstenes para encontrar números primos entre 2 e 10000.

## Objetivo

Treinar lógica de programação e otimização de algoritmos.

## Tecnologias utilizadas

- Python

## Como funciona

1. Cria uma lista onde todos os números começam marcados como `True`.
2. Os números `0` e `1` são marcados como `False`.
3. O programa percorre os números de `2` até `10000`.
4. Quando encontra um número primo, marca seus múltiplos como `False`.
5. Ao final, exibe apenas os números primos.

## Algoritmo utilizado

O projeto utiliza o algoritmo **Crivo de Eratóstenes**, conhecido por sua eficiência na busca de números primos.

## Exemplo de saída

```bash
2
3
5
7
11
13
17
19
23
29
```