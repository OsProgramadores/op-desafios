# Desafio 11 - Primos em Pi

Este desafio consiste em encontrar a sequência mais longa de números primos (entre 2 e 9973) no primeiro 1 milhão de casas decimais de π.

## Solução Do Desafio

Implementação do algoritmo Crivo de Eratóstenes para obter todos os números primos dentro do intervalo do desafio (Primos de 2 a 9973).

Para obter a sequência mais longa foi utilizado conceito de programação dinâmica. O algoritmo percorre as casas decimais de pi de trás para frente, a cada digito é calculado a distância mais longa a partir do mesmo, e salvo em um array como uma "memória", evitando assim que seja necessário percorrer um caminho que já foi calculado antes.

## Versão do Node

Foi testado utilizando a versão mais recente LTS do Node (24.15.0).

## Como rodar o programa

Para rodar o programa basta digitar:

```bash
node main.js "<caminho_do_arquivo>"
```
