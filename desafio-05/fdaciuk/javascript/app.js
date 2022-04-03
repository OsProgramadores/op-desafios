#!/usr/bin/env node

'use strict'

const { Transform } = require('stream')
const { createReadStream } = require('fs')

function finish () {
  console.log(formatFuncionariosQueRecebemMais())
  console.log(formatFuncionariosQueRecebemMenos())
  console.log(formatMediaSalarial())

  console.log(formatQuemRecebeMaisPorArea())
  console.log(formatQuemRecebeMenosPorArea())
  console.log(formatMediaSalarialPorArea())

  console.log(formatAreasComMaisFuncionarios())
  console.log(formatAreasComMenosFuncionarios())
  console.log(formatMaioresSalariosPorSobrenome())
}

let areas = {}
let maiorSalario = 0
let menorSalario = Number.MAX_SAFE_INTEGER
let somaDosSalarios = 0
let quantidadeFuncionarios = 0
let recebemMais = []
let recebemMenos = []

let maiorSalarioPorArea = {}
let menorSalarioPorArea = {}
let somaDosSalariosPorArea = {}
let quantidadeDeFuncionariosPorArea = {}
let recebemMaisPorArea = {}
let recebemMenosPorArea = {}

let maiorSalarioPorSobrenome = {}
let recebemMaisPorSobrenome = {}

function formatFuncionariosQueRecebemMais () {
  return formatArray(recebemMais, (funcionario) =>
    patterns.funcionariosQueRecebemMais
      .replace('<nome_completo>', `${funcionario.nome} ${funcionario.sobrenome}`)
      .replace('<salario>', funcionario.salario.toFixed(2))
  )
}

function formatFuncionariosQueRecebemMenos () {
  return formatArray(recebemMenos, (funcionario) =>
    patterns.funcionariosQueRecebemMenos
      .replace('<nome_completo>', `${funcionario.nome} ${funcionario.sobrenome}`)
      .replace('<salario>', funcionario.salario.toFixed(2))
  )
}

function formatMediaSalarial () {
  return patterns.mediaSalarial.replace(
    '<media_salarial>',
    (somaDosSalarios / quantidadeFuncionarios).toFixed(2),
  )
}

function formatQuemRecebeMaisPorArea () {
  const result = Object.entries(recebemMaisPorArea).reduce((acc, [area, funcionarios]) => {
    acc[area] = formatArray(funcionarios, (funcionario) => {
      return patterns.quemRecebeMaisPorArea
        .replace('<nome_da_area>', areas[area])
        .replace('<nome_completo>', `${funcionario.nome} ${funcionario.sobrenome}`)
        .replace('<salario>', funcionario.salario.toFixed(2))
    })

    return acc
  }, {})

  return Object.values(result).join('\n')
}

function formatQuemRecebeMenosPorArea () {
  const result = Object.entries(recebemMenosPorArea).reduce((acc, [area, funcionarios]) => {
    acc[area] = formatArray(funcionarios, (funcionario) => {
      return patterns.quemRecebeMenosPorArea
        .replace('<nome_da_area>', areas[area])
        .replace('<nome_completo>', `${funcionario.nome} ${funcionario.sobrenome}`)
        .replace('<salario>', funcionario.salario.toFixed(2))
    })

    return acc
  }, {})

  return Object.values(result).join('\n')
}

function formatMediaSalarialPorArea () {
  return Object.entries(somaDosSalariosPorArea).map(([area, somaDosSalarios]) => {
    return patterns.mediaSalarialPorArea
      .replace('<nome_da_area>', areas[area])
      .replace('<media_salarial>', (somaDosSalarios / quantidadeDeFuncionariosPorArea[area]).toFixed(2))
  }).join('\n')
}

function formatAreasComMaisFuncionarios () {
  const max = Math.max.apply(null, Object.values(quantidadeDeFuncionariosPorArea))
  const result = Object.entries(quantidadeDeFuncionariosPorArea)
    .map(([area, amount]) => ({ area, amount }))
    .find(({ amount }) => amount === max)

  return patterns.areasComMaisFuncionarios
    .replace('<nome_da_area>', areas[result.area])
    .replace('<numero_de_funcionarios>', result.amount)
}

function formatAreasComMenosFuncionarios () {
  const min = Math.min.apply(null, Object.values(quantidadeDeFuncionariosPorArea))
  const result = Object.entries(quantidadeDeFuncionariosPorArea)
    .map(([area, amount]) => ({ area, amount }))
    .find(({ amount }) => amount === min)

  return patterns.areasComMenosFuncionarios
    .replace('<nome_da_area>', areas[result.area])
    .replace('<numero_de_funcionarios>', result.amount)
}

