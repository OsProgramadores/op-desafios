package entities

import java.util.ArrayDeque

class AreaStat(var tot: Double, `fun`: Funcionario) {
    var qtd: Int = 0
    val listaFuncionario = ArrayDeque<Funcionario>()
    val listaFuncionario2 = ArrayDeque<Funcionario>()
    var maiorSalario: Double = 0.0
    var menorSalario: Double = 0.0

    init {
        qtd = 1
        listaFuncionario.addFirst(`fun`)
        listaFuncionario2.addFirst(`fun`)
        maiorSalario = tot
        menorSalario = tot
    }

    fun add(){
        qtd++
    }

    fun incrementTot(sal:Double){
        tot += sal
    }
}
