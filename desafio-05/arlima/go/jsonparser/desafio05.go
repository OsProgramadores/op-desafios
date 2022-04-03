// Adriano Roberto de Lima
// Funciona com arquivo de 30M de registros em máquina de 8GB de memória
// Pela memória consumida dá para abrir arquivos maiores ainda
// Não tem bom desempenho
// Desafio 05 - em GO !

package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"math"
	"os"

	"github.com/buger/jsonparser"
)

// Funcionario é a estrutura com os dados dos funcionarios no arquivo a ser lido
type Funcionario struct {
	ID        int64   `json:"id"`
	Nome      string  `json:"nome"`
	Sobrenome string  `json:"sobrenome"`
	Salario   float64 `json:"salario"`
	Area      string  `json:"area"`
}

func main() {
	var filename string

	globalmin := math.MaxFloat64
	globalmax := 0.0
	globalavg := 0.0
	contaemp := 0.0
	mostemployees := 0.0
	empmin := []Funcionario{}
	empmax := []Funcionario{}
	nomearea := make(map[string]string)
	empareamin := make(map[string][]Funcionario)
	empareamax := make(map[string][]Funcionario)
	emplastnamemax := make(map[string][]Funcionario)
	areaavg := make(map[string]float64)
	areamin := make(map[string]float64)
	areamax := make(map[string]float64)
	countarea := make(map[string]float64)
	lastnamemax := make(map[string]float64)
	countlastname := make(map[string]float64)
	leastemployees := math.MaxFloat64
	funcionario := Funcionario{}

	if len(os.Args) != 2 {
		fmt.Println("ERRO! Sintaxe: desafio5_jsonparser \"nomedoarquivo\"")
		os.Exit(0)
	} else {
		filename = os.Args[1]
	}

	// Abrir o arquivo com ReadFile é fundamental. De outras formas dá erro
	// de memória para arquivos grandes

	buf, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}

	// Vamos percorrer o array de areas para criar o mapa de nome de areas x codigo
	jsonparser.ArrayEach(buf, func(value []byte, dataType jsonparser.ValueType, offset int, err error) {
		retcod, _ := jsonparser.GetUnsafeString(value, "codigo")
		retnome, _ := jsonparser.GetUnsafeString(value, "nome")
		nomearea[retcod] = retnome
	}, "areas")

	// Vamos percorrer o array de funconarios para obter as estatisticas
	jsonparser.ArrayEach(buf, func(value []byte, dataType jsonparser.ValueType, offset int, err error) {
		funcionario.ID, _ = jsonparser.GetInt(value, "id")
		funcionario.Nome, _ = jsonparser.GetUnsafeString(value, "nome")
		funcionario.Sobrenome, _ = jsonparser.GetUnsafeString(value, "sobrenome")
		funcionario.Salario, _ = jsonparser.GetFloat(value, "salario")
		funcionario.Area, _ = jsonparser.GetUnsafeString(value, "area")

		globalavg += funcionario.Salario
		contaemp++
		if funcionario.Salario > globalmax {
			globalmax = funcionario.Salario
			empmax = []Funcionario{funcionario}
		} else {
			if funcionario.Salario == globalmax {
				empmax = append(empmax, funcionario)
			}
		}

		if funcionario.Salario < globalmin {
			globalmin = funcionario.Salario
			empmin = []Funcionario{funcionario}
		} else {
			if funcionario.Salario == globalmin {
				empmin = append(empmin, funcionario)
			}
		}

		areaavg[funcionario.Area] += funcionario.Salario
		countarea[funcionario.Area]++

		if _, ok := areamin[funcionario.Area]; !ok {
			areamin[funcionario.Area] = funcionario.Salario
		}

		if funcionario.Salario < areamin[funcionario.Area] {
			areamin[funcionario.Area] = funcionario.Salario
			empareamin[funcionario.Area] = []Funcionario{funcionario}
		} else {
			if funcionario.Salario == areamin[funcionario.Area] {
				empareamin[funcionario.Area] = append(empareamin[funcionario.Area], funcionario)
			}
		}

		if funcionario.Salario > areamax[funcionario.Area] {
			areamax[funcionario.Area] = funcionario.Salario
			empareamax[funcionario.Area] = []Funcionario{funcionario}
		} else {
			if funcionario.Salario == areamax[funcionario.Area] {
				empareamax[funcionario.Area] = append(empareamax[funcionario.Area], funcionario)
			}
		}

		if funcionario.Salario > lastnamemax[funcionario.Sobrenome] {
			lastnamemax[funcionario.Sobrenome] = funcionario.Salario
			emplastnamemax[funcionario.Sobrenome] = []Funcionario{funcionario}
		} else {
			if funcionario.Salario == lastnamemax[funcionario.Sobrenome] {
				emplastnamemax[funcionario.Sobrenome] = append(emplastnamemax[funcionario.Sobrenome], funcionario)
			}
		}

		countlastname[funcionario.Sobrenome]++
	}, "funcionarios")

	for k := range countarea {
		if countarea[k] < leastemployees {
			leastemployees = countarea[k]
		}

		if countarea[k] > mostemployees {
			mostemployees = countarea[k]
		}
	}

	// Agora vamos imprimir tudo

	for _, v := range empmax {
		fmt.Printf("global_max|%s %s|%.2f\n", v.Nome, v.Sobrenome, v.Salario)
	}
	for _, v := range empmin {
		fmt.Printf("global_min|%s %s|%.2f\n", v.Nome, v.Sobrenome, v.Salario)
	}

	fmt.Printf("global_avg|%.2f\n", globalavg/contaemp)

	for k := range nomearea {
		for _, f := range empareamax[k] {
			fmt.Printf("area_max|%s|%s %s|%.2f\n", nomearea[k], f.Nome, f.Sobrenome, f.Salario)
		}
		for _, f := range empareamin[k] {
			fmt.Printf("area_min|%s|%s %s|%.2f\n", nomearea[k], f.Nome, f.Sobrenome, f.Salario)
		}
		if countarea[k] > 0 {
			fmt.Printf("area_avg|%s|%.2f\n", nomearea[k], areaavg[k]/countarea[k])
		}

		if countarea[k] == leastemployees {
			fmt.Printf("least_employees|%s|%.0f\n", nomearea[k], countarea[k])
		}

		if countarea[k] == mostemployees {
			fmt.Printf("most_employees|%s|%.0f\n", nomearea[k], countarea[k])
		}
	}

	for k := range lastnamemax {
		if countlastname[k] > 1 {
			for _, f := range emplastnamemax[k] {
				fmt.Printf("last_name_max|%s|%s %s|%.2f\n", f.Sobrenome, f.Nome, f.Sobrenome, f.Salario)
			}
		}
	}
}
