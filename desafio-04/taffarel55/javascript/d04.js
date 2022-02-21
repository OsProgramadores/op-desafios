let pecas = {
  0: { nome: "Vazio", qtd: 0 },
  1: { nome: "Peão", qtd: 0 },
  2: { nome: "Bispo", qtd: 0 },
  3: { nome: "Cavalo", qtd: 0 },
  4: { nome: "Torre", qtd: 0 },
  5: { nome: "Rainha", qtd: 0 },
  6: { nome: "Rei", qtd: 0 },
};

const removeSpacesAndNewlines = (string) =>
  string.replaceAll(" ", "").trim().replaceAll("\n", "");

const tabuleiro1 = `
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 1 1 0 0 0
    0 0 0 1 1 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
`;

const tabuleiro2 = `
    4 3 2 5 6 2 3 4
    1 1 1 1 1 1 1 1
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    1 1 1 1 1 1 1 1
    4 3 2 5 6 2 3 4
`;

removeSpacesAndNewlines(tabuleiro2)
  .split("")
  .forEach((i) => pecas[i].qtd++);

for (const codigo in pecas) {
  const peca = pecas[codigo];
  if (codigo != 0) {
    console.log(`${peca.nome}: ${peca.qtd} peça(s)`);
  }
}
