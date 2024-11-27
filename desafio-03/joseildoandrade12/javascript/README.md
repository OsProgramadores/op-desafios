## Desafio 03: Números Palíndromos

Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado. Um exemplo de palíndromo é a palavra “reviver”.

## Solução

Primeiro passo: defini uma variável com um valor vazio de array para colocar os números palindrômicos.

Segundo passo: criei uma Função com dois parâmetros min(valor mínimo) e max(valor máximo).

Terceiro passo: fazer uma verificação se os valores min e max estão nas caracteristicas necessárias onde caso não tenha irá passar uma mensagem mostrando o erro do úsuario

Quarto passo: criei um loop que caso min fosse menor ou igual a max, ocorresse uma validação.

Quinto passo: criei uma constante numInverso, onde os valores que passaram na condição vão passar pelo método toString() tornando o Number numa string e logo em seguida com esse valor em String utilizando o método split('') que irá transformar a string numa array separando pelo valor que está sendo atribuito nos paresenteses, após isso utilizei o método de array reverse() para os valores que estão na array reverterem(quem está no inicio vai para o final e quem está no final vai para o inicio e assim por diante), e depois utilizei o split('') que irá juntar os valores da array pela condição que está no método tornando essa junção em uma String novamente.

Sexto passo: fazer uma validação com um if, se o valor min é igual ao valor que está em numInverso, ele vai adicionar o valor de min a váriavel que criei no inicio da solução pelo método de array variavel.push(valor).
