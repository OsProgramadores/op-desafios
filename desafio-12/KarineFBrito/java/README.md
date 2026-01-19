## Lógica do código
- O código recebe um arquivo por linha de comando e verifica se foi passado um caminho válido e se o arquivo existe.
- Após a validação do arquivo, o programa abre o arquivo utilizando a classe Scanner, permitindo a leitura do conteúdo linha por linha.
- Cada linha lida do arquivo é tratada individualmente:
  - Linhas vazias ou contendo apenas espaços em branco são ignoradas.
  - O valor da linha é convertido para um objeto BigInteger, possibilitando o processamento de números muito grandes sem risco de estouro de memória.
- Para cada número lido, o programa verifica se ele é uma potência de 2 utilizando um truque binário, que consiste na expressão:
```
n > 0 && (n & (n - 1)) == 0
```
Essa lógica funciona porque números que são potência de 2 possuem apenas um único bit igual a 1 em sua representação binária.
- Caso o número seja identificado como uma potência de 2 o expoente correspondente é calculado por meio do método bitLength() - 1, que retorna a posição do bit mais significativo. Em seguida o programa imprime o número, o valor true e o expoente encontrado.
- Caso o número não seja uma potência de 2 o programa imprime apenas o número seguido do valor false.
## Versão que usei

- Java 21 (JDK 21).

## Como executar o código

- Para compilar o código execute o comando abaixo:

  ```
  javac Potencia.java
  ```
- Para executar o código, utilize o seguinte comando:
  ```
  java  Potencia <caminho-absoluto>
  ```
