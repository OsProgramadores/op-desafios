export enum PecaEnum {
  VASIO,
  PEAO,
  BISPO,
  CAVALO,
  TORRE,
  RAINHA,
  REI
}; 

export const countPartsFromVector = (vector:any) => {
  const result = [0,0,0,0,0,0,0];

  for (var i = 0; i < vector.length; i++) {
    for (var x = 0; x < vector[i].length; x++) {
      const part = vector[i][x];
      result[part]++;
    }
  }

  return result;
}