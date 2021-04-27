import { countPartsFromVector } from './../chess';
import { sToVec } from './../helper';

const initialVector1=
`4 3 2 5 6 2 3 4
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
4 3 2 5 6 2 3 4`;

const initialVector2=
`0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0
0 0 0 1 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0`;

const vector1 = sToVec(initialVector1);
const vector2 = sToVec(initialVector2);

test("Verificar contagem do vetor 1", () => {
  expect(countPartsFromVector(vector1)).toEqual([32,16,4,4,4,2,2]);
});

test("Verificar contagem do vetor 2", () => {
  expect(countPartsFromVector(vector2)).toEqual([60,4,0,0,0,0,0]);
});