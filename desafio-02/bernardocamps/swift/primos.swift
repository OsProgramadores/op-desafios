//
//  primos.swift
//  
//
//  Created by Bernardo Campos on 13/02/21.
//

import Foundation

// Solução em Swift para listar todos os números primos entre 1 e 10000
// Método matemático utilizado: Crivo de Eratóstenes

// Determinando o valor limite
var valorLimite: Double = 10000.0

// Raiz quadrada do valor limite nos mostra o maior valor a ser checado
var maiorNumeroParaChecar: Double = valorLimite.squareRoot()

// Convertendo Double para Int pois a função squareRoot() é realizada apenas com Double
var valorLimiteInt: Int = Int(valorLimite)
var maiorNumeroParaChecarInt: Int = Int(maiorNumeroParaChecar)

// Criando a lista de números primos, incluindo o número 2 como primeiro ítem
var listaPrimos = [Int]()
listaPrimos.append(2)

// Sensor de número primo
var sensor: Int = 1

// Iterando entre 3 e o valor limite
for n in 3...valorLimiteInt {
    // Iterando entre os valores da lista de números primos
    for (_, value) in listaPrimos.enumerated() {
        // Caso o resto da divisão seja 0, o número não é primo e o loop é interrompido
        if n % value == 0 && value < maiorNumeroParaChecarInt {
            sensor = 0
            break
        }
    }
    // Após o loop, checar se o sensor é diferente de 0 para adicionar o número encontrado à lista
    if sensor != 0 {
        listaPrimos.append(n)
    }
    sensor = 1
}

// Resultado
print("Existem \(listaPrimos.count) números primos entre 1 e \(valorLimiteInt)")
print(listaPrimos)
