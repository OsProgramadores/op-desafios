# DevJunr - Solução para o Desafio #06

Para visualizar informações sobre o desafio, [clique aqui](https://osprogramadores.com/desafios/d06/)

---

### O problema

```txt
    - Escreva um programa na sua linguagem e bibliotecas preferidas que:
    - Leia a expressão (que pode ser uma frase ou apenas uma palavra) a ser usada para a criação dos anagramas da linha de comando. Apenas as letras de “A” a “Z” deverão ser consideradas (ignore espaços e converta todas as letras minúsculas para maíusculas). Retorne erro e aborte a execução se caracteres inválidos forem encontrados na expressão (qualquer caracter não alfabético que não seja espaço, incluindo números, pontuação, ou caracteres acentuados).
    - Leia uma lista de palavras válidas do arquivo words.txt (Download). O arquivo é formatado com uma palavra por linha, com palavras da língua inglesa (Nota: apesar de várias tentativas, o autor não conseguiu achar uma lista “limpa” de palavras da língua portuguesa).
    - Imprima todas as combinações possíveis de anagramas (sem repetição de linhas ou palavras). Os anagramas devem conter apenas palavras válidas (lidas do arquivo acima).
    - O formato de saída deve conter múltiplas linhas (uma por anagrama), com as palavras ordenadas alfabeticamente dentro de cada linha (veja exemplos abaixo).
    - O programa deve ser capaz de calcular e imprimir a lista de anagramas possíveis para uma expressão de até 16 caracteres em menos de 60 segundos.
```

Quando concluído, o código deverá ser capaz de gerar anagramas validos, tendo como base a palavra ou frase passada pelo usuário, validando as mesmas de acordo com o dicionario de palavras do desafio. Se a palavra/frase passada pelo usuário, for anagrama de uma das palavras do dicionario, a palavra será exibida.

### Tecnologia usada
[![tecnologias usadas](https://skillicons.dev/icons?i=java)](https://skillicons.dev)


### Execução
Para rodar o código você deve ter em seu PC:
1. Java JVM
2. Arquivo words.txt - [clique aqui para baixar](https://osprogramadores.com/desafios/d06/words.txt)

Faça o download do código e dicionario de palavras, insira os mesmos no diretorio que deseja. <b>Adicione o arquivo 'words.txt' no mesmo diretorio do arquivo 'Anagrama.java'</b>
a

Para rodar o código use o comando

```bash
java Anagrama.java <palavra ou expressão>
```

Em ```bash<palavra ou expressão>```, substitua por uma palavra ou uma frase, o programa irá trazer anagramas com as palavras do arquivo words.txt, de acordo com o que você passar como argumento na execução.

### Exemplo de execução
```bash
java Anagrama.java programa
A ARGO RPM
A PROM RAG
A RAG ROMP
AM GAP ORR
AM GO PARR
AM PRO RAG
AMP OR RAG
ARGO PRAM
ARGO RAMP
ARM GAP OR
ARM GO PAR
ARM GO RAP
GAP MA ORR
GAP MAR OR
GAP OR RAM
GO MA PARR
GO MAR PAR
GO MAR RAP
GO PAR RAM
GO RAM RAP
MA PRO RAG
MAP OR RAG
MARGO PAR
MARGO RAP
OR PAM RAG
```

```bash
java Anagrama.java brasil
IRS LAB
LAB SIR
```

### Funcionamento do código
O código foi escrito inteiramente em java, com openjdk version "17.0.13" 2024-10-15

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.util.*;
```
O código começa importando algumas bibliotecas para o tratamento de exceções e para a leitura de arquivos, além de importar todo o pacote java.util

```java
public class Anagrama {

  public static void main(String[] args) {
```
Posteriormente é criada uma classe pública chamada Anagrama, e após, um método chamado de main, que também é responsavel por coletar os argumentos passado na execução. Onde se tem ```String[] args``` , especifica que o main irá receber um array de string, possibilitando passar palavras e frases como argumento na execução.

```java
Scanner sc = new Scanner(System.in);
ArrayList<String> argList = new ArrayList<>();
for (String arg : args) {
  argList.add(arg);
}
```
Aqui é instanciado um objeto scanner chamado de sc, será o responsavel por coletar entradas. Passando para a proxima linha, temos a criação de um arraylist de strings, chamado argList, o mesmo será responsavel por armazenar todas as palavras passadas no argumento da execução. Próxima linha: Temos a criação de um foreach, onde percorre todos os argumentos passado na execução, e adiciona as palavras no array argList.

```java
String expressaoCombinacao = String.join("", argList);
String expressao = expressaoCombinacao.toUpperCase();
validaEntrada(expressao);
```
Aqui é criado duas strings, uma para juntar todas as palavras do array argList em um único lugar, sem ser separado por espaço, então algo como: [Oi brasil] convertido ficaria OIBRASIL, dentro de uma string.
A segunda linha serve para adicionar toda a string em caixa alta.
```java
validaEntrada(expressao);
```
a função validaEntrada, irá verificar se o argumento passado na execução possui números, simbolos, ou outro caractere, se sim: Para o programa e exibe uma mensagem de erro, pois o mesmo só aceita palavras de A a Z, sem simbolos.

```java
Set<String> palavrasValidas = null;
    try {
      palavrasValidas = carregarPalavrasValidas("words.txt");
    } catch (NoSuchFileException e) {
      System.out.println(
          "❯ Erro ao carregar o arquivo 'words.txt' . Garanta que o arquivo 'words.txt' esteja no"
              + " mesmo diretório do arquivo 'Anagrama.java'");
      System.exit(1);
    } catch (Exception e) {
      System.out.println("❯ Erro: " + e);
      System.exit(1);
    }
```
Esse bloco é responsavel por fazer a leitura do arquivo words.txt

```java
    Set<String> anagramas = gerarAnagramas(expressao, palavrasValidas);
    List<String> sortedAnagramas = new ArrayList<>(anagramas);
    Collections.sort(sortedAnagramas);
    for (String anagrama : sortedAnagramas) {
      System.out.println(anagrama);
    }
    sc.close();
  }

  public static void validaEntrada(String entrada) {
    if (!entrada.matches("[A-Z]+")) {
      System.out.println("> Entrada inválida. Digite apenas letras de A a Z, sem simbolos.");
      System.exit(1);
    }
  }
```
Esse trecho de código gera anagramas a partir de uma expressão dada, ordena esses anagramas e os imprime no console, garantindo que não haja duplicatas e que a saída seja organizada. Além disso, ele fecha o objeto Scanner para liberar recursos. Após isso, a criação do método validaEntrada é exibido, onde se entrada tiver diferente de A a Z, mostra: Entrada inválida. Digite apenas letras de A a Z, sem simbolos, e fecha o programa com system.exit(1)

```java
  public static Set<String> carregarPalavrasValidas(String arquivo) throws IOException {
    Set<String> palavrasValidas = new HashSet<>();
    List<String> linhas = Files.readAllLines(Paths.get(arquivo));
    for (String linha : linhas) {
      linha = linha.trim().toUpperCase();
      if (linha.matches("[A-Z]+")) {
        palavrasValidas.add(linha);
      }
    }
    return palavrasValidas;
  }

  public static Set<String> gerarAnagramas(String expressao, Set<String> palavrasValidas) {
    Set<String> resultados = new HashSet<>();
    List<String> listaLetras = Arrays.asList(expressao.split(""));
    gerarCombinacoes(listaLetras, palavrasValidas, new ArrayList<>(), resultados);
    return resultados;
  }

  private static void gerarCombinacoes(
      List<String> letrasRestantes,
      Set<String> palavrasValidas,
      List<String> combinacaoAtual,
      Set<String> resultados) {
    if (letrasRestantes.isEmpty()) {
      List<String> combinacaoOrdenada = new ArrayList<>(combinacaoAtual);
      Collections.sort(combinacaoOrdenada);
      String anagrama = String.join(" ", combinacaoOrdenada);
      resultados.add(anagrama);
      return;
    }

    for (int i = 1; i <= letrasRestantes.size(); i++) {
      List<String> permutacoes = permutar(letrasRestantes, i);
      for (String perm : permutacoes) {
        if (palavrasValidas.contains(perm)) {
          List<String> novasLetras = new ArrayList<>(letrasRestantes);
          for (char c : perm.toCharArray()) {
            novasLetras.remove(String.valueOf(c));
          }
          List<String> novaCombinacao = new ArrayList<>(combinacaoAtual);
          novaCombinacao.add(perm);
          gerarCombinacoes(novasLetras, palavrasValidas, novaCombinacao, resultados);
        }
      }
    }
  }
```
Essa parte é a responsável por carregar as palavras validas contida no dicionario (words.txt), gerar os anagramas,e gerar as combinações.

```java
public static List<String> permutar(List<String> lista, int tam) {
    List<String> result = new ArrayList<>();
    permutarRecursivo(lista, 0, tam, result);
    return result;
  }

  private static void permutarRecursivo(
      List<String> lista, int index, int tam, List<String> result) {
    if (index == tam) {
      result.add(String.join("", lista.subList(0, tam)));
      return;
    }

    Set<String> permutacoesGeradas = new HashSet<>();
    for (int i = index; i < lista.size(); i++) {
      Collections.swap(lista, i, index);
      String perm = String.join("", lista.subList(0, tam));
      if (!permutacoesGeradas.contains(perm)) {
        permutacoesGeradas.add(perm);
        permutarRecursivo(lista, index + 1, tam, result);
      }
      Collections.swap(lista, i, index);
    }
  }
}
```
A permutação é o ato de "rearranjar", organizar, elementos de uma seleção como um array, de todas as maneiras possíveis. Cada rearranjo é chamado de "permutação. Essa parte do código é responsavel por isso.