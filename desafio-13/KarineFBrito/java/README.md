## Lógica do código

- O código recebe uma casa inicial (ex: "a1") via argumento de linha de comando e verifica se ela foi fornecida.

- Um tabuleiro de 8 x 8  é inicializado com o valor -1, indicando que nenhuma casa foi visitada ainda.

- O programa utiliza o Algoritimo de Warnsdorff para encontrar o caminho do cavalo. Onde, a cada passo, o cavalo deve se mover para a casa que possui o menor número de movimentos subsequentes possíveis.
- O cavalo começa na posição fornecida e marca essa casa com o número 0 (primeiro passo).

- Para cada um dos 63 movimentos restantes, o programa avalia as 8 direções possíveis de um cavalo (movimentos em "L").

- A função validando garante que o cavalo não saia dos limites do tabuleiro e não retorne a uma casa já visitada.

- A função contarSaidasVazias calcula o "grau" de cada movimento válido, ou seja, quantas casas livres estão acessíveis a partir daquele próximo ponto.

- Para que o algoritmo processe os movimentos corretamente, o sistema realiza uma conversão de sistemas de coordenadas, transformando a notação algébrica (ex: a1, h8) em índices numéricos de uma matriz 8 x 8.

- O programa escolhe a próxima casa com o menor grau (menor número de saídas). Isso ajuda a evitar que o cavalo fique preso em "becos sem saída" nas bordas do tabuleiro precocemente.

- Se o programa não encontrar mais movimentos válidos antes de completar 64 casas, ele interrompe a execução.

- A cada movimento decidido, a posição é convertida de volta para a notação algébrica (ex: "b3") pela função converterParaAlgebrica e armazenada em uma lista.

- Ao final do processo, o programa imprime a sequência completa de casas visitadas, uma por linha, representando o percurso do cavalo.

## Versão que usei

- Java 21 (JDK 21).

## Como executar o código

- Para compilar o código execute o comando abaixo:

  ```
  javac PasseioDoCavalo.java
  ```
- Para executar o código, utilize o seguinte comando:
  ```
  java  PasseioDoCavalo <posicao-inicial>
  ```

## Referências

- Heurística de Warnsdorff - Wikipedia: https://en.wikipedia.org/wiki/Knight%27s_tour#Warnsdorff's_rule
- Algoritmo de Warnsdorff - GeeksforGeeks: https://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/