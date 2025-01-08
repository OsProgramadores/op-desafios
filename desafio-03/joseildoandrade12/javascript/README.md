## Desafio 03: Números Palíndromos

Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado. Um exemplo de palíndromo é a palavra “reviver”.

## Solução

Primeiro passo: puxar os valores que foram passados pelo usuário;

Segundo passo: definir uma variável com um valor vazio de array para colocar os números palindrômicos.

Terceiro passo: fazer uma validação em uma função para saber valores passados nos parâmetros estão de acordo com o necessário para saber se é um número palindromo, caso não seja retornará uma mensagem de qual erro o usuário cometeu.

Quarto passo: utilizar os valores que foram verificados em uma função com dois parâmetros min(valor mínimo) e max(valor máximo).

Quinto passo: criar um loop que caso min fosse menor ou igual a max, ocorresse uma validação.

Sexto passo: criar uma constante onde os valores que passaram na condição vão passar pelo método toString() tornando o Number numa string e logo em seguida com esse valor em String utilizando o método split('') que irá transformar a string numa array separando pelo valor que está sendo atribuito nos paresenteses, após isso utilizar o método de array reverse() para os valores que estão na array reverterem(quem está no inicio vai para o final e quem está no final vai para o inicio, e assim por diante), e depois utilizar o split('') que irá juntar os valores da array pela condição que está no método tornando essa junção em uma String novamente.

Sétimo passo: fazer uma validação com um if, se o valor min é igual ao valor que está na constante passada, ele vai adicionar o valor de min a váriavel que criou no inicio da solução pelo método de array variavel.push(valor).

## Teste e execução

Para testar a solução, é necessário ter o [Node.js](https://nodejs.org/) com a versão mais recente instalada em sua máquina.

É necessário ter o GIT em sua máquina [GIT](https://git-scm.com/downloads) com a versão mais recente.

Entre no Git e faça um clone do repositório para a sua máquina:

```bash
$ git clone https://github.com/joseildoandrade12/op-desafios.git
```

Após ter clonado, abra o terminal e digite o código para acessar a pasta que contém o arquivo :

```bash
cd desafio-03/joseildoandrade12/javascript
```

Depois disso, ainda no terminal digite o seguinte para inicializar o código:

```bash
node script.js
```

Quando você inicializar o código, vai aparecer a seguinte mensagem:

```bash
Informe o valor minimo:
```

Na primeira pergunta insira o valor mínimo, caso ele não tenha os requisitos necessários irá retornar uma mensagem mostrando seu erro.

Depois irá aparecer:

```bash
Informe o valor máximo:
```

Como no primeiro, insira o valor, caso esteja fora dos requisitos ele irá retornar uma mensagem de erro.

Após tudo isso ele retornará todos os números palíndromos no intervalo dos valores que o usuário escolheu.
