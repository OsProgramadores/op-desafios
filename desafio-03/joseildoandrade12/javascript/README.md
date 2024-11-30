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

Para testar a solução, é necessário ter o [Node.js](https://nodejs.org/) instalado em sua máquina.

```bash
$ git clone git@github.com:OsProgramadores/op-desafios.git

$ cd .\op-desafios\

$ node .\desafio-03\joseildoandrade12\javascript script.js

"Informe o valor minimo: "
"Informe o valor máximo: "
```