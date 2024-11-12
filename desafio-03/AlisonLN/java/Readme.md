# Números palindrômicos

Passo 1 : Crie um scanner para ler a entrada de dados Inicial e Final;

Passo 2 : Crie um while para verificar se a entrada e a saida inseridas nao sao numeros negativos

Passo 3 : Crie um for onde o "i" vai receber a entrada (Inicial)  <= até o final ;

Passo 4 : Para conseguirmos ler o numero que é um int de tras para frente devemos transforma-lo em uma String
entao na proxima linha apos criar o for vamos pegar o i e transformalo em uma string armazenando em uma variavel
criada do tipo String;

Passo 5 : Crie uma variavel do tipo boolean para receber o metodo de verificacao que passa a variavel criada do tipo
String como argumento;

Passo 6 : A primeira verificacao no metodo que vamos realizar é se a variavel convertida contem apenas 1 algarismo
Números de um algarismo são palíndromos por definição;

Passo 7 : Se conter mais que 1 entao vamos realizar outro for onde o j inicia com o tamanho -1 vai iniciar o laço
contando de tras para frente até o 0 onde 0 é o final da String

Passo 8 :  Para que possa capturar esses caracteres crie um StringBuilder para armazenar a string em uma variavel nova

Passo 9 : Crie um if para verficicar se a variavel criada para armazenar a nova string reversa é igual a string
de entrada utilizando um equals para comparar se for igual entao é true se não é false;

Passo 10 : Crie uma Lista para que possa armazenar os numero que são palindromos e depois imprimi-los em sequencia fora
do laço for
