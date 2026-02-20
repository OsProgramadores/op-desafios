### Sobre:

O script retorna um Array contendo todos os números primos de 1 - 10k no terminal.

### raciocínio:

Primeiro procurei entender como os Prinos se comportam. Primos são números que só podem ser dividos por 1 e por eles mesmos. Nesses dois casos o resto da divisão nunca é 0.

No começo do código eu início um Array `num[]` e o preencho usando um `for`, que em cada petição usa o próprio valor do índice `i` para fazer a adição dos números no Array, indo de 1 - 10k

 Início um outro Array `notIsPrime[]` que irá conter números que não precisaram ser verificados. Pois ao achar um numero primo maior que 1, todos os seus múltiplos subsequentes podem ser descartados.

```js
const notIsPrime = [];
const num = [];

for (let i = 1; i <= 10000; i++) {
    num.push(i);
}
```

Originalmente eu fiz um simples `num.foreach(findPrimes)`
Aonde o resultado era impresso através de um `console.log()` interno da função toda vez que encontrava um número primo. Porém me recomendaram a mudar para remover resultados `undefined`: após fazer a verificação e não ser primo, a função retornava nada, causando o problema:

```js
num.forEach(findPrimes);
```

A solução foi declarar uma variável chamada `resultado` que aplica a função `findPrimes()` a cada elemento do Array `num[]`. Toda a logica do código ja estava no caminho certo e foi só questão de mudar o método e adcionar `returns`:

```js
const resultado = num.filter(findPrimes);
```

Depois disso chegamos função "main" do programa, ela faz duas checagens no número;
- Verifica se o numero está no array `notIsPrime[]` com a função `notOnList()`, como condição para continuar. Caso contágio pula o número.
- Em seguida verifica se o numero é primo com a função `verifyPrime()`.

(Percebi agora que tem uma redundância de código um if pode ser removido, e que a função `notOnList()` poderia ser simplificada para uma simples negação de `.includes()` também.)

Dentro da função `verifyprime()` temos um `for` que testa divisores desde 2 até o próprio numero, verificando se ele é primo atravez do modulo da divisão, que não pode ser igual a 0. Conforme explicado anteriormente...

Com isso na primeira divisão que resulta em 0, faz a função parar, pois o número não é primo. Retornando o valor `false`.

```js
function verifyPrime(N) {
    for (let i = 2; i < N; i++) {
        if (N % i === 0) {
            descarteMultiplos(N);
            return false;
        }
    }
    return true;
}
```

quando nenhum divisor é encontrado, retorna `True`, passa na verificação, e a função retorna o valor para o `.filter()`, que adiciona o número no resultado final.

Quando processo é executado para cada número de 1-10k, encontrando assim os  números primos. O resultado final é armazenado na variável `resultados` e é exibida com um `console.log()`. E assim encerrando o programa.

### Requisitos

> Node.js (versão 18 ou superior recomendada)

### Execução:

1. Entre na pasta do arquivo:
```bash
cd ./op-desafios/desafio-02/samuelsantos-ctrl/javascript/
```

2. Execute o arquivo:
```bash
node primos-02.js
```
