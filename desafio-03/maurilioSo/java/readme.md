# README - Programa de Números Palíndromos

## Descrição

Este programa em Java tem como objetivo identificar e imprimir todos os **números palíndromos** entre 0 e 100.000. Um número palíndromo é aquele que pode ser lido da mesma forma da esquerda para a direita ou da direita para a esquerda, como por exemplo, os números `121` e `333`.

## Estrutura do Código

O código está estruturado em duas partes principais:
1. **Laço de repetição**: que percorre todos os números entre 0 e 100.000.
2. **Função `ehPalindromico`**: que verifica se um número é palíndromo.

### Explicação do Código

#### Método `main`

O método `main` é o ponto de entrada do programa e tem a seguinte funcionalidade:
1. **Laço `for`**: O laço percorre todos os números inteiros entre 0 e 100.000.
   - A cada iteração, o número `i` é verificado para saber se é um número palíndromo.
   
2. **Chamada para `ehPalindromico(i)`**: Para cada número `i`, o programa chama o método `ehPalindromico` para verificar se o número é palíndromo.

3. **Impressão dos números palíndromos**: Se o número for palíndromo, ele é impresso no console utilizando o `System.out.println(i)`.

#### Função `ehPalindromico(int num)`

Este método verifica se o número passado como parâmetro (`num`) é palíndromo ou não. A função realiza os seguintes passos:

1. **Checagem de número negativo**: Se o número for negativo, a função retorna `false`, pois, por convenção, números negativos não são considerados palíndromos.

2. **Inversão do número**:
   - O número original é guardado em uma variável `numeroOriginal` para comparação final.
   - Em seguida, um laço `while` é utilizado para inverter os dígitos do número:
     - A cada iteração, o último dígito de `num` é extraído utilizando a operação `num % 10` e armazenado em `resto`.
     - O número invertido é construído ao multiplicar o valor atual de `numeroInvertido` por 10 e somar o `resto`.
     - O número `num` é reduzido (dividido por 10) a cada iteração até que não sobre mais dígitos.

3. **Comparação com o número original**: Após a inversão do número, o número original (`numeroOriginal`) é comparado com o número invertido (`numeroInvertido`).
   - Se os dois números forem iguais, o número é palíndromo e o método retorna `true`.
   - Caso contrário, retorna `false`.

### Exemplo de Execução

Quando o programa é executado, ele percorre os números de 0 a 100.000 e imprime os números palíndromos encontrados nesse intervalo.

Exemplo de saída (parte da execução):

```
0
1
2
3
4
...
101
111
121
333
...
```

### Como Executar

1. **Pré-requisitos**: É necessário ter o JDK (Java Development Kit) instalado em seu sistema.
2. **Compilação**: Compile o código utilizando o comando:
   ```
   javac NumerosPalindromicos.java
   ```
3. **Execução**: Execute o programa com o comando:
   ```
   java NumerosPalindromicos
   ```

### Explicação das Funções

1. **Função `main`**:
   - A função principal que percorre os números e imprime os palíndromos.
   
2. **Função `ehPalindromico`**:
   - Verifica se um número é palíndromo, retornando `true` ou `false`.

### Complexidade

- **Tempo**: A complexidade temporal do programa é O(n * d), onde:
  - `n` é o número de números no intervalo (100.000).
  - `d` é o número de dígitos do maior número no intervalo (aproximadamente 6 dígitos no caso de 100.000).
  Portanto, o programa executa em tempo linear em relação ao número de números no intervalo, multiplicado pelo número de dígitos em cada número.

- **Espaço**: A complexidade espacial é O(1), pois o programa utiliza uma quantidade constante de memória adicional para armazenar variáveis temporárias.

## Conclusão

Esse programa oferece uma forma simples e eficiente de identificar números palíndromos em um intervalo específico. Ele pode ser facilmente modificado para atender a outros intervalos ou para utilizar diferentes critérios para considerar números como palíndromos.