
# Desafio 3 - Números palindrômicos.

Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado. Um exemplo de palíndromo é a palavra “reviver”.

Neste desafio, a idéia é imprimir todos os números palindrômicos entre dois outros números. Tal como as palavras, os números palindrômicos mantém o mesmo valor se lidos de trás para a frente.


## Stack utilizada

**Back-end:** Java


## Instalação

Faça um clone do repositorio e localize a pasta op-desafios/desafio-03/devjunr/java e rode o código em java com o comando abaixo:

```bash
  java Palindromos.java <valor inicial> <valor final>
```

Passe o valor inicial e o valor final na execuçã do código, substituindo <valor inicial> e <valor final> pelos respectivos números.

Exemplo:

```bash
  java Palindromos.java 1 15
```

## Demonstração

Bash:
```
java Palindromos.java 1 50
```

Saída:

```
__________
Valor Inicial: 1
Valor Final: 50
__________

Resultado:
1
2
3
4
5
6
7
8
9
11
22
33
44
```

## Explicação do Código

O código foi escrito 100% em java. E possui caracteristicas que um iniciante consegue compreender.

```
public class palindromicos {
  public static void main(String[] args) {
    try {
      int valorInicial = Integer.parseInt(args[0]);
      int valorFinal = Integer.parseInt(args[1]);
      if (valorInicial > 0 & valorFinal > 0) {
```

O código inicia com a declaração da classe principal (Palindromos), e em seguida, é declarado o método main.
Posteriormente é declarada duas variáveis que recebe números inteiros (valor inicial e valor final). Essas variáveis guardam os valores declarado nos argumentos da execução do código. O try-Catch será usado para o tratamento de erros


```
System.out.println(
            "_".repeat(15)
                + "\nValor Inicial: "
                + valorInicial
                + "\nValor Final: "
                + valorFinal
                + "\n"
                + "_".repeat(15));
        tratamentoDosValores(valorInicial, valorFinal);
```

Nessa parte do código, caso não tenha ocorrido nenhum erro anteriomente, o código irá imprimir o valor inicial e o final, e posteriomente usar a função tratamentoDosValores para fazer toda a lógica e imprimir apenas os números palindromos.

```
} else if (valorInicial <= 0 || valorFinal <= 0) {
        System.out.println("São aceitos apenas valores positivos");
      }
    } catch (NumberFormatException e) {
      System.out.println("Apenas números inteiros são aceitos");
    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("É necessário pelo menos dois valores inteiros como argumento");
    }
```

Ainda no try, o código faz a verificação se os valores iniciais e final são maior ou igual a zero, uma vez que deve ser aceito apenas os números positivos. Após a verificação do else, entra dois blocos com o NumberFormatException e o 
ArrayIndexOutOfBoundsException. O NumberFormatException será executado caso os valores passados como argumentos na execução do código, seja diferentes de int, exemplo: O usuário passa uma letra ao invés de um número. O ArrayIndexOutOfBoundsException é usado caso o usuário passe apenas um valor na execução.


## Autores

- [@DevJunr](https://www.github.com/devJunr)
