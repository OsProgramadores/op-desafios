export const readInput = (argv: string[]): string[] => {
  return argv.slice(2, argv.length);
}

export const stringToMatrix = (str: string[], totalCols: number=8): number[][] => {
  const mat:number[][] = [];

  let row = 0; let col = 0;
  for(let i = 0; i < str.length; i ++) {
   
    if (!mat[row]) {
      mat[row] = [];
    }

    mat[row][col++] = parseInt(str[i]);

    if ((i + 1) % totalCols === 0) {
      row ++;
      col = 0;
    }
  }  

  return mat;
}
