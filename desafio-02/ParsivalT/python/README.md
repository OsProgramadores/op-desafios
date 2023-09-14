# Crivo de Erastóstenes

O Crivo de Erastóstenes consiste em criar uma tabela com números que vão de 2 até o número desejado, visto que o número 1 não é primo. Em seguida, realizamos os seguintes passos:

Passo 1 – Tendo em vista as regras de divisibilidade, sabemos que o único número par primo é o número dois. Então, excluímos todos os demais pares da tabela, ou seja, os múltiplos de 2.

4,6,8,10,12,...

Passo 2 - De acordo com as regras de divisibilidade por 3, sabemos que um número é divisível por 3 caso a soma dos algarismos também seja. Assim, vamos excluir todos os números que são múltiplos de 3.

6,9,12,15,18,..., 321,324,...

Passo 3 – Do critério de divisibilidade por 5, sabemos que um número é divisível por 5 caso ele termine em 0 ou em 5. Vamos excluir todos os números que terminam em 0 e em 5.

10,15,20,15,30,...,5920,5925,...

Passo 4 – De maneira análoga, verificando o critério de divisibilidade, vamos excluir todos os múltiplos de 7.

14,21,28,35,...,539,546,...

Feito todo esse processo, os números que sobrarem são os primos de 2 até o número desejado.

