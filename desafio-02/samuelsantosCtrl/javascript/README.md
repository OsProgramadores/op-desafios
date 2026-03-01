### Sobre:

O script retorna um Array contendo todos os números primos de 1 - 10k no terminal.
### raciocínio:

Primeiro procurei entender como os Primos se comportam. Primos são números que só podem ser divididos por 1 e por eles mesmos. Nesses dois casos o resto da divisão nunca é 0.

No começo do código eu início um Array `num[]` e o preencho usando um `for`, que em cada petição usa o próprio valor do índice `i` para fazer a adição dos números no Array, indo de 1 - 10k

#### update:

Decidi mudar o código porque eu tentei fazer uma otimização prematura e que não ajudava em muita coisa(deixava até pior inclusive). Então eu removi a função `descartarMultiplos()` e refatorei o código.  Fiz melhorias que fazem o script calcular números primos até `500.000` em tempo aceitável.

Removi a criação do Array no único do código, agora temos um `for loop` que incrementa o número testado e somente quando é válido como primo ele é adicionado ao array de resultado

```js
for (let i = 1; i <= MAX_VALUE; i++) {
    if (verifyPrime(i) === true) {
        resultado.push(i);
    }
}
```

Adicionei uma variável `MAX_VALUE` que diz quantos números vão ser gerados na inicialização do array `num`

Mudei o código a seguir:

```js
const resultado = num.filter(verifyPrime);
```

Essa verificação foi refatorada para uma estrutura em `if`:

```js
if (verifyPrime(i) === true) {
    resultado.push(i);
}
```

A verificação do número primo mudou, agora, além de considerar se o módulo do número é 0, ele verifica números até a raiz do número `N`. E além disso, uso um novo método de verificação: o `6*k ± 1`

Se considerarmos que já foram removidos múltiplos de 2 e 3, sobra 5 como próximo número primo.

Todo número inteiro pode ser escrito como `6k + r`, onde r = {1, 2, 3, 4, 5}

Porém o filtro aplicado já foi removido 2 e 4; múltiplos de 2 e 3.

Restando apenas 1 e 5.

Como 6k + 5 = 6(k + 1) - 1.

Isso funciona porque essencialmente remove todos os números que compartilham fatores primos básicos com 6.

```js
for (let i = 5; i * i <= N; i += 6) {
    // teste na forma de 6*k ± 1
    if (N % i === 0 || N % (i + 2) === 0) {
         return false;
    }
}
```

Note que começa com 5, mas isso não é um problema pois:

6 * 1 - 1 = 5
6 * 1 + 1 = 7  (começamos no 5, por isso + 2)
