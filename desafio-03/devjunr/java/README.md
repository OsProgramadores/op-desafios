
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
public class Palindromos {
    public static void main(String[] args){
        int valorInicial = Integer.parseInt(args[0]);
        int valorFinal = Integer.parseInt(args[1]);
```

O código inicia com a declaração da classe principal (Palindromos), e em seguida, é declarado o método main.
Posteriormente é declarada duas variáveis que recebe números inteiros (valor inicial e valor final). Essas variáveis guardam os valores declarado nos argumentos da execução do código.


```
if(args.length < 2) {
            System.out.println("Forneça dois valores inteiros como argumento\nExemplo: java Palindromos.java 10 50");
        }else if(valorInicial < 0 || valorFinal < 0){
            System.out.println("Apenas números maior que 0 são aceitos");
        }else{
            System.out.println("_".repeat(10)+"\n"+"Valor Inicial: " + valorInicial + "\nValor Final: " + valorFinal +"\n"+ "_".repeat(10)+"\n");
            tratamentoDosValores(valorInicial, valorFinal);
        }
```

Nessa parte o código faz uma simples verificação para que possa prosseguir. Verifica o total de argumentos que foi passado, se o número é maior que zero ou não, se passar nas verificações o ele executa o último else, onde printa no terminal o valor inicial e o valor final, para exibir ao usuário que o código conseguiu ler os dois valores. e em seguida, usa a função         tratamentoDosValores(valorInicial, valorFinal) para fazer o tratamento dos valores

```
private static void tratamentoDosValores(int valorInicial, int valorFinal){
        System.out.println("Resultado: ");
        for(int i=valorInicial;i<=valorFinal;i++){
            String numero = Integer.toString(i);
            String reversed = new StringBuilder(numero).reverse().toString();
            if (reversed.equals(numero)) {
                System.out.println(numero);
            }
        }
    }
```

Na declaração do método tratamentoDosValores, ele recebe os valores inicial e final, em seguida printa no terminal a palavra "Resultado: "

Entrando no laço de repetição (for), ele é declarado com uma variavel do tipo inteiro (i), onde inicia com o valorInicial, vai até i ser igual valorFinal, e a cada loop ele adiciona mais um (i++). Na primeira linha do loop, é declarado uma String nomeada de número, a mesma recebe uma conversão do i (int) para String.

Após a string numero, foi declarada uma outra string, chamada de reversed, ela é a responsável por reverter o "texto" para posteriormente fazer uma verificação.

Entrando no if do método, ele faz a verificação se a variavel reversed é igual a váriavel número, se sim: Imprime o número no terminal, se não, não faz nada. Permitindo assim, exibir apenas os números que quando invertido, é igual ao valor normal

## Autores

- [@DevJunr](https://www.github.com/devJunr)
