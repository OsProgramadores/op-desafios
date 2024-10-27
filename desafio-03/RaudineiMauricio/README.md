## Entendimento do desafio03.
#Neste desafio, a idéia é imprimir todos os números palindrômicos entre dois outros números.
#Tal como as palavras, os números palindrômicos mantém o mesmo valor se lidos de trás para a frente.
#Observe que o número inicial e final devem ser incluídos nos resultados, caso também sejam palíndromos.

**Para o desafio, assuma:**
Apenas inteiros positivos podem ser usados como limites.
Números de um algarismo são palíndromos por definição.
Máximo número: (1 << 64) - 1 (máximo unsigned int de 64 bits).

## limite_max = (1 << 64) - 1 

. Utiliza operações de bitwise (bit a bit) para calcular o maior número inteiro que pode ser representado com 64 bits.
. O operador << é o operador de deslocamento à esquerda. Ele desloca os bits do número 1 para a esquerda por 64 posições.
. Isso é equivalente a multiplicar 1 por 2^64, resultando em 18446744073709551616.
. O resultado 18446744073709551615 é o maior número que pode ser representado em um inteiro sem sinal de 64 bits (unsigned int). Isso significa que, ao trabalhar com números dentro desse limite, você pode garantir que eles não excedam o espaço que pode ser alocado para armazená-los em um sistema que utiliza inteiros de 64 bits.


# Passos para Execução
1 - O usuário fornece o número inicial e final.
2 - Itera sobre cada número no intervalo.
3 - Usando um while, o número é invertido e armazenado na variável palindromo.
4 - Se o número original for igual ao número invertido, ele é um palíndromo e é impresso.


### Pré-requisitos para executar esse código.
- **Python 3.x** instalado no sistema.
- Verifique no seu terminal se o python está instalado usando o comando: python --version
- Abra a pasta do arquivo.
- Digite o Código no no vscode ou na Sua IDE, não copiei pois digitando voçê aprende, e execute.

