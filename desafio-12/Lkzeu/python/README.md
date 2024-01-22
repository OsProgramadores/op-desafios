## Requisitos
1. ter o python 3.3+ instalado;
2. ter o arquivo de validação d12.txt (que pode ser localizado na seção Validação da página do [desafio 12](https://osprogramadores.com/desafios/d12/)) na mesma pasta do programa d12_potencia.py;

## Como executar?
para executar basta rodar o seguinte comando:
```python d12_potencia.py```

## Como funciona o programa?
O programa abre o arquivo d12.txt e lê todas as linhas, depois itera por cada linha e verifica se o número contido nela é par ou não.
 - Caso o número não seja par (com exceção do número 1) ele irá mostrar na tela o número lido seguido da palavra *false* pois este número não é uma potência de 2.

 - Caso o número seja par ou 1 iremos contar qual o expoente *n* necessário para que $2^n$ seja igual ao número lido, para isso foi usado um operador binário que desloca 1 bit para direita do número (que é equivalente a dividir o número por 2). Esse processo é repetido até o número ser igual a 1 e o contador de expoentes é incrementado cada vez que o número é dividido por 2.
   - Por exemplo, o número 16 é representado em binário por `0b10000` se o deslocarmos 4 bits para direita chegaremos em 1 que em binário é `0b00001` e $2^4=16$.

 - Contudo, nem todo número par é potência de 2 e pode ser escrito perfeitamente como $2^n$ devido a isso após contar os expoentes o programa irá verificar se $2^n$ é igual ao número lido na linha, caso seja irá repetir o número lido seguido da palavra *true* e o expoente *n* ao qual se deve elevar para obter o número lido.
