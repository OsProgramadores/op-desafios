# op-desafios/desafio-12

## Potências de 2

Este desafio consiste em:

Ler um arquivo de números, contendo um número por linha.
Se o número for uma potência de 2, imprimir o número seguido de true e o expoente ao qual se deve elevar 2 para obter o número.
Se o número não for uma potência de 2, imprimir o número seguido de false.

### Exemplo
Considere a lista de números:
```
1
140
128
137
65535
65536
17179869184
```
A saída deverá ser:
```
1 true 0
140 false
128 true 7
137 false
65535 false
65536 true 16
17179869184 true 34
```

> Execute da seguinte forma:
```
$ elixir power_of_two.exs
```
