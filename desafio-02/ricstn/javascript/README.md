Localizador de Números Primos
Este é um script simples em JavaScript para encontrar todos os números primos no intervalo de 1 a 10.000.

Como Funciona
O script itera por cada número (i) de 1 até 10.000. Para cada número, ele utiliza um loop aninhado (j) que conta quantos divisores exatos o número possui.

Um número primo é definido como um número natural maior que 1 que possui exatamente dois divisores: 1 e ele mesmo.

Lógica Utilizada
O contador é iniciado em 0 para cada número i.

O loop interno j testa todos os números de i até 1 para verificar se são divisores (i % j === 0).

Se um divisor é encontrado, o contador é incrementado.

Otimização: Se o contador ultrapassar 2 em qualquer ponto, significa que o número já tem mais de dois divisores e, portanto, não é primo. O comando break é acionado para interromper o loop interno e economizar processamento.

Ao final do loop interno, se o contador for exatamente 2, o número i é adicionado ao array numeros.

Como Usar
Para executar este código, você precisará de um ambiente JavaScript, como o Node.js ou o console do seu navegador.

Usando Node.js
Salve o código em um arquivo (por exemplo, findPrimes.js).

Abra seu terminal na pasta onde o arquivo foi salvo.

Execute o comando:

Bash

node findPrimes.js
O terminal exibirá um array contendo todos os números primos encontrados entre 1 e 10.000.