 # Descrição Desafio 6
 - O programa pede para o usuário que digite uma expressão, depois remove os espaços em branco e converte a expressão para letras maiúsculas. Também verifica se a expressão contém apenas letras. Se não, exibe uma mensagem de erro. As palavras válidas são lidas a partir de um arquivo de texto (words.txt) pelo comando File. E o programa usa o "arquivoScanner.hasNextLine()" para percorrer cada linha do arquivo e armazena as palavras em uma lista.  Se o arquivo não for encontrado, o programa imprime uma mensagem e finaliza.


  No código temos cinco métodos:

  - permutar: que gera todos os anagramas da expressão;
  - verificacao: verifica se o anagrama formado possui todas as letras da expressão;
  - verificar: ele subtrai a quantidade de letras da expressão e da palavra, e atualiza o conjunto de letras restantes ao usar uma palavra;
  - cabe: ele verifica se a palavra cabe dentro da expressão;
  - contarLetras: ele conta quantas vezes cada letra aparece na string.


# Configuração

  - A versão que usei foi java 22.

# Executando o Código

   - Baixe o arquivo words.txt com as palavras válidas


   No terminal:
  - `javac Anagrama.java` - compila o código;
  - Informe o caminho para o arquivo (o comando depende do sistema operacional):
    - Linux/macOS:

      `export CAMINHO="/caminho/para/o/arquivo/words.txt"`
    - Windows (cmd.exe):

      `set CAMINHO=C:\caminho\para\o\arquivo\words.txt`
    - Windows (PowerShell):
    `$env:CAMINHO="C:\caminho\para\o\arquivo\words.txt"`
  - `java Anagrama expressao` - executa o código.

  ## Saída:
  ```
java Anagrama vermelho
C:/Users/...
ELM HO REV
ELM HOVER
ELM OH REV
HELM OVER
HELM ROVE
HOLM VEER
LEVER OHM
OHM REVEL
```
```
 java Anagrama oi gente
C:/Users/...
EGO I NET
EGO I TEN
EGO TINE
ENG I TOE
EON GET I
GEE I NOT
GEE I TON
GEE IN TO
GEE INTO
GEE IT NO
GEE IT ON
GEE OINT
GEE TONI
GENE I TO
GENE ITO
GENIE TO
GET I ONE
GINO TEE
GO I TEEN
GO IN TEE
GONE TIE
```
