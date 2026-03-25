package opdesafios

import com.jsoniter.JsonIterator
import com.jsoniter.output.EncodingMode
import com.jsoniter.output.JsonStream
import com.jsoniter.spi.DecodingMode
import com.koloboke.collect.map.ObjObjMap
import com.koloboke.collect.map.hash.HashObjObjMaps
import entities.Area
import entities.AreaStat
import entities.Funcionario
import entities.LastNameConfig

import java.io.BufferedWriter
import java.io.File
import java.io.FileInputStream
import java.io.FileNotFoundException
import java.io.IOException
import java.io.OutputStreamWriter
import java.util.ArrayDeque

object App {
    private var maior = 0.0
    private var min = java.lang.Double.MAX_VALUE
    private var minArea = Integer.MAX_VALUE
    private var maxArea = 1

    private val out = BufferedWriter(OutputStreamWriter(System.out))

    @Throws(FileNotFoundException::class)
    @JvmStatic
    fun main(args: Array<String>) {
        if (args.size != 1) {
            println("Digite java -jar target/desafio5-1.0.jar <nome-arquivo>")
            return
        }

        val areaFuncionario = HashObjObjMaps.newMutableMap<String, AreaStat>()

        try {
            val inputStream = FileInputStream(File(args[0]))

            val bufferSize = 4096

            JsonIterator.setMode(DecodingMode.DYNAMIC_MODE_AND_MATCH_FIELD_WITH_HASH)
            JsonStream.setMode(EncodingMode.DYNAMIC_MODE)

            val jsonIterator = JsonIterator.parse(inputStream, bufferSize)

            var field: String? = jsonIterator.readObject()
            while (field != null) {
                when (field) {
                    "funcionarios" -> handleFuncionarios(jsonIterator, areaFuncionario)
                    "areas" -> handleArea(jsonIterator, areaFuncionario)
                    else -> jsonIterator.skip()
                }

                field = jsonIterator.readObject()
            }

            out.close()
        } catch (e: Exception) {
            println("Erro ao ler o código")
            e.printStackTrace()
        }

    }

    @Throws(IOException::class)
    private fun handleArea(jp: JsonIterator, areaFuncionario: ObjObjMap<String, AreaStat>) {

        while (jp.readArray()) {
            val area = createArea(jp)

            try {
                val areaStat = areaFuncionario[area.codigo]

                val qtd = areaStat!!.qtd

                if (qtd == maxArea) {
                    out.write(String.format("most_employees|%s|%d\n", area.nome, qtd))
                } else if (qtd == minArea) {
                    out.write(String.format("least_employees|%s|%d\n", area.nome, qtd))
                }

                out.write("area_avg|" + area.nome + "|" +
                        String.format("%.2f", areaStat.tot / qtd).replace(',', '.') + "\n")


                for (`fun` in areaStat.listaFuncionario) {
                    val salario = `fun`.salario

                    if (salario == maior) {
                        out.write("global_max|")
                        addNameSalary(`fun`, salario)
                    }

                    out.write("area_max|" + area.nome + "|")
                    addNameSalary(`fun`, salario)
                }

                for (`fun` in areaStat.listaFuncionario2) {
                    val salario = `fun`.salario

                    if (salario == min) {
                        out.write("global_min|")
                        addNameSalary(`fun`, salario)
                    }

                    out.write("area_min|" + area.nome + "|")
                    addNameSalary(`fun`, salario)
                }
            } catch (e: NullPointerException) {
                // ignore
            } catch (e: IOException) {
            }

        }
    }

    @Throws(IOException::class)
    private fun createArea(jp: JsonIterator): Area {
        var codigo: String? = null
        var nome: String? = null

        var field: String? = jp.readObject()
        while (field != null) {
            when (field) {
                "nome" -> nome = jp.readString()
                "codigo" -> codigo = jp.readString()
                else -> jp.skip()
            }
            field = jp.readObject()
        }

        return Area(codigo, nome)
    }

    @Throws(IOException::class)
    private fun handleFuncionarios(jp: JsonIterator, areaFuncionario: ObjObjMap<String, AreaStat>) {
        var qtd = 0
        var tot = 0.0

        val listaNome = HashObjObjMaps.newMutableMap<String, LastNameConfig>()

        while (jp.readArray()) {

            val func = jp.read(Funcionario::class.java)

            val salario = func.salario

            maior = if (salario > maior) salario else maior
            min = if (salario < min) salario else min

            qtd++
            tot += salario

            val sobrenome = func.sobrenome

            try {
                val lastNameConfig = listaNome[sobrenome]

                lastNameConfig!!.qtd++

                if (lastNameConfig.maiorSalario < salario) {
                    lastNameConfig.maiorSalario = salario
                    lastNameConfig.listaFun = ArrayDeque()
                    lastNameConfig.listaFun.addFirst(func)
                }
            } catch (e: NullPointerException) {
                val lastNameConfig = LastNameConfig(salario, func)
                listaNome[sobrenome] = lastNameConfig
            }

            val area = func.area

            try {
                val areaStat = areaFuncionario[area]
                areaStat!!.qtd++

                areaStat.tot += salario

                if (areaStat.maiorSalario < salario) {
                    areaStat.maiorSalario = salario
                    areaStat.listaFuncionario = ArrayDeque()
                    areaStat.listaFuncionario.addFirst(func)
                } else if (areaStat.maiorSalario == salario) {
                    areaStat.listaFuncionario.addFirst(func)
                }

                if (areaStat.menorSalario > salario) {
                    areaStat.menorSalario = salario
                    areaStat.listaFuncionario2 = ArrayDeque()
                    areaStat.listaFuncionario2.addFirst(func)
                } else if (areaStat.menorSalario == salario) {
                    areaStat.listaFuncionario2.addFirst(func)
                }
            } catch (e: Throwable) {
                val areaStat = AreaStat(salario, func)
                areaFuncionario[area] = areaStat
            }

        }

        for ((_, areaStat) in areaFuncionario) {

            maxArea = if (areaStat.qtd > maxArea) areaStat.qtd else maxArea
            minArea = if (areaStat.qtd < minArea) areaStat.qtd else minArea
        }

        for ((key, value) in listaNome) {
            if (value.qtd > 1) {
                for (funcionario in value.listaFun) {
                    out.write(String.format("last_name_max|%s|", key))
                    addNameSalary(funcionario, funcionario.salario)
                }
            }
        }

        out.write("global_avg|" + String.format("%.2f", tot / qtd).replace(',', '.') + "\n")
    }

    @Throws(IOException::class)
    private fun addNameSalary(`fun`: Funcionario, salario: Double) {
        out.write(String.format("%s %s|%.2f\n", `fun`.nome,
                `fun`.sobrenome, salario).replace(',', '.'))
    }
}


