# Os Programadores - Desafio 05 - Implementação em Java

Implementação em **Java** para o [Desafio 05](https://osprogramadores.com/desafios/d05/) do grupo [OsProgramadores](https://osprogramadores.com/). Os arquivos utilizados no desafio, bem como os gráficos de desempenho podem ser verificados [aqui](http://bcampos.com/Graphs.php)

Essa implementação utiliza o [Gradle](https://gradle.org/) como ferramenta de build e gestão de dependências. O único pré-requisito é que esteja disponível o Java JDK versão 8 ou superior.

## Guia de Uso

### Comandos Gradle

- `./gradlew clean`: Remove todos artefatos do projeto
- `./gradlew eclipse`: Gera a configuração do projeto para ser importado no Eclipse
- `./gradlew fatJar`: Gera o jar executável na pasta `build/libs` com o nome `op-d05-java-all-x.y.jar`

### Execução

- `java -jar op-d05-java-all-x.y.jar <nome-arquivo>`

## Histórico de Versões

### v0.4

- Alteração do parser para usar [Jsoniter](https://jsoniter.com/)
- Atualização do Gradle Wrapper para versão 5.1.1

### v0.3

- Alteração do parser para usar [Jackson](https://github.com/FasterXML/jackson)
- Melhora de 25% (aproximadamente)

### v0.2

- Padronização do arquivo de saída de acordo com o definido no desafio

### v0.1

- Versão inicial utilizando [gson](https://github.com/google/gson)
