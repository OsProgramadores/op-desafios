import { readInput, stringToMatrix } from './../helper';

test("Testar função de entrada de dados do sistema", async () => {
  expect(readInput('yarn ./src/main.ts 0 0 0'.split(' '))).toEqual(["0", "0", "0"]);
});

test("Testar função para transformar string em matrix de inteiros", async () => {
  expect(stringToMatrix(['0', '0', '0', '0', '0', '0', '0', '0', '0'], 3)).toEqual([[0, 0, 0], [0, 0, 0], [0, 0, 0]]);
});
