// funcionarios implementa o parsing dos funcionários em JSON.
package main

import (
	"fmt"
	"github.com/francoispqt/gojay"
	"sync"
)

// funcRecord guarda os dados de um funcionário.
type funcRecord struct {
	id        int
	nome      string
	sobrenome string
	salario   float64
	area      string
}

// implement UnmarshalerJSONObject
func (x *funcRecord) UnmarshalJSONObject(dec *gojay.Decoder, k string) error {
	switch k {
	case "id":
		return dec.Int(&x.id)
	case "nome":
		return dec.String(&x.nome)
	case "sobrenome":
		return dec.String(&x.sobrenome)
	case "salario":
		return dec.Float64(&x.salario)
	case "area":
		return dec.String(&x.area)
	}
	return nil
}

func (x *funcRecord) NKeys() int {
	return 0
}

// funcList contem dados sobre uma lista de funcionários.
type funcList struct {
	once        sync.Once
	funcionario *funcRecord

	// Statistics
	gstats baseStatsItem
	astats areaStats
	nstats nameStats
}

// Implementa UnmarshalerJSONObject em funcionarios.
func (x *funcList) UnmarshalJSONArray(dec *gojay.Decoder) error {
	// Decodifica os dados de um funcionário no array JSON.
	if err := dec.Object(x.funcionario); err != nil {
		return err
	}

	// Inicializa estatísticas globais uma vez.
	x.once.Do(func() {
		x.gstats.min = x.funcionario.salario
		x.gstats.max = x.funcionario.salario
		x.gstats.minNomes = []string{}
		x.gstats.maxNomes = []string{}
	})

	if x.funcionario.salario == x.gstats.min {
		x.gstats.minNomes = append(x.gstats.minNomes, x.funcionario.nome+" "+x.funcionario.sobrenome)
	} else if x.funcionario.salario < x.gstats.min {
		x.gstats.min = x.funcionario.salario
		x.gstats.minNomes = []string{x.funcionario.nome + " " + x.funcionario.sobrenome}
	}

	if x.funcionario.salario == x.gstats.max {
		x.gstats.maxNomes = append(x.gstats.maxNomes, x.funcionario.nome+" "+x.funcionario.sobrenome)
	} else if x.funcionario.salario > x.gstats.max {
		x.gstats.max = x.funcionario.salario
		x.gstats.maxNomes = []string{x.funcionario.nome + " " + x.funcionario.sobrenome}
	}

	x.gstats.sum += x.funcionario.salario
	x.gstats.count++

	// Estatísticas por área.
	as, ok := x.astats[x.funcionario.area]
	if !ok {
		as = &baseStatsItem{
			min:      x.funcionario.salario,
			max:      x.funcionario.salario,
			minNomes: []string{},
			maxNomes: []string{},
		}
		x.astats[x.funcionario.area] = as
	}
	if x.funcionario.salario == as.min {
		as.minNomes = append(as.minNomes, x.funcionario.nome+" "+x.funcionario.sobrenome)
	} else if x.funcionario.salario < as.min {
		as.min = x.funcionario.salario
		as.minNomes = []string{x.funcionario.nome + " " + x.funcionario.sobrenome}
	}

	if x.funcionario.salario == as.max {
		as.maxNomes = append(as.maxNomes, x.funcionario.nome+" "+x.funcionario.sobrenome)
	} else if x.funcionario.salario > as.max {
		as.max = x.funcionario.salario
		as.maxNomes = []string{x.funcionario.nome + " " + x.funcionario.sobrenome}
	}
	as.sum += x.funcionario.salario
	as.count++

	// Estatísticas por sobrenome: Das pessoas que têm o mesmo sobrenome,
	// aquela que recebe mais (não inclua sobrenomes que apenas uma pessoa
	// tem nos resultados)
	ns, ok := x.nstats[x.funcionario.sobrenome]
	if !ok {
		ns = &nameStatsItem{
			max:   x.funcionario.salario,
			nomes: []string{},
		}
		x.nstats[x.funcionario.sobrenome] = ns
	}
	if x.funcionario.salario == ns.max {
		ns.nomes = append(ns.nomes, x.funcionario.nome+" "+x.funcionario.sobrenome)
	} else if x.funcionario.salario > ns.max {
		ns.max = x.funcionario.salario
		ns.nomes = []string{x.funcionario.nome + " " + x.funcionario.sobrenome}
	}
	ns.count++

	return nil
}

// printGlobalStats imprime estatísticas globais sobre os funcionários.
func (x *funcList) printGlobalStats() {
	for _, n := range x.gstats.minNomes {
		fmt.Printf("global_min|%s|%.2f\n", n, x.gstats.min)
	}
	for _, n := range x.gstats.maxNomes {
		fmt.Printf("global_max|%s|%.2f\n", n, x.gstats.max)
	}
	fmt.Printf("global_avg|%.2f\n", x.gstats.sum/float64(x.gstats.count))
}

// printAreaStats imprime estatísticas por área.
func (x *funcList) printAreaStats(areanames map[string]string) {
	var (
		once         sync.Once
		minAreaCount int
		maxAreaCount int
		minAreaNames []string
		maxAreaNames []string
	)

	for k, as := range x.astats {
		aname := areaCodeToName(areanames, k)

		for _, n := range as.minNomes {
			fmt.Printf("area_min|%s|%s|%.2f\n", aname, n, as.min)
		}
		for _, n := range as.maxNomes {
			fmt.Printf("area_max|%s|%s|%.2f\n", aname, n, as.max)
		}
		fmt.Printf("area_avg|%s|%.2f\n", aname, as.sum/float64(as.count))

		once.Do(func() {
			minAreaCount = as.count
			maxAreaCount = as.count
			minAreaNames = []string{}
			maxAreaNames = []string{}
		})

		if as.count == minAreaCount {
			minAreaNames = append(minAreaNames, aname)
		} else if as.count < minAreaCount {
			minAreaCount = as.count
			minAreaNames = []string{aname}
		}

		if as.count == maxAreaCount {
			maxAreaNames = append(maxAreaNames, aname)
		} else if as.count > maxAreaCount {
			maxAreaCount = as.count
			maxAreaNames = []string{aname}
		}
	}

	for _, a := range minAreaNames {
		fmt.Printf("least_employees|%s|%d\n", a, minAreaCount)
	}
	for _, a := range maxAreaNames {
		fmt.Printf("most_employees|%s|%d\n", a, maxAreaCount)
	}
}

// printNameStats imprime estatísticas por nome.
func (x *funcList) printNameStats() {
	// Maiores salários por último nome.
	for k, ns := range x.nstats {
		// Apenas sobrenomes com mais de um nome.
		if ns.count > 1 {
			for _, n := range ns.nomes {
				fmt.Printf("last_name_max|%s|%s|%.2f\n", k, n, ns.max)
			}
		}
	}
}

func areaCodeToName(a map[string]string, s string) string {
	r, ok := a[s]
	if ok {
		return r
	}
	return "Não disponível"
}
