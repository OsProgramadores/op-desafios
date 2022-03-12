import { exec } from "child_process";
import { contabilize, printContabilizado } from "./../xadrex/contabilize";

const tabulerio1 = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
];

describe ("testar contabilização das peças", () => {
  const result = contabilize(tabulerio1);

  test('Testando estrutura que deveria ser retornada da função de contabilidade', () => {
    expect(result).toEqual([60, 4, 0, 0, 0, 0, 0]);
  });
  
})

test("Testar saida da função de printar o resultado contabilizado", () => {
  const resultFormat = `Peão: 4 peça(s)\nBispo: 0 peça(s)\nCavalo: 0 peça(s)\nTorre: 0 peça(s)\nRainha: 0 peça(s)\nRei: 0 peça(s)`;
  expect(printContabilizado([60, 4, 0, 0, 0, 0, 0])).toEqual(resultFormat);
});

test("Testar saida do programa formatado", () => {
  return new Promise((resolve, reject) => {
    exec('yarn start 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0', (error, stdout) => {
      if (error) {
        reject(error);
      }
      resolve(stdout);
    })
  }).then(result => {
    const resultFormat = `Peão: 4 peça(s)\nBispo: 0 peça(s)\nCavalo: 0 peça(s)\nTorre: 0 peça(s)\nRainha: 0 peça(s)\nRei: 0 peça(s)`;
    expect(result).toMatch(resultFormat);
  });

});