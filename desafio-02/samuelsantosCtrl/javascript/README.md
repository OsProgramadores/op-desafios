### Sobre:

O script retorna um Array contendo todos os números primos de 1 - 10k no terminal.
### raciocínio:

Primeiro procurei entender como os Primos se comportam. Primos são números que só podem ser divididos por 1 e por eles mesmos. Nesses dois casos o resto da divisão nunca é 0.

No começo do código eu início um Array `num[]` e o preencho usando um `for`, que em cada petição usa o próprio valor do índice `i` para fazer a adição dos números no Array, indo de 1 - 10k

#### update:

Decidi mudar o código porque eu tentei fazer uma otimização prematura e que não ajudava em muita coisa(deixava até pior inclusive). Então eu removi a função `descartarMultiplos()` e refatorei o código.  Fiz melhorias que fazem o script calcular números primos até `500.000` em tempo aceitável. 

Adicionei uma variável `MAX_VALUE` que diz quantos números vão ser gerados na inicialização do array `num`

Após isso uso o mesmo método `.filter`, mas removi a função `findPrimes()`, pois tbm era redundante. A função `verifyPrime()` pode retornar diretamente o valor `true` ou `false` do número sendo verificado.

```js
const resultado = num.filter(verifyPrime);
```

A verificação do número primo mudou, agora, além de considerar se o módulo do número é 0, ele verifica números até a raiz do número `N`. Isso otimiza e corta pela metade o número de verificações por número.
