# Desafio 02: Primos

## Sobre a solução
primeiro, defini a função `display_primes` que recebe um `int`, que seria o limite de primos.

No corpo da função a variavel `dividers` guarda a quantidade de divisores que aquele número especifico tem. detalhe que numeros *primos* tem apenas dois divisores(1 e ele mesmo).

O primeiro `for` loop cria um laço começando de **2** até o número limite. cada número vai ser divido por todos os números anteriores a ele (*for* aninhado) e então verificado se é um divisor caso o resto de sua divisão seja **zero**, caso seja divisivel adicina +1 a `dividers` informando que o numero(do primeiro `for`) tem mais um divisor.

Quando a divisao for feita com todos os numeros anteriores, o segundo laço termina e agora verificamos se o numero é **primo**. Como? pelo numero de divisores.

Como eu desconsiderei a divisao por *1* (jà que todo numero é divisivel por *1*) precisamos apenas saber se o numero tem **1** divisor, então mostre-o. Caso tenha mais de *1* divisor ele não é primo ebnaobsera mostrado.

Agora é só reiniciar a variavel `dividers` com o valor 0 (*zero*) para ser contado os divisores do proximo numero no laço `for`.
