void main() {
  Map<int, List> tabuleiro = {
    0: ['Nulo', 0],
    1: ['Peao', 0],
    2: ['Bispo', 0],
    3: ['Cavalo', 0],
    4: ['Torre', 0],
    5: ['Rainha', 0],
    6: ['Rei', 0]
  };
  List<List<int>> matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
  ];

  for (var linha in matriz) {
    for (var pecas in linha) {
      tabuleiro[pecas][1] += 1;
    }
  }
  for (int i = 1; i < tabuleiro.length; i++) {
    print('${tabuleiro[i][0]} = ${tabuleiro[i][1]}');
  }
}
