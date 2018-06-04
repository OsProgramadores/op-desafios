package main

import (
	"flag"
	"fmt"
	"github.com/json-iterator/go"
	"io/ioutil"
	"log"
	"os"
	"runtime/pprof"
)

type funArea struct {
	Funcionarios []struct {
		ID        int     `json:"id"`
		Nome      string  `json:"nome"`
		Sobrenome string  `json:"sobrenome"`
		Salario   float64 `json:"salario"`
		Area      string  `json:"area"`
	} `json:"funcionarios"`
	Areas []struct {
		Codigo string `json:"codigo"`
		Nome   string `json:"nome"`
	} `json:"areas"`
}

type baseStatsItem struct {
	min      float64
	max      float64
	minNomes []string
	maxNomes []string
	sum      float64
	count    int
}

type nameStatsItem struct {
	max   float64
	nomes []string
	count int
}

type areaStats map[string]*baseStatsItem

type nameStats map[string]*nameStatsItem

type areaName map[string]string

func loadAreaNames(fa funArea) areaName {
	m := areaName{}
	for _, a := range fa.Areas {
		m[a.Codigo] = a.Nome
	}
	return m
}

func areaCodeToName(a areaName, s string) string {
	r, ok := a[s]
	if ok {
		return r
	}
	return "Não disponível"
}

func main() {
	var (
		minAreaCount  int
		maxAreaCount  int
		minAreaNames  []string
		maxAreaNames  []string
		optCPUProfile string
	)

	log.SetFlags(0)

	flag.StringVar(&optCPUProfile, "cpuprofile", "", "write cpu profile to file")
	flag.Parse()

	if len(flag.Args()) != 1 {
		log.Fatalln("Use: d05 arquivo")
	}

	// Profiling
	if optCPUProfile != "" {
		f, err := os.Create(optCPUProfile)
		if err != nil {
			log.Fatal(err)
		}
		pprof.StartCPUProfile(f)
		defer pprof.StopCPUProfile()
	}

	buf, err := ioutil.ReadFile(flag.Args()[0])
	if err != nil {
		log.Fatalln(err)
	}

	// Converte json em uma estrutura em memória.
	fa := funArea{}
	json := jsoniter.ConfigFastest
	if err = json.Unmarshal(buf, &fa); err != nil {
		log.Fatalln(err)
	}

	gstats := baseStatsItem{}
	astats := areaStats{}
	nstats := nameStats{}

	// Processamento de funcionários.
	for ix, f := range fa.Funcionarios {
		// Estatísticas Globais.
		if ix == 0 {
			gstats.min = f.Salario
			gstats.max = f.Salario
			gstats.minNomes = []string{}
			gstats.maxNomes = []string{}
		}

		//fullName := f.Nome + " " + f.Sobrenome

		if f.Salario == gstats.min {
			gstats.minNomes = append(gstats.minNomes, f.Nome+" "+f.Sobrenome)
		} else if f.Salario < gstats.min {
			gstats.min = f.Salario
			gstats.minNomes = []string{f.Nome + " " + f.Sobrenome}
		}

		if f.Salario == gstats.max {
			gstats.maxNomes = append(gstats.maxNomes, f.Nome+" "+f.Sobrenome)
		} else if f.Salario > gstats.max {
			gstats.max = f.Salario
			gstats.maxNomes = []string{f.Nome + " " + f.Sobrenome}
		}

		gstats.sum += f.Salario
		gstats.count++

		// Estatísticas por área.
		as, ok := astats[f.Area]
		if !ok {
			as = &baseStatsItem{
				min:      f.Salario,
				max:      f.Salario,
				minNomes: []string{},
				maxNomes: []string{},
			}
			astats[f.Area] = as
		}
		if f.Salario == as.min {
			as.minNomes = append(as.minNomes, f.Nome+" "+f.Sobrenome)
		} else if f.Salario < as.min {
			as.min = f.Salario
			as.minNomes = []string{f.Nome + " " + f.Sobrenome}
		}

		if f.Salario == as.max {
			as.maxNomes = append(as.maxNomes, f.Nome+" "+f.Sobrenome)
		} else if f.Salario > as.max {
			as.max = f.Salario
			as.maxNomes = []string{f.Nome + " " + f.Sobrenome}
		}
		as.sum += f.Salario
		as.count++

		// Estatísticas por sobrenome: Das pessoas que têm o mesmo sobrenome,
		// aquela que recebe mais (não inclua sobrenomes que apenas uma pessoa
		// tem nos resultados)
		ns, ok := nstats[f.Sobrenome]
		if !ok {
			ns = &nameStatsItem{
				max:   f.Salario,
				nomes: []string{},
			}
			nstats[f.Sobrenome] = ns
		}
		if f.Salario == ns.max {
			ns.nomes = append(ns.nomes, f.Nome+" "+f.Sobrenome)
		} else if f.Salario > ns.max {
			ns.max = f.Salario
			ns.nomes = []string{f.Nome + " " + f.Sobrenome}
		}
		ns.count++
	}

	// Estatísticas globais.
	for _, n := range gstats.minNomes {
		fmt.Printf("global_min|%s|%.2f\n", n, gstats.min)
	}
	for _, n := range gstats.maxNomes {
		fmt.Printf("global_max|%s|%.2f\n", n, gstats.max)
	}
	fmt.Printf("global_avg|%.2f\n", gstats.sum/float64(gstats.count))

	// Salários por área
	aname := loadAreaNames(fa)

	ix := 0
	for k, as := range astats {
		area := areaCodeToName(aname, k)

		for _, n := range as.minNomes {
			fmt.Printf("area_min|%s|%s|%.2f\n", area, n, as.min)
		}
		for _, n := range as.maxNomes {
			fmt.Printf("area_max|%s|%s|%.2f\n", area, n, as.max)
		}
		fmt.Printf("area_avg|%s|%.2f\n", area, as.sum/float64(as.count))

		if ix == 0 {
			minAreaCount = as.count
			maxAreaCount = as.count
			minAreaNames = []string{}
			maxAreaNames = []string{}
		}
		if as.count == minAreaCount {
			minAreaNames = append(minAreaNames, area)
		} else if as.count < minAreaCount {
			minAreaCount = as.count
			minAreaNames = []string{area}
		}

		if as.count == maxAreaCount {
			maxAreaNames = append(maxAreaNames, area)
		} else if as.count > maxAreaCount {
			maxAreaCount = as.count
			maxAreaNames = []string{area}
		}
		ix++
	}

	for _, a := range minAreaNames {
		fmt.Printf("least_employees|%s|%d\n", a, minAreaCount)
	}
	for _, a := range maxAreaNames {
		fmt.Printf("most_employees|%s|%d\n", a, maxAreaCount)
	}

	// Maiores salários por último nome.
	ix = 0
	for k, ns := range nstats {
		// Apenas sobrenomes com mais de um nome.
		if ns.count > 1 {
			for _, n := range ns.nomes {
				fmt.Printf("last_name_max|%s|%s|%.2f\n", k, n, ns.max)
			}
		}
		ix++
	}
}
