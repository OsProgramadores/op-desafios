const INICIO = 10100;
const FINAL = 12111;

const palindromos = [];

for (let i = INICIO; i <= FINAL; i++) {
    let inverted = "";
    const invertedChars = i.toString().split("").reverse();
    for (let i = 0; i < invertedChars.length; i++) {
        inverted += invertedChars.at(i);
    }
    if (String(i) === inverted) {
        palindromos.push(i);
    }
}

for (const p of palindromos) {
    console.log(p);
}
