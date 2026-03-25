package entities

import java.util.ArrayDeque

class LastNameConfig(var maiorSalario: Double, func: Funcionario) {
    var qtd: Int = 0
    var listaFun = ArrayDeque<Funcionario>()

    init {
        this.qtd = 1
        this.listaFun.addFirst(func)
    }
}
