
## Lógica do código
- O código recebe um arquivo por linha de comando. E verifica se foi passado um caminho e se o arquivo existe.

- Depois, em cada linha desse arquivo, ele faz o processo de:

    - separar a linha em partes para identificar o arquivo de regras e a fita de entrada;

    - carregar as regras do arquivo indicado e armazenar em uma estrutura de mapas, guardando também a posição de cada regra, pois caso ocorra um empate entre duas regras possíveis, a regra com a menor posição é a escolhida;

    - criar a fita com a palavra de entrada, onde cada caractere representa um símbolo inicial.

- Em seguida, inicia a execução da Máquina de Turing:

    - lê o símbolo atual da fita;

    - procura a regra correspondente ao estado atual e ao símbolo lido. E caso não exista uma regra exata, o programa tenta aplicar regras genéricas utilizando o coringa(*), que pode representar qualquer estado ou qualquer símbolo. E se nenhuma regra for encontrada ele retorna "ERR";

    - Depois, substitui o símbolo da fita para o símbolo novo, move a cabeça de leitura/escrita para a direção informada na fita e atualiza o estado;

    - O programa continua até que o estado inicie com "halt".

- No final, a fita processada é exibida no formato: nomeDoArquivoDeRegras, fitaEntrada, fitaSaida.


## Versão que usei
- Java 21 (JDK 21).

## Como executar o código

- Para compilar o código execute o comando abaixo:

  ```
  javac MaquinaTuring.java
  ```
- Para executar o código, utilize o seguinte comando:
  ```
  java MaquinaTuring <caminho-absoluto>/datafile
  ```
