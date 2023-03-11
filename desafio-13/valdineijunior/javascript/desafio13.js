const file = process.argv[2];
const notacaoInicial = file;
const casaInicial = converteNotacaoInicialEmNumero(notacaoInicial);
const resultado = [];
const tamanhoTabuleiro = 8;
const possibilidades = montarPossibilidadesDoTabuleiro(tamanhoTabuleiro);

contabilizandoMovimento(casaInicial, possibilidades, resultado);
passeioDoCavalo(casaInicial, possibilidades, resultado);

console.table(resultado);
for (let index = 0; index < resultado.length; index++) {
    const notacaoNumerica = resultado[index];
    console.log(converteNotacaoInicialEmNumero(notacaoNumerica));
}

function converteNotacaoInicialEmNumero(notacaoInicial) {
    const letrasDeReferenciaDasCasas = ["a", "b", "c", "d", "e", "f", "g", "h"];
    if (typeof notacaoInicial === "string") {
        const notacaoEmNumeros = notacaoInicial.split("");
        notacaoEmNumeros[0] = (
            letrasDeReferenciaDasCasas.findIndex((elemenet) => elemenet === notacaoEmNumeros[0]) + 1
        );
        notacaoEmNumeros[1] = parseInt(notacaoEmNumeros[1]);
        return notacaoEmNumeros;
    } else {
        notacaoInicial[0] = letrasDeReferenciaDasCasas[notacaoInicial[0] - 1];
        notacaoInicial[1] = notacaoInicial[1].toString();
        const notacaoEmString = notacaoInicial[0] + notacaoInicial[1];
        return notacaoEmString;
    }
}

function montarPossibilidadesDoTabuleiro(tamanho) {
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

function contabilizandoMovimento(novaCasa, possibilidades, result) {
    const casaASerMovimentada = possibilidades.findIndex(
        (element) => element[0] === novaCasa[0] && element[1] === novaCasa[1]
    );
    result.push(possibilidades[casaASerMovimentada]);
    if (casaASerMovimentada < possibilidades.length - 1) {
        possibilidades[casaASerMovimentada] = possibilidades.pop();
    } else {
        possibilidades.pop();
    }
}

function reverteUltimoMovimento(novaCasa, possibilidades, resultado) {
    possibilidades.push(resultado.pop());
    novaCasa = resultado[resultado.length - 1];
}

function passeioDoCavalo(casaAtual, possibilidades) {
    const jogadasPossiveis = coletaJogadasPossiveisDandoPreferenciaPelasComMenoresPossibilidades(casaAtual, possibilidades);
    for (let index = 0; index < jogadasPossiveis.length; index++) {
        const jogada = jogadasPossiveis[index];
        const novaCasa = [casaAtual[0] + jogada[0], casaAtual[1] + jogada[1]];
        // console.log(resultado)
        contabilizandoMovimento(novaCasa, possibilidades, resultado);
        passeioDoCavalo(novaCasa, possibilidades, resultado);
        if (possibilidades.length > 2) {
            reverteUltimoMovimento(novaCasa, possibilidades, resultado);
        } else {
            return;
        }
    }
}

function coletaJogadasPossiveisDandoPreferenciaPelasComMenoresPossibilidades(casa, possibilidades) {
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
    const possibilidadesCantos = [[1, 1], [8, 8], [1, 8], [8, 1]];
    const possibilidadesBordaTabuleiro = coletarBordasDoTabuleiro(possibilidades, tamanhoTabuleiro, 1);
    const possibilidadesSegundaCasaApartirDaBordaTabuleiro = coletarBordasDoTabuleiro(possibilidades, tamanhoTabuleiro, 2);
    const movimentosQueVaoParaOsCantos = [];
    const movimentosQueVaoParaBorda = [];
    const MovimentosQueVaoParaSegundaCasaApartirDaBordas = [];
    const movimentosQueVaoParaOCentro = [];
    for (let i = 0; i < movimentosPossiveisParaOCavalo.length; i++) {
        const movimentoDoCavalo = movimentosPossiveisParaOCavalo[i];
        const casaAlvo = [casa[0] + movimentoDoCavalo[0], casa[1] + movimentoDoCavalo[1]];
        const indexPossibilidadesRestantes = possibilidades.findIndex((element) => element[0] === casaAlvo[0] && element[1] === casaAlvo[1]);
        const indexSegundaCasaApartirDaBorda = possibilidadesSegundaCasaApartirDaBordaTabuleiro.findIndex((element) => element[0] === casaAlvo[0] && element[1] === casaAlvo[1]);
        const indexCasaDaBorda = possibilidadesBordaTabuleiro.findIndex((element) => element[0] === casaAlvo[0] && element[1] === casaAlvo[1]);
        const indexCantos = possibilidadesCantos.findIndex((element) => element[0] === casaAlvo[0] && element[1] === casaAlvo[1]);
        const jogadaMoveParaABordaEEstaNasPossibilidades = indexCasaDaBorda !== -1 && indexPossibilidadesRestantes !== -1;
        const jogadaMoveParaSegundaCasaApartirDaBordaEEstaNasPossibilidades = indexSegundaCasaApartirDaBorda !== -1 && indexPossibilidadesRestantes !== -1;
        const jogadaMoveParaOCentroEEstaNasPossibilidades = indexCasaDaBorda === -1 && indexPossibilidadesRestantes !== -1;
        const jogadaMoveParaOCantoEEstaNasPossibilidades = indexCantos === -1 && indexPossibilidadesRestantes !== -1;
        if (jogadaMoveParaOCantoEEstaNasPossibilidades) {
            movimentosQueVaoParaOsCantos.push(movimentoDoCavalo);
        } else if (jogadaMoveParaABordaEEstaNasPossibilidades) {
            movimentosQueVaoParaBorda.push(movimentoDoCavalo);
        } else if (jogadaMoveParaSegundaCasaApartirDaBordaEEstaNasPossibilidades) {
            MovimentosQueVaoParaSegundaCasaApartirDaBordas.push(movimentoDoCavalo);
        } else if (jogadaMoveParaOCentroEEstaNasPossibilidades) {
            movimentosQueVaoParaOCentro.push(movimentoDoCavalo);
        }
    }
    const jogadasPossiveisOrdenadasPelasPeriferias = movimentosQueVaoParaOsCantos.concat(movimentosQueVaoParaBorda).concat(MovimentosQueVaoParaSegundaCasaApartirDaBordas).concat(movimentosQueVaoParaOCentro);
    return jogadasPossiveisOrdenadasPelasPeriferias;
}
