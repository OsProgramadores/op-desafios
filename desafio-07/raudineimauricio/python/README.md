### Problema com Quebras de Linha (CRLF vs LF)

O meu programa estava lendo e processando arquivos no formato Unix (usando apenas `LF` para quebra de linha). No entanto, como uso o programa em um sistema Windows, a saída padrão do terminal estava sendo gerada com quebras de linha no formato **CRLF** (`\r\n`), que é o padrão no Windows.

Isso causou um problema ao calcular o hash MD5 da saída gerada, já que o MD5 é sensível a qualquer diferença nos dados. Como a saída estava incluindo **caracteres extras** (`\r`), o hash MD5 gerado não batia com o do arquivo original.

### Solução

Para corrigir esse problema, fiz essa alteracão no código:

1. **Remoção do Carriage Return (`\r`)**:
   No código Python, fiz com  que a saída do programa não tivesse caracteres de
   **Carriage Return** (`\r`), mantendo apenas o **Line Feed** (`\n`), que é o padrão no formato Unix e esperado pelo Git Bash.

   usei o comando:

   linha = linha.replace(b'\r', b'')


# Programa `tac` - Leitura Invertida de Arquivos e calculo de hash.

# Descrição

O programa lê um arquivo e imprime seu conteúdo da última linha para a primeira. Ele foi desenvolvido em Python, e pode ser usado para ler arquivos grandes de forma eficiente, processando-os em blocos de até 4096 bytes (ajuste se necessário).

# USO

Para usar o programa, basta rodar o comando abaixo no terminal, fornecendo o caminho para o arquivo que você deseja processar.

python main.py [ARQUIVO] | md5sum

# Necessário (Python 3) ou superior.

Instale o Python e abra o terminal de comando em sua máquina e digite o comando python --version. O comando deverá informar a versão atual do interpretador de Python caso o download tenha sido feito corretamente. -se de possuir uma versão igual ou superior à 3.10, caso contrário, o código não funcionará.