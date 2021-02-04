# Solução em Java e Antlr4
Esta solução utiliza a gramática do Antlr4 para interpretar e parsear as expressões numéricas enviadas
além de um visitor para percorrer a árvore gerada pelo Antlr e efetuar as operações necessárias a 
serem executadas.  

- Requisitos para se compilar e rodar o projeto:
    - Java 11+
    - Maven 3.6+
- Compilando e rodando o projeto:
    - Entrar na pasta root do projeto(onde está localizado este arquivo README)
    - Rodar o comando `mvn clean package -DskipTests`
    - Rodar o comando `java -jar target/desafio-14-1.0.jar [path-para-o-arquivo]`