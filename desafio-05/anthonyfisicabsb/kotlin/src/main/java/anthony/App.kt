package anthony

import com.fasterxml.jackson.core.JsonParser
import com.fasterxml.jackson.core.JsonToken
import com.fasterxml.jackson.databind.MappingJsonFactory
import entities.Area
import entities.AreaStat
import entities.Funcionario
import entities.LastNameConfig

import java.io.BufferedWriter
import java.io.File
import java.io.IOException
import java.io.OutputStreamWriter
import java.util.HashMap

object App {
    private var maior = 0.0
    private var min = java.lang.Double.MAX_VALUE
    private var minArea = Integer.MAX_VALUE
    private var maxArea = 1

    private val out = BufferedWriter(OutputStreamWriter(System.out))

    @Throws(IOException::class)
    @JvmStatic
    fun main(args: Array<String>) {
        if (args.size != 1) {
            println("Digite java -jar target/desafio5-1.0.jar <nome-arquivo>")
            System.exit(-1)
        }

        val areaFuncionario = HashMap<String?, AreaStat>()

        val f = MappingJsonFactory()
        var current: JsonToken

        try {
            f.createParser(File(args[0])).use { jp ->
                jp.nextToken()

                while (jp.nextToken() != JsonToken.END_OBJECT) {
                    val field = jp.currentName ?: break

                    current = jp.nextToken()
                    if (field == "funcionarios") {
                        if (current == JsonToken.START_ARRAY) {
                            handleFuncionarios(jp, areaFuncionario)
                        }
                    } else if (field == "areas") {
                        if (current == JsonToken.START_ARRAY) {
                            handleArea(jp, areaFuncionario)
                        }
                    }
                }

                out.close()
            }
        } catch (e: IOException) {
            println("Erro ao ler o codigo!")
            e.printStackTrace()
        }

    }

    @Throws(IOException::class)
    private fun handleArea(jp: JsonParser, areaFuncionario: HashMap<String?, AreaStat>) {
        while (jp.nextToken() != JsonToken.END_ARRAY) {
            val area = jp.readValueAs(Area::class.java)

            var areaStat: AreaStat? = null

            if (areaFuncionario.containsKey(area.codigo)) {
                areaStat = areaFuncionario[area.codigo]
            } else {
                continue
            }

            val qtd = areaStat!!.qtd

            if (qtd == maxArea) {
                out.write("most_employees|" + area.nome + "|" + qtd + "\n")
            } else if (qtd == minArea) {
                out.write("least_employees|" + area.nome + "|" + qtd + "\n")
            }

            out.write("area_avg|" + area.nome + "|" +
                    String.format("%.2f", areaStat.tot / qtd).replace(',', '.') + "\n")

            for (`fun` in areaStat.listaFuncionario) {
                val salario = `fun`.salario!!

                if (salario == maior) {
                    out.write("global_max|")
                    addNameSalary(`fun`, salario)
                }


                out.write("area_max|" + area.nome + "|")
                addNameSalary(`fun`, salario)

            }

            for (`fun` in areaStat.listaFuncionario2) {
                val salario = `fun`.salario!!

                if (salario == min) {
                    out.write("global_min|")
                    addNameSalary(`fun`, salario)
                }

                out.write("area_min|" + area.nome + "|")
                addNameSalary(`fun`, salario)

            }
        }
    }

    @Throws(IOException::class)
    private fun handleFuncionarios(jp: JsonParser, areaFuncionario: HashMap<String?, AreaStat>) {
        var qtd = 0
        var tot = 0.0

        val listaNome = HashMap<String?, LastNameConfig>()

        while (jp.nextToken() != JsonToken.END_ARRAY) {
            val func = jp.readValueAs(Funcionario::class.java)

            val salario = func.salario!!

            maior = if (maior < salario) salario else maior
            min = if (min > salario) salario else min

            qtd++
            tot += salario

            val sobrenome = func.sobrenome

            if (listaNome.containsKey(sobrenome)) {
                listaNome[sobrenome]!!.increment()

                if (listaNome[sobrenome]!!.maiorSalario < salario) {
                    listaNome[sobrenome]!!.maiorSalario = salario
                    listaNome[sobrenome]!!.listaFun.clear()
                    listaNome[sobrenome]!!.listaFun.addFirst(func)

                }
            } else {
                val lastname = LastNameConfig(salario, func)
                listaNome[sobrenome] = lastname
            }

            val area = func.area

            if (areaFuncionario.containsKey(area)) {
                areaFuncionario[area]!!.add()

                areaFuncionario[area]!!.incrementTot(salario)

                if (areaFuncionario[area]!!.maiorSalario < salario) {
                    areaFuncionario[area]!!.maiorSalario = salario
                    areaFuncionario[area]!!.listaFuncionario.clear()
                    areaFuncionario[area]!!.listaFuncionario.addFirst(func)
                } else if (areaFuncionario[area]!!.maiorSalario == salario) {
                    areaFuncionario[area]!!.listaFuncionario.addFirst(func)
                }

                if (areaFuncionario[area]!!.menorSalario > salario) {
                    areaFuncionario[area]!!.menorSalario = salario
                    areaFuncionario[area]!!.listaFuncionario2.clear()
                    areaFuncionario[area]!!.listaFuncionario2.addFirst(func)
                } else if (areaFuncionario[area]!!.menorSalario == salario) {
                    areaFuncionario[area]!!.listaFuncionario2.addFirst(func)
                }
            } else {
                val areaStat = AreaStat(func.salario!!, func)
                areaFuncionario[area] = areaStat
            }
        }

        for (key in areaFuncionario.keys) {
            val stat = areaFuncionario[key]
            maxArea = if (stat!!.qtd > maxArea) stat.qtd else maxArea
            minArea = if (stat!!.qtd < minArea) stat.qtd else minArea
        }

        for (key in listaNome.keys) {
            if (listaNome[key]!!.qtd > 1) {
                for (`fun` in listaNome[key]!!.listaFun) {
                    out.write("last_name_max|$key|")
                    addNameSalary(`fun`, `fun`.salario!!)
                }
            }
        }

        out.write("global_avg|" + String.format("%.2f", tot / qtd).replace(',', '.') + "\n")
    }

    @Throws(IOException::class)
    private fun addNameSalary(`fun`: Funcionario, salary: Double) {
        out.write(`fun`.nome + " " + `fun`.sobrenome + "|" +
                String.format("%.2f", salary).replace(',', '.') + "\n")

    }
}
