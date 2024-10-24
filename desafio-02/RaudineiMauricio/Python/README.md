## Desafio02/RaudnieiMauricio/Python

## Crivo de Eratóstenes – Implementação em Python

## Descrição
O **Crivo de Eratóstenes** é um algoritmo eficiente para encontrar todos os números primos até um certo limite. Ele elimina múltiplos de números primos, deixando apenas os próprios primos na lista. Este método é muito mais rápido do que verificar número a número, tornando-se ideal para encontrar muitos primos de uma vez.

---

## Como o Crivo de Eratóstenes Funciona?
1. Crie uma lista de números marcados como primos (inicialmente, todos são assumidos como primos).
2. Comece com o número 2 (o menor número primo).
3. Marque como não primos todos os múltiplos de 2, exceto ele mesmo.
4. Avance para o próximo número ainda marcado como primo e repita o processo para seus múltiplos.
4. Continue até que todos os números da Raiz quadrada de n tenham sido processados.

## Explicação do Código

1. Lista de primos: Criamos uma lista onde todos os números são inicialmente marcados como True (primos).
2. Marcar não primos: Para cada número primo, marcamos seus múltiplos como False (não primos).
3. Filtrar primos: No final, retornamos apenas os números que ainda estão marcados como True.
---

## Vantagens
Rápido e eficiente para encontrar primos em grandes intervalos.
Fácil de entender e implementar.

## Limitações
. Requer mais memória para armazenar a lista de primos.
. Pode não ser ideal para intervalos muito grandes (como bilhões) sem otimizações adicionais.


## 🛠 Pré-requisitos
- **Python 3.x** instalado no sistema.




