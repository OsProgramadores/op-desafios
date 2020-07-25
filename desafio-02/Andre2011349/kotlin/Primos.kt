/* Verifica Primos

desenvolvido por: Andre2011349   email:2011349@aluno.univesp.br
versão 1.0
16 de julho de 2020

Descrição:
Lógica desenvolvida para o desafio 02 do grupo OsProgramadores com o objetivo de identificar os numeros
primos entre 1 e 10000
O número primo 2 foi previamente inserido na lista para que a mesma não seja inicializada com valor Null */
fun main() {

    // declaração das variáveis
    var Lista_Primos = mutableListOf<Int>()
    var Num_Testado : Int = 3
    var Qtd_Divisores : Int = 0
    var Qtd_Primos : Int = 0
    var Num_Max : Long = 10000


    Lista_Primos.clear() // limpa a lista
    Lista_Primos.add(2) // adiciona o 2 na lista
    for (Indice_1: Long in 2..Num_Max ) { // Quantidade de testes a serem feitos.

        for (Indice_2: Int in 0..(Qtd_Primos)) { // Loop para testar se o número é primo

            if (Num_Testado % Lista_Primos.get(Indice_2) == 0)  {  // Verifica se o numero testado é divisivel por algum numero primo presente na lista
                break
            }else  if (Indice_2 == Qtd_Primos) {
                Lista_Primos.add(Num_Testado) // se nao houve divisores na lista o numero é primo
                Qtd_Primos += 1 // incrementa a quantidade de numeros primos encontrados
            }

        }
        Num_Testado += 1 //incrementa o numero testado para reiniciar o teste com o próximo valor
    }

    // mostra a quantidade de numeros primos encontrados e quais foram estes números
println("Entre os números 1 e $Num_Max existem ${Qtd_Primos +1} números primos.")
    println("E eles são:")
print(Lista_Primos)

}
