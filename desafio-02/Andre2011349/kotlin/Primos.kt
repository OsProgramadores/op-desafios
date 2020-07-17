/* Verifica Primos

desenvolvido por: Andre2011349   email:2011349@aluno.univesp.br
versão 1.0
16 de julho de 2020

Descrição:
Lógica desenvolvida para o desafio 02 do grupo OsProgramadores com o objetivo de identificar os numeros
primos entre 1 e 10000
 */
fun main() {

    // declaração das variáveis
    var Lista_Primos = mutableListOf<String>()
    var Num_Testado : Int = 2
    var Qtd_Divisores : Int = 0
    var Qtd_Primos : Int = 0
    var Num_Max : Int = 10000

         Lista_Primos.clear() // limpa a lista

    for (Indice_1:Int in 1..Num_Max){ // Quantidade de testes a serem feitos.
        Qtd_Divisores=0 // Zera a váriavel para iniciar a verificação.

        for (Indice_2:Int in 1..Num_Testado){ // Loop para testar se o número é primo

            if (Num_Testado % Indice_2 == 0){  // Divide o numero testado pelo indice do loop e verifica se o resto é 0 caso o resto seja 0 incrementa a variavel quantidade de divisores

                Qtd_Divisores +=1 // Quantidade de divisores encontrados para o numero testado
            }

        }
        if (Qtd_Divisores == 2){ // verifica se a quantidade de divisores para o numero testado foram 2
            Lista_Primos.add(Num_Testado.toString()) // caso tenha sido 2 adiciona o numero testado na lista
            Qtd_Primos += 1 // incrementa a quantidade de numeros primos encontrados

        }

        Num_Testado +=1 //incrementa o numero testado para reiniciar o teste com o próximo valor

    }

    // mostra a quantidade de numeros primos encontrados e quais foram estes números
println("Entre os números 1 e 10000 existem $Qtd_Primos números primos.")
    println("E eles são:")
print(Lista_Primos)

}
