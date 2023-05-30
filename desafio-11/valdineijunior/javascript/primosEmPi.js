const fs = require("fs");
const filePath = process.argv[2];
if (!filePath) {
    console.error("Erro: Caminho do arquivo não fornecido. Utilize 'node primosEmPi.js pi-1M.txt'");
    process.exit(1);
}

function isPrimo(numero) {
    if (numero === 2) {
        return true;
    }
    if (numero < 2 || numero % 2 === 0) {
        return false;
    }
    const raizQuadradaDoNumero = Math.sqrt(numero);
    for (let index = 3; index <= raizQuadradaDoNumero; index += 2) {
        if (numero % index === 0) {
            return false;
        }
    }
    return true;
}

function obterNumerosPrimos(primoInicial, primoFinal) {
    const primos = new Set();
    for (let numero = primoInicial; numero <= primoFinal; numero++) {
        if (isPrimo(numero)) {
            primos.add(numero);
        }
    }
    return primos;
}

function coletarMaiorSequencia(indexDeInicio, sequenciaDeDigitosAtuais) {
    let digitosAdcionais = "";
    let sequenciaAtualizada = "";
    for (let i = indexDeInicio; i < indexDeInicio + 4 && i < arrayComNumerosdosDigitosEmPi.length; i++) {
        digitosAdcionais += arrayComNumerosdosDigitosEmPi[i];
        const recorteDeNumeros = parseInt(digitosAdcionais);
        const recortePertenceAosprimos = numerosPrimos.has(recorteDeNumeros);
        if (recortePertenceAosprimos) {
            sequenciaAtualizada = sequenciaDeDigitosAtuais + digitosAdcionais;
            coletarMaiorSequencia(i + 1, sequenciaAtualizada);
        }
    }
    if (sequenciaAtualizada.length > maiorDasSequencias.length) {
        maiorDasSequencias = sequenciaAtualizada;
    }
}

const PrimeirasUmMilhaoDeCasasDecimaisEmPi = fs.readFileSync(filePath, "utf-8").slice(2);
const arrayComNumerosdosDigitosEmPi = PrimeirasUmMilhaoDeCasasDecimaisEmPi.split("").map(Number);
const primeiroPrimo = 2;
const ultimoPrimo = 9973;
const numerosPrimos = obterNumerosPrimos(primeiroPrimo, ultimoPrimo);
let maiorDasSequencias = "";
for (let index = 0; index < arrayComNumerosdosDigitosEmPi.length; index++) {
    const digitosQueFaltamSerProcessados = arrayComNumerosdosDigitosEmPi.length - index;
    const linhasQueFaltamSerProcessadasEmenorQuemaiorDasSequenciasJaEncontrada = maiorDasSequencias.length > digitosQueFaltamSerProcessados;
    if (linhasQueFaltamSerProcessadasEmenorQuemaiorDasSequenciasJaEncontrada) {
        break;
    }
    const sequenciaInicial = "";
    coletarMaiorSequencia(index, sequenciaInicial);
}

console.log(maiorDasSequencias);
