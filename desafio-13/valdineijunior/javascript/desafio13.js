const file = process.argv[2];
const notacaoInicial = file;
const casaInicial = converteOuReverteNotacaoDeLetraParaNumero(notacaoInicial);
const resultado = [];
const tamanhoTabuleiro = 8;
const possibilidades = geraAsPossibilidadesDoTabuleiro(tamanhoTabuleiro);
contabilizaMovimento(casaInicial, possibilidades, resultado);
main(casaInicial, possibilidades, resultado);
for (let index = 0; index < resultado.length; index++) {
    const notacaoNumerica = resultado[index];
    console.log(converteOuReverteNotacaoDeLetraParaNumero(notacaoNumerica));
}

function converteOuReverteNotacaoDeLetraParaNumero(notacaoInicial) {
    const referenciaCasas = ["a", "b", "c", "d", "e", "f", "g", "h"];
    if (typeof notacaoInicial === "string") {
        const notacaoEmNumeros = notacaoInicial.split("");
        notacaoEmNumeros[0] = (
            referenciaCasas.findIndex((elemenet) => elemenet === notacaoEmNumeros[0]) + 1
        );
        notacaoEmNumeros[1] = parseInt(notacaoEmNumeros[1]);
        return notacaoEmNumeros;
    } else {
        notacaoInicial[0] = referenciaCasas[notacaoInicial[0] - 1];
        notacaoInicial[1] = notacaoInicial[1].toString();
        const notacaoEmString = notacaoInicial[0] + notacaoInicial[1];
        return notacaoEmString;
    }
}

function geraAsPossibilidadesDoTabuleiro(tamanho) {
    const colunas = [];
    for (let index = tamanho; index > 0; index--) {
        colunas.push(index);
    }
    const possibilidadesDoTabuleiro = [];
    for (let i = 0; i < colunas.length; i++) {
        const linha = colunas[i];
        for (let j = colunas.length - 1; j >= 0; j--) {
            const coluna = colunas[j];
            possibilidadesDoTabuleiro.push([linha, coluna]);
        }
    }
    return possibilidadesDoTabuleiro;
}

function contabilizaMovimento(novaCasa, possibilidades, resultado) {
    const antigaCasa = possibilidades.findIndex(
        (element) => element[0] === novaCasa[0] && element[1] === novaCasa[1]
    );
    resultado.push(possibilidades[antigaCasa]);
    if (antigaCasa < possibilidades.length - 1) {
        possibilidades[antigaCasa] = possibilidades.pop();
    } else {
        possibilidades.pop();
    }
}

function reverteUltimoMovimento(novaCasa, possibilidades, resultado) {
    possibilidades.push(resultado.pop());
    novaCasa = resultado[resultado.length - 1];
}

function main(casaAtual, possibilidades) {
    const jogadasPossiveis = coletaMovimentosPossiveis(casaAtual, possibilidades);
    for (let index = 0; index < jogadasPossiveis.length; index++) {
        const jogada = jogadasPossiveis[index];
        const novaCasa = [casaAtual[0] + jogada[0], casaAtual[1] + jogada[1]];
        contabilizaMovimento(novaCasa, possibilidades, resultado);
        main(novaCasa, possibilidades, resultado);
        if (possibilidades.length > 0) {
            reverteUltimoMovimento(novaCasa, possibilidades, resultado);
        } else {
            return;
        }
    }
}

function coletaMovimentosPossiveis(casaAtual, possibilidades) {
    // Essa e a funcao mais importante que coleta os movimentos ordenando pelos que geram menas possibilidades futuramente.
    const possibilidadesCantos = [[1, 1], [8, 8], [1, 8], [8, 1]];
    const possibilidadesBordaTabuleiro = coletarBordasDoTabuleiro(possibilidades, tamanhoTabuleiro, 1);
    const possibilidadesSegundaCasaApartirDaBordaTabuleiro = coletarBordasDoTabuleiro(possibilidades, tamanhoTabuleiro, 2);
    const movimentosPossiveisParaOCavalo = [
        [2, 1],
        [2, -1],
        [1, 2],
        [1, -2],
        [-1, 2],
        [-1, -2],
        [-2, 1],
        [-2, -1]
    ];
    const movimentosParaCantos = [];
    const movimentosParaBorda = [];
    const movimentosParaSegundacasaApartirdaBorda = [];
    const movimentosParaOCentro = [];
    for (let i = 0; i < movimentosPossiveisParaOCavalo.length; i++) {
        const movimento = movimentosPossiveisParaOCavalo[i];
        const casaAlvo = [casaAtual[0] + movimento[0], casaAtual[1] + movimento[1]];
        const verificaSeJogadaPertenceAoCanto = possibilidadesCantos.findIndex((element) => element[0] === casaAlvo[0] && element[1] === casaAlvo[1]);
        const verificaSeJogadaPertenceABorda = possibilidadesBordaTabuleiro.findIndex((element) => element[0] === casaAlvo[0] && element[1] === casaAlvo[1]);
        const verificaSeJogadaPertenceASegundaCasaApartirBorda = possibilidadesSegundaCasaApartirDaBordaTabuleiro.findIndex((element) => element[0] === casaAlvo[0] && element[1] === casaAlvo[1]);
        const indexPossibilidadesRestantes = possibilidades.findIndex((element) => element[0] === casaAlvo[0] && element[1] === casaAlvo[1]);
        if (verificaSeJogadaPertenceAoCanto !== -1 && indexPossibilidadesRestantes !== -1) {
            movimentosParaCantos.push(movimento);
        } else if (verificaSeJogadaPertenceABorda !== -1 && indexPossibilidadesRestantes !== -1) {
            movimentosParaBorda.push(movimento);
        } else if (verificaSeJogadaPertenceASegundaCasaApartirBorda !== -1 && indexPossibilidadesRestantes !== -1) {
            movimentosParaSegundacasaApartirdaBorda.push(movimento);
        } else if (verificaSeJogadaPertenceABorda === -1 && verificaSeJogadaPertenceAoCanto === -1 && indexPossibilidadesRestantes !== -1) {
            movimentosParaOCentro.push(movimento);
        }
    }
    const jogadasPossiveis = movimentosParaCantos.concat(movimentosParaBorda).concat(movimentosParaSegundacasaApartirdaBorda).concat(movimentosParaOCentro);
    return jogadasPossiveis;
}

function coletarBordasDoTabuleiro(possibilidades, tamanhoTabuleiro, casasApartirDaBorda) {
    const casasPertencentesABorda = [];
    for (let index = 0; index < possibilidades.length; index++) {
        const casas = possibilidades[index];
        const coletandoDiagonalSuperior = casas[0] <= 2 - casasApartirDaBorda | casas[1] <= 2 - casasApartirDaBorda;
        const coletandoDiagonalInferior = casas[0] > tamanhoTabuleiro - casasApartirDaBorda | casas[1] > tamanhoTabuleiro - casasApartirDaBorda;
        if (coletandoDiagonalSuperior | coletandoDiagonalInferior) {
            casasPertencentesABorda.push(casas);
        }
    }
    return casasPertencentesABorda;
}
