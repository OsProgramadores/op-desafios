package main

import (
	"flag"
	"fmt"
	"github.com/json-iterator/go"
	"io/ioutil"
	"log"
	"os"
	"runtime/pprof"
	"sort"
)

type funArea struct {
	Funcionarios []struct {
		ID        int    `json:"id"`
		Nome      string `json:"nome"`
		Sobrenome string `json:"sobrenome"`
		Salario   int    `json:"salario"`
		Area      string `json:"area"`
	} `json:"funcionarios"`
	Areas []struct {
		Codigo string `json:"codigo"`
		Nome   string `json:"nome"`
	} `json:"areas"`
}

type baseStatsItem struct {
	min      int
	max      int
	minNomes []string
	maxNomes []string
	sum      int
	count    int
}

type nameStatsItem struct {
	max   int
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
		minAreaName   string
		maxAreaName   string
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
		switch {
		case f.Salario == gstats.min:
			gstats.minNomes = append(gstats.minNomes, f.Nome)
		case f.Salario < gstats.min:
			gstats.min = f.Salario
			gstats.minNomes = []string{f.Nome}
		case f.Salario == gstats.max:
			gstats.maxNomes = append(gstats.maxNomes, f.Nome)
		case f.Salario > gstats.max:
			gstats.max = f.Salario
			gstats.maxNomes = []string{f.Nome}
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
		switch {
		case f.Salario == as.min:
			as.minNomes = append(as.minNomes, f.Nome)
		case f.Salario < as.min:
			as.min = f.Salario
			as.minNomes = []string{f.Nome}
		case f.Salario == as.max:
			as.maxNomes = append(as.maxNomes, f.Nome)
		case f.Salario > as.max:
			as.max = f.Salario
			as.maxNomes = []string{f.Nome}
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
			ns.nomes = append(ns.nomes, f.Nome)
		} else if f.Salario > ns.max {
			ns.max = f.Salario
			ns.nomes = []string{f.Nome}
		}
		ns.count++
	}

	out := []string{}

	// Estatísticas globais.
	for _, n := range gstats.minNomes {
		out = append(out, fmt.Sprintf("global_min %s %d\n", n, gstats.min))
	}
	for _, n := range gstats.maxNomes {
		out = append(out, fmt.Sprintf("global_max %s %d\n", n, gstats.max))
	}
	out = append(out, fmt.Sprintf("global_avg %d\n", gstats.sum/gstats.count))

	// Salários por área
	aname := loadAreaNames(fa)

	ix := 0
	for k, as := range astats {
		area := areaCodeToName(aname, k)

		for _, n := range as.minNomes {
			out = append(out, fmt.Sprintf("area_min %s %s %d\n", area, n, as.min))
		}
		for _, n := range as.maxNomes {
			out = append(out, fmt.Sprintf("area_max %s %s %d\n", area, n, as.max))
		}
		out = append(out, fmt.Sprintf("area_avg %s %d\n", area, as.sum/as.count))

		if as.count < minAreaCount || ix == 0 {
			minAreaCount = as.count
			minAreaName = k
		}
		if as.count > maxAreaCount || ix == 0 {
			maxAreaCount = as.count
			maxAreaName = k
		}
		ix++
	}

	out = append(out, fmt.Sprintf("area_min_func %s %d\n", areaCodeToName(aname, minAreaName), minAreaCount))
	out = append(out, fmt.Sprintf("area_max_func %s %d\n", areaCodeToName(aname, maxAreaName), maxAreaCount))

	// Maiores salários por último nome.
	ix = 0
	for k, ns := range nstats {
		// Apenas sobrenomes com mais de um nome.
		if ns.count > 1 {
			for _, n := range ns.nomes {
				out = append(out, fmt.Sprintf("last_name_max %s %s %d\n", k, n, ns.max))
			}
		}
		ix++
	}
	sort.Strings(out)
	for ix := range out {
		fmt.Print(out[ix])
	}
}
