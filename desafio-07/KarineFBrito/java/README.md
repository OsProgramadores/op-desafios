  # Lógica usada no programa:
  - Primeiro, o programa recebe o caminho do arquivo pelos argumentos (args). Em seguida, verifica se o caminho foi informado e se o arquivo é válido. Depois disso, abre o arquivo em modo leitura usando RandomAccessFile, carrega todo o conteúdo em um buffer de bytes e faz a leitura de trás para frente. A cada byte lido, se for uma quebra de linha (\n), considera que uma linha foi completada: reverte os bytes acumulados, converte para String e imprime. Se não for uma quebra de linha nem \r, o byte é adicionado à lista. No final, o programa trata a última linha (caso ela não termine com \n), garantindo que todas as linhas sejam impressas na ordem invertida.

  ## versão que usei:
- Java 22 (JDK 22).

##  Como executar o código:
- Baixe o arquivo de teste (308M);
- Descompacte o arquivo localmente com "gzip -d 1GB.txt.gz";
- javac tac.java - para compilar o código;
- java tac "caminho do arquivo na sua máquina"
