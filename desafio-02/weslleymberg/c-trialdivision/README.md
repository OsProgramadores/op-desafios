Iniciei esse desafio com a ideia de que eu queria um código que pudesse gerar um numero primo de cada vez, sem a necessidade de criar listas de números em memória, como é feito nas peneiras ("sieves"). A opção mais simples, então, foi usar "trial division"; ou seja, testar cada número N dividindo-o por k, onde 1 < k < N.

Algumas pequenas otimizações podem ser realizadas para evitar testes de divisão desnecessários:
- Usar raiz de N como um limite para k (1 < k < sqrt(N)).
- Não testar numeros pares, pois já sabemos que não podem ser primos. Desta forma diminuimos a lista de números a serem testados pela metade.
- Todo número primo maior que 3 tem a forma 6x±1, onde x é qualquer número maior do que zero. Se considerarmos k = 6x±1, estaremos testando N contra seus possíveis fatores primos, o que diminui inda mais a quantidade de testes de divisão a serem feitos.

Fonte: https://en.wikipedia.org/wiki/Primality_test