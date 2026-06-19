# Anagramas

Esse programa recebe do usuário uma palavra ou frase qualquer e, dentre uma lista de
palavras, faz todos os anagramas possíveis da palavra ou frase fornecida.

Anagrama é um rearranjo de palavras, tal palavra é anagrama de outra se possuir
as mesmas letras, porém em ordem diferentes.

Importante ressaltar que esse algoritmo não considera espaços e uma anagrama não pode ser formado por palavras iguais.

# Como funciona

1. Com a palavra fornecida pelo usuário, é criado um "estoque" de letras contidas na String, ou seja, a quantidade de cada letra na palavra
2. Após isso, é percorrido todo o arquivo de palavras e são selecionadas aquelas que cabem no estoque da palavra escolhida, essas entram no dicionário
3. Depois, usando recursividade, os anagramas são procurados
4. Para cada palavra do dicionário é verificado se ela cabe no estoque da palavra, se sim adiciona ela em uma lista
5. Depois parte para a próxima do dicionário, adiciona na lista e verifica novamente o estoque
6. Se não tiver estoque, a última palavra da lista é removida e repete o processo
7. Se o estoque chegar em 0, significa que o anagrama foi encontrado
8. Printa o anagrama na tela

# Tecnologias utilizadas

Linguagem: Java 11+

# Execução

Para rodar o programa, basta seguir os seguintes passos

1. Esteja no diretório onde a classe se encontra
2. É importante que o arquivo com as palavras esteja no mesmo diretório, se chame `words.txt` e que possua uma palavra por linha
3. Rode no terminal:
```bash
$ java MeuPrograma.java palavra
```
# Saída

Ao executar o programa você verá uma lista dos possíveis anagramas

Ex.:
```
$ java MeuPrograma.java anagrama
```
```java
A AM AN RAG
A AMRA NAG
A AN MA RAG
A ANAGRAM
A MANA RAG
AM ANA RAG
ANA MA RAG