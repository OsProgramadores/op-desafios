# README

## Desafio 6 (Linguagem: Python)

O desafio consiste em localizar anagramas de uma expressão, de no máximo 16 caracteres, fornecida pelo usuário na linha de comando. Esses anagramas deverão ser compostos por palavras obtidas no arquivo 'words.txt', fornecido pelo proponente do desafio.

Minha solução foi escrita usando a linguagem Python, nas versões 3.12 e 3.13, e não utiliza bibliotecas externas. Ela consiste em, primeiramente, reduzir o campo de busca ao mínimo usando uma série de funções (aquelas relacionadas em _shrink_search_field_). Após, utilizei um algoritmo obtido na web (Livre para uso, segundo o autor.) para encontrar todas as partições ([Função de Partição](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_de_parti%C3%A7%C3%A3o_(matem%C3%A1tica))) possíveis para o número de caracteres contidos na expressão fornecida pelo usuário e escrevi uma função (_shrink_partitions_) para eliminar as que não fossem adequadas para a obtenção dos anagramas.

Com as partições definidas, escrevi uma função (_find_in_partition_) que busca os anagramas no arquivo 'words.txt', utilizando um dicionário para mapeamento dos totais de caracteres contidos na expressão e nas diversas palavras a serem testadas.

## Modo de Usar

Abra um terminal e execute o programa, assim:

```bash
$ python desafio06.py VERMELHO
ELM HO REV
ELM OH REV
ELM HOVER
LEVER OHM
OHM REVEL
HELM OVER
HELM ROVE
HOLM VEER
```

Para ajuda sobre o uso do programa, digite no terminal `python desafio06.py --help`. Os testes podem ser executados com `python test_desafio06.py` (Optei por deixá-los em um arquivo separado.).
