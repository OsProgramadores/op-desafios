const palindromos = [];

let INICIO;
let FINAL;

try {
    const args = process.argv.slice(2);
    if (args.length === 0 || args.length > 2) {
        throw new Error("Forneça no máximo 2 argumentos numéricos ao executar o código");
    }

    INICIO = Number(args[0]);
    FINAL = Number(args[1]);
    if (isNaN(INICIO + FINAL)) {
        throw new Error("Forneça apenas números");
    }

    for (let i = INICIO; i <= FINAL; i++) {
        let inverted = "";
        const chars = i.toString().split("");
        const invertedChars = [];
        for (let i = 0; i < chars.length; i++) {
            invertedChars.push(chars.slice(0, chars.length - i).pop());
        }
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

    console.log(`\n${palindromos.length} palindromos encontrados entre ${INICIO} e ${FINAL}`);
} catch (error) {
    console.error("Um erro ocorreu: ", error.message);
}
