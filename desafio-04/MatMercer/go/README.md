# Solução desafio Xadrez

O programa usa o stdio para calcular a quantidade de peças, no seguinte formato:

```
4 3 2 5 6 2 3 4\n1 1 1 1 1 1 1 1\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n1 1 1 1 1 1 1 1\n4 3 2 5 6 2 3 4
```

Logo, o uso dele é da seguinte maneira:

```
echo "4 3 2 5 6 2 3 4\n1 1 1 1 1 1 1 1\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n1 1 1 1 1 1 1 1\n4 3 2 5 6 2 3 4" | xadrez
Peão: 16 peça(s)
Bispo: 4 peça(s)
Cavalo: 4 peça(s)
Torre: 4 peça(s)
Rainha: 2 peça(s)
Rei: 2 peça(s)
```
