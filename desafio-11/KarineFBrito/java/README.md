## Lógica do código

- O código recebe um arquivo por linha de comando e verifica se foi passado um caminho válido e se o arquivo existe.

- O método processarLinha utiliza uma Expressão Regular para extrair e concatenar todos os dígitos numéricos do arquivo na string estática global piDecimais, ignorando pontuações, espaços e caracteres não numéricos.

- O método preCalcularPrimos executa o Crivo de Eratóstenes, um algoritmo antigo para encontrar todos os números primos até um determinado limite. Os números primos são guardados em uma estrutura de dados especial (HashSet) que permite ao programa verificar se um número é primo.

- O método encontrarSequenciaMaisLonga percorre os dígitos de π (piDecimais). Ele usa o array auxiliar comprimentoMax para rastrear o maior comprimento válido de uma subsequência que termina em cada posição (i). Para cada posição final, o método verifica todas as substrings de até 4 dígitos que terminam ali. Se a substring for um número primo (ehPrimo), o algoritmo tenta estender a melhor subsequência encontrada até o ponto inicial desse primo, atualizando comprimentoMax[i] se a nova combinação for mais longa. O array indiceAnterior armazena o ponto de partida ideal do primo anterior, funcionando como um "ponteiro" para a reconstrução.

- O método reconstruirSequencia é o responsável por montar a solução final. Ele utiliza o array indiceAnterior para refazer o caminho da solução ótima encontrada no passo anterior. Começando pela posição final (fimDaSequencia) onde o maior comprimento foi atingido, o método retrocede iterativamente:

  - Encontra o Primo: Usa indiceAnterior para determinar o início do último número primo na sequência.

  - Adiciona e Reverte: Extrai o primo de piDecimais e o insere no início do StringBuilder (sequenciaCompleta) para garantir que a ordem dos primos na sequência final esteja correta.

  - Avança: Define atual para inicio, movendo o processo para o próximo primo anterior, e repete até que o índice anterior seja -1, indicando que toda a subsequência foi reconstruída.

## Versão que usei

- Java 21 (JDK 21).

## Como executar o código

- Para compilar o código execute o comando abaixo:

  ```
  javac PrimoPi.java
  ```
- Para executar o código, utilize o seguinte comando:
  ```
  java PrimoPi <caminho-absoluto>
  ```
