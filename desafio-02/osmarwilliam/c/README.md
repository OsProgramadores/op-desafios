Como compilar e testar arquivos em C?
- instale o compilador GCC
    *   Ambiente linux: em praticamente todas distros o compilador GCC já está presente, verifique no terminal.
        ```
            gcc --version
        ```
    *   Ambiente Windows: pouco mais trabalhoso e manual.
        1) Faça download do MinGW (pelo sourceforge.net)
        2) Faça a instalação:
            *   Importante, lembre-se de instalar o mingw32-base na aba de packages em seguida clique em "installation --> Apply Changes"
            *   Copie o endereço da subpasta bin geralmente encontrada em C:\mingw64\bin
        3) Crie uma nova variável de ambiente: pesquise na Barra de Início por "variáveis de ambiente" e abra, marque a opção "Path" e clique no botão "Editar", após isso clique em "Novo" e cole o endereço do caminho: C:\mingw64\bin
- Compilando
    *   Entre no devido diretório, onde está contido o arquivo que irá ser compilado:
        ```
            ~/op-desafios/desafio-02/osmarwilliam/c
        ```
    *   Execute o comando ls no terminal, tenha certeza que o arquivo está presente.
    *   Digite o seguinte comando no terminal para gerar um arquivo executável: gcc -o [nome para o arquivo executável] [arquivo com *.c]
        ```
            gcc -o numPrimos numPrimos.c
        ```
    *   Para executar:
        ```
            ./numPrimos
        ```