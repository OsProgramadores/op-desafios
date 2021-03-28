import {
  lerArquivoFuncionarios
} from './lib/arquivos';

import { 
  printGeral,
} from './lib/print';

const count = process.argv.length-1;
const param = process.argv[count];

((fileName: string) => {

  try {
    const funcionariosDb = lerArquivoFuncionarios(fileName);

    if (funcionariosDb !== null) {
      console.log(printGeral(funcionariosDb));
    }
  } catch (e) {
    console.log(`Error: ${fileName} ${e.message}`);
  } 

})(param);