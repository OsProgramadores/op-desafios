//
// Desafio 04 - Contabilizar Peças de Xadrez
//
// Proposta de resolução em Swift por Bernardo Campos
//

import Foundation

// Key. nomePeca (n de pecas por time)
// 1. Peão (8)
// 2. Bispo (2)
// 3. Cavalo (2)
// 4. Torre (2)
// 5. Rainha (1)
// 6. Rei (1)

// Tabuleiro de Xadrez
let tabuleiro = [4, 3, 2, 5, 6, 2, 3, 4,
                 1, 1, 1, 1, 1, 1, 1 ,1,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 4, 3, 2, 5, 6, 2, 3, 4]

// Criando dicionário e contando os valores semelhantes
let dicionarioPecas = Dictionary(grouping: tabuleiro, by: { $0 })
let contagemPecas = dicionarioPecas.mapValues { (value: [Int]) in
    return value.count
}

// Imprimindo o resultado
print("Peão: \(dicionarioPecas[1]?.count ?? 0) peça (s)")
print("Bispo: \(dicionarioPecas[2]?.count ?? 0) peça (s)")
print("Cavalo: \(dicionarioPecas[3]?.count ?? 0) peça (s)")
print("Torre: \(dicionarioPecas[4]?.count ?? 0) peça (s)")
print("Rainha: \(dicionarioPecas[5]?.count ?? 0) peça (s)")
print("Rei: \(dicionarioPecas[6]?.count ?? 0) peça (s)")
