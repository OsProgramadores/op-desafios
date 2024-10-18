# Desafio 02: Primos
Solução usando algoritmo [crivo de eratostenes (Wikipedia)](https://pt.m.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes)

## Sobre a solução
Primeiramente, defini a função `crivo()` que recebe `limit`, um `int` que é o limite de números, e retorna `primes`, uma `list` que é um array com os números *primos* definidos como `True` e os não *primos* como `False`.

Dentro do escopo da função, defini a variável `primes` que inicia uma lista de tamanho `limit`, onde cada célula será definida como `True` inicialmente, assim informando que todos os números de 0 a `limit` são *primos*.

Como os números iniciais **0** e **1** não são primos, defini os valores de suas células como `False`.

A variável `prime` vai servir como um iterador para o laço `while` e vai servir para calcularmos seus múltiplos. Já que cada iteração do laço seu valor sera o próximo *primo*.

No laço while verificamos se o atual número (valor de `prime`) é menor que a raiz quadrada de `limit` (usando a equação `(prime*prime) <= limit)`). Enquanto for verdade, verificaremos os multiplos daquele número.

Já no escopo do laço `while`, verificamos se o valor da célula do número na lista é `True` indicando que é *primo*. Então calculamos os múltiplos desse número e caso seja, marcamos o valor da célula como `False` informando que não são *primos*.

> Inicialmente começamos com o **2**, então marcamos como `False` todos os múltiplos de **2**. Exceto, obviamente, ele mesmo.

Já fora do escopo do `for` e do `if`, atualizamos a váriavel `prime` para que faça o mesmo com o proximo numero.

Ja no `for` que fica fora do escopo da funcao `crivo()`, percorremos o retorno da funcao, nesse caso `primes`, e se a posicao conter `True` o nemero da posicao é *primo*.
