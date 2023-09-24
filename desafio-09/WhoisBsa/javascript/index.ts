import fs from 'fs';

const inputs = fs.readFileSync('./data.txt', 'utf8').split('\n');
const CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
const listChar: string[] = CHARS.split('');
const convertedValues: string[] = [];
const convertedList: string[] = [];

inputs.map(input => {
  const [inputBase, outputBase, value] = input.split(' ');

  convertedList.push(convertBase(+inputBase, +outputBase, value));
});

function convertBase(inputBase: number, outputBase: number, value: string): string {
  const decimalValue = baseNtoBase10(inputBase, value);

  let convertedValue = '???';

  if (verifyBase(inputBase, outputBase, value, decimalValue)) {
    base10toBaseN(outputBase, decimalValue);
    convertedValue = convertedValues.join('');
  }

  convertedValues.length = 0;
  return convertedValue || '0';
}

function baseNtoBase10(inputBase: number, value: string): bigint {
  const chars = value.split('').reverse();

  const decimalValue = chars.reduce((acc, char, index) =>
    BigInt(listChar.indexOf(char)) *
    BigInt(BigInt(inputBase) ** BigInt(index)) +
    acc, 
    0n);

  return decimalValue;
}

function base10toBaseN(outputBase: number, value: bigint): void {
  if (value <= 0n) return;

  const remainder = value % BigInt(outputBase);
  const quotient = BigInt((value - remainder)) / BigInt(outputBase);

  convertedValues.unshift(listChar.at(Number(remainder))!);

  base10toBaseN(outputBase, quotient);
}

function verifyBase(inputBase: number, outputBase: number, value: string, decimalValue: bigint): boolean {
  if (inputBase < 2 ||
    inputBase > 62 ||
    outputBase < 2 ||
    outputBase > 62 ||
    +value < 0)
    return false;

  const limit = baseNtoBase10(62, 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz');

  if (decimalValue > limit) return false;

  for (let i = 0; i <= value.length - 1; i++) {
    if (inputBase <= +listChar.indexOf(value[i]))
      return false;
  }

  return true;
}

console.log(convertedList.join('\n'));
