# Desafio 06 em Java

## Configurações de Ambiente
1. Deve-se ter instalado uma versão do Java igual ou superior a **11.0**.
2. Baixar o arquivo de palavras válidas na página do desafio no site.
3. Definir a variável de ambiente `CAMINHO_PALAVRAS_VALIDAS` como o caminho absoluto para o arquivo de palavras válidas, utilizando o seguinte comando:
```sh
$ export CAMINHO_PALAVRAS_VALIDAS=\path-para-arquivo\words.txt
```

## Compilando e Executando
1. Entrar na raiz da pasta com o desafio e rodar o comando `mvn clean package`. É necessário ter instalado pelo menos a versão 3 do Maven.
2. Rodar o comando para executar o programa:
```sh
java -Xmx[tamanho-maximo-heap-em-giga] -Xmx[tamanho-minimo-heap-em-giga] -jar target/Desafio6-2-0.jar [lista-de-palavras]
```
3. Para strings com o tamanho sugerido no desafio de 16 caracteres, como `ICONIC PANAMA GARB`, recomenda-se uma heap de pelo menos 7G.

---

## Detalhes implementação
### Versão 1
Primeira tentativa, utilizando apenas as bibliotecas padrões do Java, sem utilizar multicore.

### Versão 2
- Utiliza-se a `Eclipse Collections API`, que possui implementações mais performáticas para se trabalhar com valores primitivos, como `char` e `int`.
- Adicionou-se o processamento em multithread através da API do `ForkJoinPool` e `ExecutorService`
- Utilizou-se o `BufferedOutputWriter` no lugar do `System.out.println` para se printar os anagramas no terminal em batch e reduzir a quantidade de `I\O` utilizada.