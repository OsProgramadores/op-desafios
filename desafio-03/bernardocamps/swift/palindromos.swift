//
//  Imprimir todos os números palindrômicos entre dois outros números
//
//  Created by Bernardo Campos
//

import Foundation

// Criando uma Array de números palindrômicos para armazenar o resultado
var palindromicos: Array<Int> = []

// Determinando o intervalo a ser analisado
var primeiroNumero: UInt64 = 1
var ultimoNumero: UInt64 = 999999

for n in primeiroNumero...ultimoNumero {
    let numero = String(n)
    let numeroInvertido = String(numero.reversed())
    if numero == numeroInvertido {
        palindromicos.append(Int(numero)!)
    }
}

// Resultado
print(palindromicos)
