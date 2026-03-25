// Implemente o comando tac na sua linguagem e bibliotecas preferidas.
// O programa deve ler arquivos de qualquer tamanho e funcionar com um limite de 512MB de memória.
//
// pacote npm | npm i readline-specific
// $ node --max-old-space-size=512 desafio-07 1GB.txt
//
const fs = require("fs");
const inputFile = process.argv[2];
let lineCount = 1; // 1GB.txt - 13147026 linhas
let i;
let firstLog = true;

const stream = fs.createReadStream(inputFile);
stream.on("data", chunk => {
    for (i = 0; i < chunk.length; ++i) {
		if (chunk[i] == 10) {lineCount++;}
	}
})
.on("end", () => loop());

const loop = () => {if (lineCount > 0) {readLine();}};

const rl = require("readline-specific");
const readLine = () => {
	rl.oneline(inputFile, lineCount, function(err, line) {
		if (err) {return console.error(err);}
		if (firstLog) {
			firstLog = false;
			process.stdout.write(line);
			lineCount--;
			loop();
		} else {
			console.log(line);
			lineCount--;
			loop();
		}
	});
};