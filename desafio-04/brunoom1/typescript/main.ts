import { sToVec } from './helper';
import { PecaEnum, countPartsFromVector } from './chess';

(function () {

  const strVetor=
  `4 3 2 5 6 2 3 4
  1 1 1 1 1 1 1 1
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  1 1 1 1 1 1 1 1
  4 3 2 5 6 2 3 4`;
  
  const vetor = sToVec(strVetor);
  const arrcounted = countPartsFromVector(vetor);

console.log(`Peão: ${ arrcounted[PecaEnum.PEAO] } peça(s)
Bispo: ${ arrcounted[PecaEnum.BISPO] } peça(s)
Cavalo: ${ arrcounted[PecaEnum.CAVALO] } peça(s)
Torre: ${ arrcounted[PecaEnum.TORRE] } peça(s)
Rainha: ${ arrcounted[PecaEnum.RAINHA] } peça(s)
Rei: ${ arrcounted[PecaEnum.REI] } peça(s)`);

})();