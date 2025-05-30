 - O programa pede para o usuário que digite uma expressão, depois remove os espaços em branco e converte a expressão para letras maiúsculas. Também verifica se a expressão contém apenas letras. Se não, exibe uma mensagem de erro. As palavras válidas são lidas a partir de um arquivo de texto (words.txt) pelo comando File. E o programa usa o "arquivoScanner.hasNextLine()" para percorrer cada linha do arquivo e armazena as palavras em uma lista.  Se o arquivo não for encontrado, o programa imprime uma mensagem e finaliza.
  No código temos quatro funções:
  -permutar: que gera todos os anagramas da expressão;
  -verificar: ele subtrai a quantodade de letras da expressão e da palavra, e atualiza o conjunto de letras restantes ao usar uma palavra;
  -cabe: ele verifica se a palavra cabe dentro da expressão;
  -contarLetras: ele conta quantas vezes cada letra aparece na string.

  - A versão que usei foi java 22.

  - Para executar o código:
   -Baixe o arquivo words.txt com as palavras válidas
   No terminal:
  -Javac Anagrama.java - compila o código;
  - Informe o caminho para o arquivo (o comando depende do sistema operacional):
    -Linux/macOS:
    export CAMINHO="/caminho/para/o/arquivo/words.txt"
    -Windows (cmd.exe):
    set CAMINHO=C:\caminho\para\o\arquivo\words.txt
    -Windows (PowerShell):
    $env:CAMINHO="C:\caminho\para\o\arquivo\words.txt"
  -java Anagrama - executa o código.
