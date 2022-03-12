import { contabilize, printContabilizado } from "./../src/xadrex/contabilize"
import { readInput, stringToMatrix } from "./helper";

(() => {
  const tabuleiroData = readInput(process.argv);
  const tabuleiro = stringToMatrix(tabuleiroData);

  const contabilizado = contabilize(tabuleiro);
  const result = printContabilizado(contabilizado);

  console.log(result);
})()
