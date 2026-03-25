const { readFile } = require("fs");
const filename = process.argv[2];

let pecas = {
  0: { nome: "Vazio", qtd: 0 },
  1: { nome: "Peão", qtd: 0 },
  2: { nome: "Bispo", qtd: 0 },
  3: { nome: "Cavalo", qtd: 0 },
  4: { nome: "Torre", qtd: 0 },
  5: { nome: "Rainha", qtd: 0 },
  6: { nome: "Rei", qtd: 0 },
};

readFile(filename, "utf8", function (err, data) {
  if (err) {
    console.log(
      `Não foi possível ler o arquivo ${process.argv[2]}.\nErro: ${err.message}`
    );
    return;
  }

  data
    ?.replace(/ /g, "") // Remover espaços
    ?.replace(/\n/g, "") // Remover novas linhas
    ?.split("") // Transformar em um vetor
    ?.forEach((i) => pecas[i].qtd++); // Contar cada peça

  for (const codigo in pecas) {
    const peca = pecas[codigo];
    if (codigo != 0) {
      console.log(`${peca.nome}: ${peca.qtd} peça(s)`);
    }
  }
});
