# Desafio 3: Palíndromos

## Descrição do Desafio

Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado. Um exemplo de palíndromo é a palavra “reviver”.

Neste desafio, a idéia é imprimir todos os números palindrômicos entre dois outros números. Tal como as palavras, os números palindrômicos mantêm o mesmo valor se lidos de trás para a frente.

Observe que o número inicial e final devem ser incluídos nos resultados, caso também sejam palíndromos.

Exemplo 1: Dado o número inicial 1 e número final 20, o resultado seria: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11.

Exemplo 2: Dado o número inicial 3000 e número final 3010, o resultado seria: 3003.

Exemplo 3: Dado o número inicial 101 e número final 121, o resultado seria: 101, 111, 121.

Para o desafio, assuma:

Apenas inteiros positivos podem ser usados como limites.
Números de um algarismo são palíndromos por definição.
Máximo número: (1 « 64) - 1 (máximo unsigned int de 64 bits).
Bônus: Se o desafio parece fácil demais, implemente um novo tipo de dados para calcular pra qualquer número com precisão arbitrária (limite: 100000 algarismos por número). O uso de bibliotecas matemáticas de precisão arbitrária não será considerado como uma solução válida.

## Tecnologias utilizadas

- Linguagem: Java
- Versão: 17

## Lógica utilizada para a solução do problema

Como estou estudando orientação a objetos no momento, optei por implementar uma classe Palindromo e seu construtor que aceita apenas números inteiros positivos iguais ou maiores que um. Sendo que o intervalo inicial deve ser maior que um e o intervalo final deve ser maior que o inicial.

A minha lógica foi a seguinte: Criei um objeto palíndromos que armazena uma lista de palíndromos entre um dado intervalo inicial e final de números inteiros. Pensei o seguinte, qual a condição de existência desse objeto? A condição de existência é que exista um intervalo inicial e final válido e que existam palíndromos nesse intervalo. Caso a condição não fosse atendida, não faria sentido criar esse objeto palíndromos. Por esse motivo achei razoável colocar a lógica no construtor.

Para que esse requisito seja atendido, antes de instanciar a classe, foi implantado um método estático de validação `lerInteiroPositivoMaiorQueOMinimo()` que aceita números inteiros positivos maior que o valor mínimo informado.

Com esse método estático, no método main:
- Para o intervalo inicial foi lido um número inteiro positivo maior que 0;
- Para o intervalo final foi lido um número inteiro positivo maior que o intervalo inicial;

Com os requisitos estavam atendidos. Foi instanciado um novo objeto Palindromos:

```java
Palindromos palindromos = new Palindromos(intervaloInicial, intervaloFinal);
```

Ao instanciar um novo objeto do tipo palindromo, o construtor invoca o método encontrarPalindromos que retorna uma lista de números inteiros palindromos no intervalo especificado.

Quando esse método recebe um número maior que 9, já que todos os números de 1 a 9 são palíndromos, esse método utiliza uma função `isPalindromo()` que verifica de forma matemática se o número é palindromo.

A verificação é feita armazenando o número original numa variável para comparação com o número Revertido. O `numeroAReverter` é revertido ao adicionar o seu último dígito à variável `numeroRevertido`. A cada número adicionado nessa variável `numeroRevertido`, um último número é retirado da variável `numeroAReverter`.

Quando todos os dígitos do número original foram processados e removidos, a variável `numeroAReverter` se torna zero. Nesse momento, o laço `while` de repetição é quebrado.

Quando a repetição é quebrada, a função booleana `isPalindromo()` retorna verdadeiro caso o `numeroRevertido` seja igual ao `numeroOriginal`.

Para que a impressão fosse feita, conforme os requisitos do exercício, foi sobre-escrito o método toString para retornar apenas os números da lista separados por vírgula em uma única string:

```java
@java.lang.Override
    public java.lang.String toString() {

        String resultadoFormatado = String.join(", ",
                palindromos.stream().map(Object::toString).toList()
        );

        return resultadoFormatado;
    }
```

## Como Rodar o Desafio

Siga os passos abaixo no seu terminal para compilar e executar o projeto:

### 1\. Navegue até a pasta do projeto

Entre no diretório onde o arquivo principal (`Palindromos.java`) se encontra:

```bash
cd desafio-03/lgjor/Java
```

### 2\. Execute o Programa

Utilize o comando `java` seguido do nome da classe principal e dois números inteiros válidos, sendo que o segundo deve ser maior que o primeiro, por exemplo:

```bash
java Palindromos.java 1 100
```

### Licença de uso

Este projeto está licenciado sob a **[MIT License](https://opensource.org/licenses/MIT)**.

A licença MIT é uma licença permissiva que permite a reutilização, cópia, modificação, fusão, publicação, distribuição, sublicenciamento e/ou venda do software.

Autor: Lucas Godoy

- Sinta-se à vontade para copiar e reutilizar este exercício, ou partes dele, em qualquer ambiente de aprendizado, aula, material didático ou projeto educacional. Ao utilizar o código, fortaleça a comunidade e referencie os autores do desafio.

## Site de referência e repositório original

- [Site: Os programadores](https://osprogramadores.com/desafios/d03/)
- [Repositório oficial: Os Programadores - Desafios](https://github.com/OsProgramadores/op-desafios)
