# Solução desafio Xadrez

## Compilando

```
go build xadrez.go
```

## Como usar

O programa usa um arquivo para calcular a quantidade de peças:
```
Uso: xadrez [nome_arquivo]

Voce pode gerar o tabuleiro e salvar ele:
xadrez gerar-tabuleiro

O programa também aceita tabuleiros de qualquer tamanho:
xadrez gerar-tabuleiro-gigante
```

Tabuleiro exemplo:

```
4 3 2 5 6 2 3 4
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
4 3 2 5 6 2 3 4
```

## Exemplos
```
go build xadrez.go
./xadrez gerar-tabuleiro > tabuleiro.txt
cat tabuleiro.txt
4 3 2 5 6 2 3 4
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
4 3 2 5 6 2 3 4

./xadrez tabuleiro.txt

Peão: 16 peça(s)
Bispo: 4 peça(s)
Cavalo: 4 peça(s)
Torre: 4 peça(s)
Rainha: 2 peça(s)
Rei: 2 peça(s)
```

```
go build xadrez.go
./xadrez gerar-tabuleiro-gigante > tabuleiro-gigante.txt
cat tabuleiro-gigante.txt
4 1 1 4 2 1 2 4 3 2 3 1 3 1 2 0 3 6 2 6 3 1 0 0 1 0 0 0 4 6 6 2
2 3 4 5 4 3 3 3 5 4 6 1 0 4 4 0 4 5 2 1 4 1 1 3 3 0 4 4 6 1 4 6
0 0 6 0 4 4 3 5 1 4 2 2 4 2 2 4 4 2 1 0 1 2 0 6 0 3 2 3 4 2 2 1
3 4 0 3 5 5 4 4 6 4 0 0 1 0 6 1 3 2 0 6 3 5 3 2 4 2 0 5 5 5 3 6
6 1 5 2 2 4 1 3 4 3 2 4 2 3 1 2 4 3 6 2 3 5 6 1 5 1 5 4 6 3 5 1
4 4 4 6 1 1 4 6 6 2 1 2 0 2 5 5 0 0 2 5 5 0 6 0 2 4 6 0 1 2 1 3
1 6 0 6 5 6 0 1 5 0 5 2 0 4 1 0 2 4 0 5 0 4 4 5 4 3 2 5 6 3 5 5
2 2 6 3 4 0 0 1 1 2 5 3 3 2 3 6 2 3 0 1 0 1 0 0 4 1 1 0 0 0 1 1
5 0 5 5 0 1 4 0 4 6 3 2 1 0 6 4 5 4 5 1 4 5 2 3 2 1 4 5 3 5 1 0
2 4 1 6 1 3 2 5 6 6 4 6 2 0 1 6 1 2 2 4 0 3 1 4 0 2 4 3 3 0 1 1
1 1 3 3 0 3 1 3 6 3 4 3 3 0 6 2 2 1 4 2 3 1 4 0 4 3 0 3 6 0 1 1
0 0 3 5 2 1 1 2 4 3 3 2 1 6 0 1 6 5 5 1 0 6 2 4 3 4 2 1 1 5 2 3
2 0 5 4 2 0 6 0 2 0 6 2 0 0 5 4 1 1 3 2 2 6 2 5 5 5 0 5 6 4 5 0
2 2 2 2 3 5 3 5 1 0 4 2 6 1 2 5 3 6 2 5 2 0 4 1 4 6 3 6 3 4 2 4
4 2 0 4 2 2 0 6 3 5 6 4 2 6 3 1 3 2 5 5 3 0 6 0 4 0 4 1 6 0 0 1
1 5 2 0 1 4 1 2 2 1 5 5 0 4 3 0 1 4 0 6 5 2 3 1 6 2 3 5 0 6 4 3
3 3 0 5 4 0 5 0 6 0 1 2 5 5 1 3 0 2 2 5 5 2 3 4 5 1 3 6 2 4 3 5
0 2 6 4 6 6 4 6 0 6 4 5 3 6 4 5 3 0 0 4 3 1 1 3 5 0 6 2 2 2 1 6
5 0 4 2 6 6 5 2 2 2 5 5 0 3 2 0 3 4 0 0 6 1 0 4 2 1 6 5 0 5 0 2
3 1 6 5 4 6 4 0 3 6 5 4 3 1 1 4 6 2 4 6 0 0 6 0 3 4 1 6 0 5 1 1
5 1 3 2 5 2 2 5 1 1 5 0 3 4 6 4 0 4 6 0 3 3 3 3 0 6 4 6 4 3 4 3
3 1 2 5 5 5 5 1 2 0 6 5 1 2 2 3 3 3 2 3 5 4 5 1 0 3 1 6 4 0 3 4
3 1 0 0 1 4 2 2 6 4 5 2 4 1 3 5 6 4 2 2 1 3 3 3 1 2 1 2 1 6 6 3
0 6 5 5 2 5 2 3 1 5 2 0 5 6 0 4 3 1 5 4 6 6 3 6 4 0 4 5 0 3 6 0
4 4 3 1 0 3 0 1 1 1 4 2 1 5 2 5 3 6 0 3 5 3 0 6 2 4 0 2 4 6 6 0
3 6 6 1 5 3 4 1 5 2 4 2 1 3 2 5 2 6 5 6 1 4 3 1 3 0 4 1 6 2 3 0
6 1 4 3 5 2 2 3 4 2 4 3 5 4 2 2 2 5 6 5 4 5 5 2 3 1 3 4 6 2 4 6
1 2 1 0 0 3 2 4 1 3 1 0 4 5 1 6 5 6 3 1 4 5 0 4 2 1 3 6 1 4 2 1
6 6 0 4 1 0 6 5 5 5 2 3 6 2 3 2 3 5 5 4 4 6 6 1 1 4 2 0 6 5 5 5
4 3 1 0 3 5 5 1 0 3 1 6 4 2 5 6 5 5 1 3 5 2 4 2 4 3 2 6 3 0 2 0
1 4 2 5 2 4 4 0 3 3 4 3 6 3 1 0 2 6 3 6 5 4 1 6 5 6 4 6 0 5 2 6
4 2 6 3 2 0 3 3 3 1 4 2 0 4 2 0 4 3 0 6 5 4 1 0 0 2 4 2 4 1 6 2

./xadrez tabuleiro-gigante.txt

Peão: 146 peça(s)
Bispo: 160 peça(s)
Cavalo: 150 peça(s)
Torre: 154 peça(s)
Rainha: 135 peça(s)
Rei: 130 peça(s)
```
