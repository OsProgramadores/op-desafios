# Desafio 06 - Anagramas
Um anagrama é uma palavra ou frase formada com o re-arranjo de todas as letras de uma outra palavra ou frase (sem sobra ou falta). Exemplos:

* A palavra barco é um anagrama da palavra cobra (todas as letras de “cobra” usadas em “barco).
* A palavra mar não é um anagrama da palavra roma (a letra “o” em “roma” não foi usada).
* A palavra sal não é um anagrama da palavra mal (a letra “s” de “sal” não existe em “mal”).

## O Problema
Escreva um programa na sua linguagem e bibliotecas preferidas que:

* Leia a expressão (que pode ser uma frase ou apenas uma palavra) a ser usada para a criação dos anagramas da linha de comando. Apenas as letras de “A” a “Z” deverão ser consideradas (ignore espaços e converta todas as letras minúsculas para maíusculas). Retorne erro e aborte a execução se caracteres inválidos forem encontrados na expressão (qualquer caracter não alfabético que não seja espaço, incluindo números, pontuação, ou caracteres acentuados).

* Leia uma lista de palavras válidas do arquivo words.txt (Download). O arquivo é formatado com uma palavra por linha, com palavras da língua inglesa (Nota: apesar de várias tentativas, o autor não conseguiu achar uma lista “limpa” de palavras da língua portuguesa).

* Imprima todas as combinações possíveis de anagramas (sem repetição de linhas ou palavras). Os anagramas devem conter apenas palavras válidas (lidas do arquivo acima).

* O formato de saída deve conter múltiplas linhas (uma por anagrama), com as palavras ordenadas alfabeticamente dentro de cada linha (veja exemplos abaixo).

* O programa deve ser capaz de calcular e imprimir a lista de anagramas possíveis para uma expressão de até 16 caracteres em menos de 60 segundos.

# Solução
## Como funciona
O programa irá ler uma entrada do usuário
* Deverá conter apenas letras e espaços.
* Se for inválida, ele tentará ler novamente.
* Se "S" for inserido, ele aborta o programa.

O programa busca pelo arquivo `words.txt`, que contém as palavras válidas, no diretório atual.
* Se não encontrar, pede que o usuário insira o caminho para o arquivo.
* Se as palavras forem inválidas, pedirá para ler um arquivo válido.

O programa imprimirá todas as combinações possíveis de anagramas com palavras válidas, em múltiplas linhas, sem repetir linhas ou palavras, que são ordenadas alfabeticamente.

## Como rodar
Para rodar, use Python na versão 3.12 ou superior e utilize o comando:

`python desafio-06.py`

# Algoritmo
## Função `read_expression`
Lê a entrada do usuário.
* Se for "S", aborta o programa
* Se for válida, a retorna em maiúsculas
* Se não for válida, pede uma nova entrada

## Função `read_words_file`
Lê o arquivo contendo as palavras válidas.
* Ele busca o arquivo `words.txt` por padrão na pasta do script.
* Se não encontrar, pede para o usuário inserir um caminho válido
* Verifica se o conteúdo do arquivo é válido
* Se "S" for digitado, aborta o programa.

## Função `count_letters`
Cria um dicionário (tabela hash) onde as chaves são as letras e os valores a ocorrência dessas letras.
* Recebe uma string
* Retorna um dicionário

## Função `is_valid_file`
Verifica se as linhas do arquivo de palavras são válidas

## Função `filter_valid_words`
Recebe uma string e uma lista de palavras.

Retorna uma lista contendo todas as palavras que possuem letras válidas contidas na string.

## Função `remove_letters`
Recebe duas strings e remove da primeira strings todas as letras que estão contidas na segunda.

## Função `generate_anagrams_list`
Recursivamente gera uma lista de todos os anagramas possíveis das palavras contidas na lista de palávras válidas cujas letras façam parte da expressão passada.

## Função `sort_valid_anagrams`
Recebe uma lista de anagramas, ordena, filtra e retorna apenas os anagramas válidos e ordenados.
