# Solução para o desafio de números primos 

## Linguagem de programação

- Javascript

A função **isPrime** verifica se o número passado como parâmetro para ela **num** é ou não um número primo. Para fazer a verficação ele passa pela primeira condição que verifica se o parâmetro **num** é igual  ao número **1**, caso seja você vai retornar **false** já que **1** não é um número primo. Caso não seja igual ao número **1**  ele vai para a segunda condição onde ele verifica se **num** é igual ao número **2**, caso seja o retorno será **true** por **2** ser um número primo.Caso não seja igual a **2** ele vai para a terceira condição que verifica o resto da divisão entre **num** e **2** e no caso de o resto dessa divisão ser igual  a **0** retornará **false**. 

Caso o resto da divisão não seja igual a zero vai iniciar loop **for** onde inicia uma variável **i** em 3,onde vai executar **for** enquanto a variável **i** ser menor ou igual a raiz quadrada de **num**, o método **Math.sqrt(num)** retorna a raíz quadrada de **num** e aumenta **i** mais 2 a **i** a cada iteração. Fazendo com que o loop itere somente em números ímpares, verificando se **num** é didvisivel por números ímpares, caso encontre esse divisor então num não é umnúmero primo.


Na função **generatePrimeInRange** temos dois parãmetros sendo o primeiro o número onde quero que comece a contar, e o segundo o número onde essa  contagem termina. Inicia dois arrays sendo numbers receberá a lista de números no intervalo determinado. E numbersPrimes a lista de números que são primos. No loop onde inicia a variavel **i** a qual recebe o parãmetro **start** e o loop será eexecutado enquanto **i** ser menor do que **end** e **i** receberá mais 1 a cada iteração. E a cada iteração desse loop o será adicionado ao array numbers o número que estiver na variável de iteração **i**.

Em seguida tem outro  loop **for** onde inicia a variável  c  em 0, e esse loop será executado enquanto **c** for menor  que o tamanho do array **numbers**, a cada iteração será adicionado  mais a **c**. Em seguida inicia a variável  **prime** que vai receber a chamada da função **isPrime** passando como parâmetro o iterador. O **if** verifica se o retorno da função **isPrime** é  igual **true** caso seja  ele irá adicionar ao array **numbersPrimes** o número que está no iterador, ea função então retornará o array **numbersPrimes** que deverá conter a lista  dos números  que são primos no intervalo determinado.