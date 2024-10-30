# Listando números primos.

Escreva um programa para listar todos os números primos entre 1 e 10000, na
linguagem de sua preferência.

Utilizando Crivo Eratóstenes

Passo 1 : Declare uma variavel indicando o valor máximo;

Passo 2 : Declare um array booleano com tamanho maximo + 1;

Passo 3 : Use o Arrays.fills  para transformar todos valores do array em true
como especificado numPrimos, true;

Passo 4 : Crie um for para receber os valores e comecar a seleção atraves do
metodo crivo de eratóstenes;

Passo 5 : No for o [i] inicia com 2 ; 2 * 2 é menor que o max  e incrementa + 1
quando retornar nessa linha;

Passo 6 : Na proxima  linha é verificado se o numero é true , sendo true é
imprimido;

Passo 7 : No proximo for o j inicia valendo 2 * 2 ; 4 <= max ; a incrementação
sera j += i;

Passo 8 : O valor de j sendo 4 passa a ser false quando validado na proxima linha;

Passo 9 : Quando retornar no for o j vai  incrementar  4 + 2 = 6 e assim por
diante até o valor max, com isso teremos todos os mutiplos de 2 e assim
sucessivamente para todos os numero que forem primos os seus mutiplos serao
descartados como falso.

Passo 10 : E todos os numero que forem primos sera imprimido no terminal do
ultimo for,onde cada numPrimo encontrado até o maximo toda vez que passar pelo
sysout;