function formatMaioresSalariosPorSobrenome () {
  const result = Object.entries(recebemMaisPorSobrenome).reduce((acc, [sobrenome, funcionarios]) => {
    acc[sobrenome] = formatArray(funcionarios, (funcionario) => {
      return patterns.maioresSalariosPorSobrenome
        .replace('<sobrenome_do_funcionario>', sobrenome)
        .replace('<nome_completo>', `${funcionario.nome} ${sobrenome}`)
        .replace('<salario>', funcionario.salario.toFixed(2))
    })

    return acc
  }, {})

  return Object.values(result).join('\n')
}

function formatArray (data, func) {
  return data.map(func).join('\n')
}

function calculaFuncionarios (chunk) {
  const chunkString = chunk.toString()

  const funcionarios = JSON.parse(chunkString).data

  for (const funcionario of funcionarios) {
    quantidadeFuncionarios++

    // Cálculo geral
    somaDosSalarios += funcionario.salario

    if (funcionario.salario >= maiorSalario) {
      maiorSalario = funcionario.salario
      recebemMais = recebemMais
        .filter(f => f.salario === maiorSalario)
        .concat(funcionario)
    }

    if (funcionario.salario <= menorSalario) {
      menorSalario = funcionario.salario
      recebemMenos = recebemMenos
        .filter(f => f.salario === menorSalario)
        .concat(funcionario)
    }

    // Cálculo por sobrenome
    if (maiorSalarioPorSobrenome[funcionario.sobrenome] === undefined) {
      maiorSalarioPorSobrenome[funcionario.sobrenome] = 0
    }

    if (funcionario.salario >= maiorSalarioPorSobrenome[funcionario.sobrenome]) {
      maiorSalarioPorSobrenome[funcionario.sobrenome] = funcionario.salario
      recebemMaisPorSobrenome[funcionario.sobrenome] = (recebemMaisPorSobrenome[funcionario.sobrenome] || [])
        .filter(f => f.salario === maiorSalarioPorSobrenome[funcionario.sobrenome])
        .concat(funcionario)
    }

    // Cálculo por área
    const area = funcionario.area

    if (quantidadeDeFuncionariosPorArea[area] === undefined) {
      quantidadeDeFuncionariosPorArea[area] = 0
    }
    quantidadeDeFuncionariosPorArea[area]++

    if (somaDosSalariosPorArea[area] === undefined) {
      somaDosSalariosPorArea[area] = 0
    }
    somaDosSalariosPorArea[area] += funcionario.salario

    if (maiorSalarioPorArea[area] === undefined) {
      maiorSalarioPorArea[area] = 0
    }

    if (funcionario.salario >= maiorSalarioPorArea[area]) {
      maiorSalarioPorArea[area] = funcionario.salario
      recebemMaisPorArea[area] = (recebemMaisPorArea[area] || [])
        .filter(f => f.salario === maiorSalarioPorArea[area])
        .concat(funcionario)
    }

    if (menorSalarioPorArea[area] === undefined) {
      menorSalarioPorArea[area] = Number.MAX_SAFE_INTEGER
    }

    if (funcionario.salario <= menorSalarioPorArea[area]) {
      menorSalarioPorArea[area] = funcionario.salario
      recebemMenosPorArea[area] = (recebemMenosPorArea[area] || [])
        .filter(f => f.salario === menorSalarioPorArea[area])
        .concat(funcionario)
    }
  }
}

const patterns = {
  funcionariosQueRecebemMais: 'global_max|<nome_completo>|<salario>',
  funcionariosQueRecebemMenos: 'global_min|<nome_completo>|<salario>',
  mediaSalarial: 'global_avg|<media_salarial>',
  quemRecebeMaisPorArea: 'area_max|<nome_da_area>|<nome_completo>|<salario>',
  quemRecebeMenosPorArea: 'area_min|<nome_da_area>|<nome_completo>|<salario>',
  mediaSalarialPorArea: 'area_avg|<nome_da_area>|<media_salarial>',
  areasComMaisFuncionarios: 'most_employees|<nome_da_area>|<numero_de_funcionarios>',
  areasComMenosFuncionarios: 'least_employees|<nome_da_area>|<numero_de_funcionarios>',
  maioresSalariosPorSobrenome: 'last_name_max|<sobrenome_do_funcionario>|<nome_completo>|<salario>',
}

function wrapper (key, string) {
  return string && `{"key":"${key}","data":[${string}]}`
}

