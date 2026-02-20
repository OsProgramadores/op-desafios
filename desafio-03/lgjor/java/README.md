# Desafio 3: Palíndromos

## Descrição do Desafio

Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado. Um exemplo de palíndromo é a palavra “reviver”.

Neste desafio, a idéia é imprimir todos os números palindrômicos entre dois outros números. Tal como as palavras, os números palindrômicos mantêm o mesmo valor se lidos de trás para a frente.

Observe que o número inicial e final devem ser incluídos nos resultados, caso também sejam palíndromos.

### Exemplos

1. Dado o número inicial 1 e número final 20, o resultado seria: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11.

2. Dado o número inicial 3000 e número final 3010, o resultado seria: 3003.

3.  Dado o número inicial 101 e número final 121, o resultado seria: 101, 111, 121.

### Para o desafio, assuma:

Apenas inteiros positivos podem ser usados como limites.
Números de um algarismo são palíndromos por definição.
Máximo número: (1 « 64) - 1 (máximo unsigned int de 64 bits).
Bônus: Se o desafio parece fácil demais, implemente um novo tipo de dados para calcular pra qualquer número com precisão arbitrária (limite: 100000 algarismos por número). O uso de bibliotecas matemáticas de precisão arbitrária não será considerado como uma solução válida.

## Tecnologias utilizadas

- Linguagem: Java
- Versão: 17

## Lógica utilizada para a solução do problema

Foi implementada a classe Palindromos com os campos: Intervalo inicial(inteiro), intervalo final(inteiro) e Lista de Palindromos (inteiros).

A validação é feita antes de instanciar o objeto e assegura que:
- Deve possuir 2 argumentos.
- Devem ser inteiros válidos.
- Devem ser maior ou igual a 1.
- O intervalo final deve ser maior que o inicial

Após passar por essa validação, é instanciado o objeto Palindromos com um intervalo inicial (válido), intervalo final (válido) e uma lista de palindromos vazia.

```java
Palindromos palindromos = new Palindromos(intervaloInicial, intervaloFinal);
```

Após instanciar o objeto, é chamado o método encontrarPalindromos para localizar os palindromos existentes entre o intervalo inicial e final e preencher a lista de palindromos, incialmente vazia.

```java
palindromos.encontrarPalindromos(intervaloInicial, intervaloFinal);
```

Quando esse método recebe um número maior que 9, já que todos os números de 1 a 9 são palíndromos, esse método utiliza uma função `isPalindromo()` que verifica de forma matemática se o número é palindromo.

A verificação é feita armazenando o número original numa variável para comparação com o número Revertido. O `numeroAReverter` é revertido ao adicionar o seu último dígito à variável `numeroRevertido`. A cada número adicionado nessa variável `numeroRevertido`, um último número é retirado da variável `numeroAReverter`.

Quando todos os dígitos do número original foram processados e removidos, a variável `numeroAReverter` se torna zero. Nesse momento, o laço `while` de repetição é quebrado.

Quando a repetição é quebrada, a função booleana `isPalindromo()` retorna verdadeiro caso o `numeroRevertido` seja igual ao `numeroOriginal`.

Após encontrados os palíndromos, a impressão dos elementos palíndromos encontrados é feita pelo método:

```java
palindromos.imprimirPalindromos();
```

Esse método percorre a lista de elementos palíndromos do Objeto Palindromos e imprime um elemento por vez utilizando o BufferedWriter, após imprimir cada elemento, salta para a próxima linha.

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
