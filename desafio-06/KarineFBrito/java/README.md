 - O programa pede para o usuário que digite uma expressão, depois remove os espaços em branco e converte a expressão para letras maiúsculas. Também verifica se a expressão contém apenas letras. Se não, exibe uma mensagem de erro. As palavras válidas são lidas a partir de um arquivo de texto (words.txt) pelo comando File. E o programa usa o "arquivoScanner.hasNextLine()" para percorrer cada linha do arquivo e armazena as palavras em uma lista.  Se o arquivo não for encontrado, o programa imprime uma mensagem e finaliza.
  No código temos duas funções principais que são:
  -permutar (gera todas as permutações possíveis de uma string) e para cada permutação gerada, verifica se ela está na lista de palavras válidas. Se sim, adiciona ao conjunto de anagramas.
  -trocarPosição (troca dois caracteres na string).  Depois de gerar os anagramas, o programa exibe a lista ordenada dos anagramas encontrados. Se nenhum anagrama válido for encontrado, uma mensagem é exibida. 

  - A versão que usei foi java 22.

  - Para executar o código é preciso que baixe o arquivo words.txt com as palavras válidas e atualize o caminho do arquivo no código no comando:
  "new File("C:\\Users\\Karin\\Downloads\\words.txt");"
  Depois é só usar os comandos:
  -Javac Anagrama.java - que compila o código;
  -java Anagrama - executa o código.
