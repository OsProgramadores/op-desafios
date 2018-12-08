package entities

import java.util.*

class LastNameConfig(var maiorSalario: Double, func:Funcionario) {
    var qtd: Int = 0
    val listaFun = ArrayDeque<Funcionario>()

    init {
        qtd = 1
        listaFun.addFirst(func)
    }

    fun increment(){
        qtd++
    }
}
