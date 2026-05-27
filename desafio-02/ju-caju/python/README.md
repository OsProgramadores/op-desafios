# Desafio 02 - Numeros primos

Solucao do desafio 02 do grupo [OsProgramadores](https://osprogramadores.com/desafios/).

## Autora

Juliana - [ju-caju](https://github.com/ju-caju)

## Sobre o desafio

O objetivo deste desafio e listar todos os numeros primos entre 1 e 10000.

Um numero primo e um numero natural maior que 1 que possui apenas dois divisores:
1 e ele mesmo.

## Como a solucao funciona

A implementacao usa o Crivo de Eratostenes, um algoritmo eficiente para encontrar
numeros primos ate um limite definido.

O programa cria uma lista marcando todos os numeros como possiveis primos. Em
seguida, percorre os numeros a partir de 2 e elimina os seus multiplos, pois
eles nao podem ser primos. A marcacao dos multiplos comeca em `numero * numero`,
porque os multiplos menores ja foram tratados por numeros anteriores.

Ao final, o programa imprime todos os numeros que continuaram marcados como
primos.

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa e necessaria

## Como executar

Entre na pasta da solucao:

```bash
cd desafio-02/ju-caju/python
```

Execute o programa:

```bash
python3 resposta.py
```

## Saida esperada

O programa imprime um numero primo por linha, comecando em `2` e seguindo ate o
maior numero primo menor ou igual a `10000`.

Exemplo do inicio da saida:

```text
2
3
5
7
11
13
```

## Estrutura dos arquivos

```text
desafio-02/ju-caju/python/
├── README.md
└── resposta.py
```
