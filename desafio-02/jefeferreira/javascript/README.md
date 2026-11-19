Escrita

# Crivo de Eratóstenes em JavaScript

## 📌 Descrição

Este projeto implementa o **Crivo de Eratóstenes**, um algoritmo utilizado para encontrar todos os números primos até um determinado limite.

O algoritmo identifica os números primos eliminando seus múltiplos, que são classificados como números não primos.

## ⚙️ Como funciona?

1. Cria um array para armazenar os números primos encontrados.
2. Cria um segundo array para marcar os números que não são primos.
3. Percorre os números a partir de 2 até o limite informado.
4. Quando encontra um número que ainda não foi marcado como não primo, adiciona esse número à lista de primos.
5. Marca todos os múltiplos desse número, começando pelo seu quadrado, como não primos.
6. Ao final, retorna a lista de números primos encontrados.

## 💻 Exemplo de uso

javascript

```javascript
const primos = crivo(10000);

console.log(primos.join(", "));
```

Nesse exemplo, o algoritmo encontra todos os números primos de 2 até 10.000 e imprime os resultados no console, separados por vírgula.

## 🚀 Como executar

1. Tenha o Node.js instalado.
2. Salve o código em um arquivo chamado `crivo.js`.
3. Execute o comando no terminal:

bash

```bash
node crivo.js
```

## 📊 Complexidade

- **Tempo:** O(n log log n), sendo n o limite informado.
- **Espaço:** O(n), pois utiliza arrays para armazenar os números e suas marcações.

## 🎯 Objetivo

Demonstrar a aplicação do Crivo de Eratóstenes utilizando JavaScript, explorando estruturas de repetição, arrays e lógica de programação para encontrar números primos de maneira eficiente.