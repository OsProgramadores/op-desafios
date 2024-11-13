# Números palindrômicos

Descrição
Este programa em Java identifica números palíndromos em um intervalo especificado pelo usuário.
Mas o que é um número palíndromo?
Em termos simples, um palíndromo é uma palavra, número ou sequência de caracteres que pode ser lida da mesma forma da 
esquerda para a direita e da direita para a esquerda.
Alguns exemplos são a palavra “reviver” e o número “121”.

Funcionalidades

Tratamento de Exceções para a Entrada:

O uso de um laço while com tratamento de exceções (try-catch) assegura que o programa só continuará após receber duas 
entradas válidas do usuário.

Conversão de Número para String:

Cada número no intervalo é convertido para uma String, permitindo que cada caractere seja tratado individualmente, 
semelhante a um array de caracteres.

Método de Verificação de Palíndromo:

O método ePalindromo() utiliza a classe StringBuilder para inverter a String.
Se a String invertida for idêntica à String original, o número é considerado palíndromo.

Armazenamento e Exibição:

Os números palíndromos são adicionados a uma lista e exibidos ao final, organizados de forma clara para o usuário.

Como o Programa Funciona

Entrada de Intervalo:

O programa solicita ao usuário dois números inteiros positivos que definem o intervalo de busca dos números palíndromos:
um valor inicial (numeroInicial) e um valor final (numeroFinal).

Validação de Entradas:

Antes de iniciar a busca, o programa valida os valores inseridos para garantir que ambos sejam inteiros não negativos.
Caso o usuário insira um valor inválido (como um caractere não numérico ou um número negativo), o programa exibe uma 
mensagem de erro e solicita a entrada novamente.

Identificação dos Palíndromos:

Para cada número no intervalo [numeroInicial, numeroFinal], o programa verifica se ele é um palíndromo.
Essa verificação é feita convertendo o número em uma String e usando um método auxiliar chamado ePalindromo():
O método ePalindromo() inverte a String e compara a versão invertida com a original.
Se ambas as versões forem idênticas, o número é considerado palíndromo.

Exibição do Resultado:

Todos os números palíndromos encontrados no intervalo são armazenados em uma lista, que é exibida ao final do programa.
