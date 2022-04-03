// Adriano Roberto de Lima
// Desafio 05 - em GO !

package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"os"

	jsoniter "github.com/json-iterator/go"
)

// Funcionario é a estrutura com os dados dos funcionarios no arquivo a ser lido
type Funcionario struct {
	ID        int     `json:"id"`
	Nome      string  `json:"nome"`
	Sobrenome string  `json:"sobrenome"`
	Salario   float64 `json:"salario"`
	Area      string  `json:"area"`
}

// Area é a estrutura com os dados das areas no arquivo a ser lido
type Area struct {
	Codigo string `json:"codigo"`
	Nome   string `json:"nome"`
}

// Empresa é a estrutura geral do arquivo a ser lido
type Empresa struct {
	Funcionarios []Funcionario `json:"funcionarios"`
	Areas        []Area        `json:"areas"`
}

func main() {
	var (
		filename string
		dados    Empresa
	)

	globalmin := math.MaxFloat64
	globalmax := 0.0
	globalavg := 0.0
	leastemployees := math.MaxFloat64
	mostemployees := 0.0
	nomearea := make(map[string]string)
	areaavg := make(map[string]float64)
	areamin := make(map[string]float64)
	areamax := make(map[string]float64)
	countarea := make(map[string]float64)
	lastnamemax := make(map[string]float64)
	countlastname := make(map[string]float64)

	if len(os.Args) != 2 {
		fmt.Println("ERRO! Sintaxe: desafio5 \"nomedoarquivo\"")
		os.Exit(0)
	} else {
		filename = os.Args[1]
	}

	r, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("ERRO! Não consegui ler o arquivo !")
		os.Exit(0)
	}

	json := jsoniter.ConfigFastest
	json.Unmarshal(r, &dados)

	for _, a := range dados.Areas {
		nomearea[a.Codigo] = a.Nome
		areamin[a.Codigo] = math.MaxFloat64
	}

	for _, f := range dados.Funcionarios {
		if f.Salario > globalmax {
			globalmax = f.Salario
		}

		if f.Salario < globalmin {
			globalmin = f.Salario
		}

		globalavg += f.Salario

		areaavg[f.Area] += f.Salario
		countarea[f.Area]++

		if f.Salario < areamin[f.Area] {
			areamin[f.Area] = f.Salario
		}

		if f.Salario > areamax[f.Area] {
			areamax[f.Area] = f.Salario
		}

		if f.Salario > lastnamemax[f.Sobrenome] {
			lastnamemax[f.Sobrenome] = f.Salario
		}

		countlastname[f.Sobrenome]++
	}

	globalavg = globalavg / float64(len(dados.Funcionarios))

	for _, c := range countarea {
		if c < leastemployees {
			leastemployees = c
		}
		if c > mostemployees {
			mostemployees = c
		}
	}

	for _, f := range dados.Funcionarios {
		if f.Salario == globalmax {
			fmt.Printf("global_max|%s %s|%.2f\n", f.Nome, f.Sobrenome, f.Salario)
		}
		if f.Salario == globalmin {
			fmt.Printf("global_min|%s %s|%.2f\n", f.Nome, f.Sobrenome, f.Salario)
		}
		if f.Salario == areamin[f.Area] {
			fmt.Printf("area_min|%s|%s %s|%.2f\n", nomearea[f.Area], f.Nome, f.Sobrenome, f.Salario)
		}
		if f.Salario == areamax[f.Area] {
			fmt.Printf("area_max|%s|%s %s|%.2f\n", nomearea[f.Area], f.Nome, f.Sobrenome, f.Salario)
		}
		if f.Salario == lastnamemax[f.Sobrenome] && countlastname[f.Sobrenome] > 1 {
			fmt.Printf("last_name_max|%s|%s %s|%.2f\n", f.Sobrenome, f.Nome, f.Sobrenome, f.Salario)
		}
	}

	fmt.Printf("global_avg|%.2f\n", globalavg)

	for _, a := range dados.Areas {
		if countarea[a.Codigo] > 0 {
			fmt.Printf("area_avg|%s|%.2f\n", nomearea[a.Codigo], areaavg[a.Codigo]/countarea[a.Codigo])
		}

		if countarea[a.Codigo] == leastemployees {
			fmt.Printf("least_employees|%s|%.0f\n", nomearea[a.Codigo], countarea[a.Codigo])
		}

		if countarea[a.Codigo] == mostemployees {
			fmt.Printf("most_employees|%s|%.0f\n", nomearea[a.Codigo], countarea[a.Codigo])
		}
	}
}
