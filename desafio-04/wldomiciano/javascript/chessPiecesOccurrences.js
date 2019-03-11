const input1 = `
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 1 1 0 0 0
  0 0 0 1 1 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
`;

const input2 = `
  4 3 2 5 6 2 3 4
  1 1 1 1 1 1 1 1
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  1 1 1 1 1 1 1 1
  4 3 2 5 6 2 3 4
`;

function printOccurrences(input) {
  const inputArray = input.trim().split(/\s+/);
  const occurrences = new Array(7).fill(0);
  inputArray.forEach(e => occurrences[e]++);

  console.log('Peão:', occurrences[1], 'peça(s)');
  console.log('Bispo:', occurrences[2], 'peça(s)');
  console.log('Cavalo:', occurrences[3], 'peça(s)');
  console.log('Torre:', occurrences[4], 'peça(s)');
  console.log('Rainha:', occurrences[5], 'peça(s)');
  console.log('Rei:', occurrences[6], 'peça(s)');
}

console.log('Exemplo 1');
printOccurrences(input1);

console.log('\nExemplo 2');
printOccurrences(input2);
