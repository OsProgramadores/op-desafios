package entities

import java.util.ArrayDeque

class AreaStat(var tot: Double, `fun`: Funcionario) {
    var qtd = 0
    var listaFuncionario = ArrayDeque<Funcionario>()
    var listaFuncionario2 = ArrayDeque<Funcionario>()
    var menorSalario: Double = 0.toDouble()
    var maiorSalario: Double = 0.toDouble()

    init {
        this.qtd = 1
        this.listaFuncionario.addFirst(`fun`)
        this.listaFuncionario2.addFirst(`fun`)
        this.maiorSalario = tot
        this.menorSalario = tot
    }
}
