import { pecas } from "./../";

type Tabuleiro = number[][];
type ContabilizeResult = number[];

export function contabilize (tabuleiro: Tabuleiro): ContabilizeResult {
  const pecasCount:number[] = [];

  for (let i = 0; i < pecas.length; i++) {
    pecasCount[i] = 0;
  }

  for(let x = 0; x < tabuleiro.length; x++) {
    for (let y = 0; y < tabuleiro[x].length; y++) {
      pecasCount[tabuleiro[x][y]]++;
    }
  }  
  
  return pecasCount;
}

export function printContabilizado (result: ContabilizeResult): string {
  return result.map((total, i) => [
    `${pecas[i]}: ${total} peça(s)`
  ]).filter((peca, i) => i !== 0).join('\n');
}