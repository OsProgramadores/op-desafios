package main

import (
	"flag"
	"github.com/francoispqt/gojay"
	"io/ioutil"
	"log"
	"os"
	"runtime/debug"
	"runtime/pprof"
)

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

func main() {
	var (
		optCPUProfile string
	)

	log.SetFlags(0)

	flag.StringVar(&optCPUProfile, "cpuprofile", "", "write cpu profile to file")
	flag.Parse()

	if len(flag.Args()) != 1 {
		log.Fatalln("Use: d05 arquivo")
	}

	// Disable GC
	debug.SetGCPercent(-1)

	// Profiling.
	if optCPUProfile != "" {
		f, err := os.Create(optCPUProfile)
		if err != nil {
			log.Fatal(err)
		}
		pprof.StartCPUProfile(f)
		defer pprof.StopCPUProfile()
	}

	// Le o arquivo inteiro em memória.
	buf, err := ioutil.ReadFile(flag.Args()[0])
	if err != nil {
		log.Fatal(err)
	}

	af := &areaOrFunc{
		funcs: &funcList{
			funcionario: &funcRecord{},
			gstats:      baseStatsItem{},
			astats:      areaStats{},
			nstats:      nameStats{},
		},
		areas: &areasList{
			aRecord:          &areasRecord{},
			areasCodeAndName: map[string]string{},
		},
	}

	err = gojay.Unsafe.Unmarshal(buf, af)
	if err != nil {
		log.Fatal(err)
	}

	af.funcs.printGlobalStats()
	af.funcs.printAreaStats(af.areas.areasCodeAndName)
	af.funcs.printNameStats()
}