function parse () {
  const key = 'funcionarios'
  const arrayFuncionariosStart = `"${key}":[`
  const arrayEnd = ']'
  const objectStart = /^{/
  const objectEnd = /},?$/

  let tempChunk = ''

  let arrayStart = 0
  let firstIndex = -1
  let lastIndex = -1
  let counter = 0

  let firstIndexArea = -1
  let lastIndexArea = -1

  const arrayAreasStart = `"areas":[`

  return new Transform({
    transform (chunk, encoding, callback) {
      counter++
      const thisChunk = chunk.toString().split(/\n\s+/).join('')

      // achou o começo do array de areas
      if (thisChunk.includes(arrayAreasStart)) {
        firstIndexArea = thisChunk.indexOf(arrayAreasStart)
        lastIndexArea = thisChunk.indexOf(arrayEnd, firstIndexArea)
      }

      // tem começo e fim no mesmo chunk (areas)
      if (thisChunk.includes(arrayAreasStart) && lastIndexArea > -1) {
        const jsonArray = thisChunk.substring(firstIndexArea, lastIndexArea)
          .split(arrayAreasStart)
          .join('')
          .split('},{')
          .join('},\n{')

        areas = jsonArray.split('\n').reduce((acc, area) => {
          if (!area) return acc
          const parsedArea = JSON.parse(area.replace(/,$/, ''))
          acc[parsedArea.codigo] = parsedArea.nome
          return acc
        }, {})
      }

      // achou o começo do array de funcionarios
      if (thisChunk.includes(arrayFuncionariosStart)) {
        arrayStart++

        firstIndex = thisChunk.indexOf(arrayFuncionariosStart)
        lastIndex = thisChunk.indexOf(arrayEnd, firstIndex)
      }

      // tem começo e fim no mesmo chunk
      if (thisChunk.includes(arrayFuncionariosStart) && lastIndex > -1) {
        arrayStart--

        const jsonArray = thisChunk.substring(firstIndex, lastIndex)
          .split(arrayFuncionariosStart)
          .join('')
          .split('},{')
          .join('},\n{')

        this.push(wrapper(key, jsonArray))

        firstIndex = -1
        lastIndex = -1
      }

      // primeira passagem pelo chunk
      if (lastIndex === -1 && arrayStart > 0 && counter === 1) {
        lastIndex = thisChunk.indexOf(arrayEnd)
        const jsonArray = thisChunk
          .split('\n')
          .join('')
          .split('},{')
          .join('},\n{')

        let result = jsonArray.split('\n').reduce((acc, funcionario, index, array) => {
          if (index === 0) {
            const cleanFirstLine = funcionario.replace(`{${arrayFuncionariosStart}`, '')
            acc.push(cleanFirstLine)
          }
          else if (array.length === index + 1) {
            // último índice. Verificar se ele está completo antes de comitar
            const isChunkComplete = objectEnd.test(funcionario)
            if (isChunkComplete) {
              acc.push(funcionario.replace(/,$/, ''))
            }
            else {
              tempChunk = funcionario
            }

          }
          else {
            acc.push(funcionario)
          }

          return acc
        }, [])

        // Remove a vírgula do último objeto
        result[result.length - 1] = result[result.length - 1].replace(/,$/, '')

        this.push(wrapper(key, result.join('')))

        if (lastIndex > -1) {
          arrayStart--
          lastIndex = -1
        }
      }

      // já começou, mas não tem todos os itens ainda
      if (firstIndex > 0 && lastIndex === -1 && arrayStart > 0 && counter > 1) {
        lastIndex = thisChunk.indexOf(arrayEnd)
        const chunkToIterate = lastIndex > -1
          ? thisChunk.substring(0, lastIndex)
          : thisChunk

        const jsonArray = chunkToIterate
          .split('\n')
          .join('')
          .split('},{')
          .join('},\n{')

        const result = jsonArray.split('\n').reduce((acc, funcionario, index, array) => {
          if (index === 0) {
            // primeiro item
            const isChunkComplete = objectStart.test(funcionario)

            if (isChunkComplete) {
              acc.push(funcionario)
            }
            else {
              acc.push(`${tempChunk}${funcionario}`.replace(/^,/, ''))
              tempChunk = ''
            }
          }
          else if (array.length === index + 1) {
            // último item
            const isChunkComplete = objectEnd.test(funcionario)
            if (isChunkComplete) {
              acc.push(funcionario)
            }
            else {
              tempChunk = funcionario
            }
          }
          else {
            acc.push(funcionario)
          }

          return acc
        }, [])

        // Remove a vírgula do último objeto
        result[result.length - 1] = result[result.length - 1].replace(/,$/, '')

        this.push(wrapper(key, result.join('')))

        if (lastIndex > -1) {
          arrayStart--
          lastIndex = -1
        }
      }

      callback()
    }
  })
}

const file = process.argv[2]
const pipeline = createReadStream(file, { encoding: 'utf8' })
  .pipe(parse())

pipeline.on('data', calculaFuncionarios)
pipeline.on('end', finish)
