# Desafio #2 - Primos

Implementando o algoritmo **Crivo de Eratóstenes** para encontrar todos os números primos até um determinado limite

O algoritmo identifica os números primos eliminando seus múltiplos, que são classificados como números não primos

## Lógica utilizada para solucionar o desafio

1. Criamos um array chamado `primos` para guardar os números primos encontrados
2. Criamos outro array chamado `numNaoPrimos` para marcar os números que não são primos
3. Percorremos os números de 2 até o limite
4. Se o número ainda não foi marcado, significa que ele é primo, então adicionamos o número ao array `primos`
5. Percorremos os múltiplos desse número, começando pelo seu quadrado, e marcamos todos como não primos
6. Retornamos o array com todos os números primos encontrados

## Como rodar o código

1. Ter o Node.js instalado
3. Execute o comando no terminal

```bash
node primos.js
```
