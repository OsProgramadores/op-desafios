## Lógica do código
- Primeiro o código verifica se foi passado um arquivo e se o caminho é válido.
- Lê o arquivo linha por linha e em cada linha:
  - Verifica se possui linha vazia e ignora se tiver;
  - Divide pelo caractere / para separar numerador e denominador;
  - Verifica se só tiver numerador, considera denominador = 1;
  - Converte para int;
  - Se o denominador for 0, imprime "ERR";
  - Calcula o MDC para simplificar a fração;
  - E imprime a fração simplificada no formato:
    - inteiro, se denominador = 1;
    - número misto, se numerador > denominador;
     - fração própria, se numerador < denominador.

## Versão que usei:
- Java 22 (JDK 22).

## Como executar  código:

```
javac Fracoes.java
```
- Para compilar o código.

```
java Fracoes "caminho-absoluto do arquivo"
```
  - Para executar.
