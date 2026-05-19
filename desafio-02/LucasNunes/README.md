# Números Primos até 10000

Este programa exibe todos os números primos entre 2 e 10000 utilizando o algoritmo Crivo de Eratóstenes.

## Como funciona

1. Cria uma lista onde todos os números começam marcados como `True`.
2. Os números `0` e `1` são marcados como `False`, pois não são primos.
3. Percorre os números de `2` até `10000`.
4. Se o número atual ainda estiver marcado como `True`, ele é considerado primo.
5. Todos os múltiplos desse número são marcados como `False`.
6. Ao final, são exibidos apenas os números que permaneceram marcados como `True`.