package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"runtime/pprof"
	"strconv"
	"strings"
	"sync"
	"time"

	jsoniter "github.com/json-iterator/go"
)

// Area  struct da area, carregando campos extras para serem utilizados durante os calculos ..
type Area struct {
	Codigo       string `json:"codigo"`
	Nome         string `json:"nome"`
	Qtd          int
	AvgSal       float64
	MaxSal       float64
	MinSal       float64
	StrMinSal    *Employee
	StrMaxSal    *Employee
	MostAreaQTD  *Area
	LeastAreaQTD *Area
}

// Employee , funcionario ..
type Employee struct {
	ID           int     `json:"id"`
	Nome         string  `json:"nome"`
	Sobrenome    string  `json:"sobrenome"`
	Salario      float64 `json:"salario"`
	Area         string  `json:"area"`
	GlobalMaxSal *Employee
	GlobalMinSal *Employee
	AreaMaxSal   *Employee
	AreaMinSal   *Employee
}

// JSON união dos 2 para unmarshal ..
type JSON struct {
	Funcs []Employee `json:"funcionarios"`
	Areas []Area     `json:"areas"`
}

// MaiorSal aonde é armazenado o maior valor glogal de salario
type MaiorSal struct {
	Salario float64
	Worker  *Employee
}

// MenorSal aonde é armazenado o menor valor glogal de salario
type MenorSal struct {
	Salario float64
	Worker  *Employee
}

// LeastAreaQtd (least_employee) aonde é armazenado a maior(es) area(s) por quantidade de funcionario
type LeastAreaQtd struct {
	QTD   int
	Areas *Area
}

// MostAreaQtd (most_employee)aonde é armazenado a maior(es) area(s) por quantidade de funcionario
type MostAreaQtd struct {
	QTD   int
	Areas *Area
}

var count int

// lastNameSal ..
type lastNameSal1 struct {
	LastNameMax  strings.Builder
	MaxSal       float64
	SobreNome    string
	Funcionarios []string
}
type lastNameSal map[string][]*Employee

/*
	calcula o maior salario por sobrenome,
	desconsiderando nomes + sobrenomes
	já existentes durante o calculo.
	Exemplo: se João Vitor, já existir,
	o próximo João Vitor informado é desconsiderado.
*/
func maxSalByLastName(bigSalaryByLastName *lastNameSal, dat JSON) {
	slice, found := (*bigSalaryByLastName)[dat.Funcs[count].Sobrenome]
	if found {
		for _, value := range slice {
			if dat.Funcs[count].Salario > value.Salario {
				slice = ([]*Employee{&dat.Funcs[count]})
				return
			}
			if dat.Funcs[count].Salario == value.Salario {
				slice = append(slice, &dat.Funcs[count])
				return
			}
		}
		return
	}
	(*bigSalaryByLastName)[dat.Funcs[count].Sobrenome] = []*Employee{&dat.Funcs[count]}
	return
}
func main() {
	start := time.Now()

	var optCPUProfile string
	flag.StringVar(&optCPUProfile, "cpuprofile", "", "write cpu profile to file")
	flag.Parse()
	if optCPUProfile != "" {
		f, err := os.Create(optCPUProfile)
		if err != nil {
			panic(err)
		}
		pprof.StartCPUProfile(f)
		defer pprof.StopCPUProfile()
	}

	rawdata, err := ioutil.ReadFile(os.Args[len(os.Args)-1])
	if err != nil {
		panic(err)
	}

	dat := JSON{}
	json := jsoniter.ConfigFastest
	if err = json.Unmarshal(rawdata, &dat); err != nil {
		panic(err)
	}
	var sizeArea int = len(dat.Areas)

	var mediaGlobalSal float64

	globalMaxSal := MaiorSal{}
	globalMinSal := MenorSal{}
	bigSalaryByLastName := lastNameSal{}

	mostArea := MostAreaQtd{}
	leastArea := LeastAreaQtd{}

	for count = 0; count < len(dat.Funcs); count++ {
		// calculo maior salario por sobrenome
		maxSalByLastName(&bigSalaryByLastName, dat)

		// calculo global_max
		if dat.Funcs[count].Salario > globalMaxSal.Salario {
			globalMaxSal.Salario = dat.Funcs[count].Salario
			globalMaxSal.Worker = &dat.Funcs[count]
		} else if dat.Funcs[count].Salario == globalMaxSal.Salario {
			globalMaxSal.Worker.GlobalMaxSal = &dat.Funcs[count]
		}
		// calculo glogal_min
		if count == 0 {
			globalMinSal.Salario = dat.Funcs[count].Salario
			globalMinSal.Worker = &dat.Funcs[count]
		} else if dat.Funcs[count].Salario < globalMinSal.Salario {
			globalMinSal.Salario = dat.Funcs[count].Salario
			globalMinSal.Worker = &dat.Funcs[count]
		} else if dat.Funcs[count].Salario == globalMinSal.Salario {
			globalMinSal.Worker.GlobalMaxSal = &dat.Funcs[count]
		}

		mediaGlobalSal += dat.Funcs[count].Salario

		for a := 0; a < sizeArea; a++ {
			if dat.Funcs[count].Area == dat.Areas[a].Codigo {
				// calculo menor salario
				if dat.Areas[a].Qtd == 0 {
					dat.Areas[a].MinSal = dat.Funcs[count].Salario
					dat.Areas[a].StrMinSal = &dat.Funcs[count]
				} else if dat.Funcs[count].Salario < dat.Areas[a].MinSal {
					dat.Areas[a].MinSal = dat.Funcs[count].Salario
					dat.Areas[a].StrMinSal = &dat.Funcs[count]
				} else if dat.Funcs[count].Salario == dat.Areas[a].MinSal {
					dat.Areas[a].StrMinSal.AreaMinSal = &dat.Funcs[count]
				}

				dat.Areas[a].Qtd++

				// calculo maior salario
				if dat.Funcs[count].Salario == dat.Areas[a].MaxSal {
					dat.Areas[a].StrMaxSal.AreaMaxSal = &dat.Funcs[count]
				}
				if dat.Funcs[count].Salario > dat.Areas[a].MaxSal {
					dat.Areas[a].MaxSal = dat.Funcs[count].Salario
					dat.Areas[a].StrMaxSal = &dat.Funcs[count]
				}

				dat.Areas[a].AvgSal += dat.Funcs[count].Salario

				// calculo das areas most employee e least employee
				if dat.Areas[a].Qtd == mostArea.QTD {
					mostArea.Areas.MostAreaQTD = &dat.Areas[a]
				}
				if dat.Areas[a].Qtd > mostArea.QTD {
					mostArea.QTD = dat.Areas[a].Qtd
					mostArea.Areas = &dat.Areas[a]
				}

			}
		}
	}
	wg := sync.WaitGroup{}
	wg.Add(9)

	leastArea.QTD = mostArea.QTD
	// area avg
	go func() {
		var sb strings.Builder
		for contador := 0; contador < sizeArea; contador++ {
			if dat.Areas[contador].Qtd != 0 {
				sb.WriteString("\narea_avg|")
				sb.WriteString(dat.Areas[contador].Nome)
				sb.WriteString("|")
				sb.WriteString(strconv.FormatFloat(dat.Areas[contador].AvgSal/float64(dat.Areas[contador].Qtd), 'f', 2, 64))
			}
		}
		// exibindo o area_avg
		os.Stdout.WriteString(sb.String())
		wg.Done()
	}()

	// exibindo global_avg
	go func() {
		os.Stdout.WriteString("\nglobal_avg|")
		os.Stdout.WriteString(strconv.FormatFloat(mediaGlobalSal/float64(count), 'f', 2, 64))
		wg.Done()
	}()
	// exibindo glogal_max
	go func() {
		var sb strings.Builder
		sb.WriteString("\nglobal_max|")
		sb.WriteString(globalMaxSal.Worker.Sobrenome)
		sb.WriteString("|")
		sb.WriteString(globalMaxSal.Worker.Nome)
		sb.WriteString(" ")
		sb.WriteString(globalMaxSal.Worker.Sobrenome)
		sb.WriteString("|")
		sb.WriteString(strconv.FormatFloat(globalMaxSal.Worker.Salario, 'f', 2, 64))
		for globalMaxSal.Worker.GlobalMaxSal != nil {
			sb.WriteString("\nglobal_max|")
			sb.WriteString(globalMaxSal.Worker.GlobalMaxSal.Sobrenome)
			sb.WriteString("|")
			sb.WriteString(globalMaxSal.Worker.GlobalMaxSal.Nome)
			sb.WriteString(" ")
			sb.WriteString(globalMaxSal.Worker.GlobalMaxSal.Sobrenome)
			sb.WriteString("|")
			sb.WriteString(strconv.FormatFloat(globalMaxSal.Worker.GlobalMaxSal.Salario, 'f', 2, 64))
			globalMaxSal.Worker.GlobalMaxSal = globalMaxSal.Worker.GlobalMaxSal.GlobalMaxSal
		}
		os.Stdout.WriteString(sb.String())
		wg.Done()
	}()

	// exibindo os glogal_min
	go func() {
		var sb strings.Builder
		sb.WriteString("\nglobal_min|")
		sb.WriteString(globalMinSal.Worker.Sobrenome)
		sb.WriteString("|")
		sb.WriteString(globalMinSal.Worker.Nome)
		sb.WriteString(" ")
		sb.WriteString(globalMinSal.Worker.Sobrenome)
		sb.WriteString("|")
		sb.WriteString(strconv.FormatFloat(globalMinSal.Worker.Salario, 'f', 2, 64))
		for globalMinSal.Worker.GlobalMinSal != nil {
			sb.WriteString("\nglobal_min|")
			sb.WriteString(globalMinSal.Worker.GlobalMinSal.Sobrenome)
			sb.WriteString("|")
			sb.WriteString(globalMinSal.Worker.GlobalMinSal.Nome)
			sb.WriteString(" ")
			sb.WriteString(globalMinSal.Worker.GlobalMinSal.Sobrenome)
			sb.WriteString("|")
			sb.WriteString(strconv.FormatFloat(globalMinSal.Worker.GlobalMinSal.Salario, 'f', 2, 64))
			globalMinSal.Worker.GlobalMaxSal = globalMinSal.Worker.GlobalMinSal.GlobalMinSal
		}
		os.Stdout.WriteString(sb.String())
		wg.Done()
	}()

	// calculando os least_employe
	go func() {
		for contador := 1; contador < sizeArea; contador++ {
			if dat.Areas[contador].Qtd != 0 {
				if dat.Areas[contador].Qtd == leastArea.QTD {
					leastArea.Areas.LeastAreaQTD = &dat.Areas[contador]
				}
				if dat.Areas[contador].Qtd < leastArea.QTD {
					leastArea.QTD = dat.Areas[contador].Qtd
					leastArea.Areas = &dat.Areas[contador]
				}
			}

		}
		// exibindo os least_employess
		var sb strings.Builder
		sb.WriteString("\nleast_employees|")
		sb.WriteString(leastArea.Areas.Nome)
		sb.WriteString("|")
		sb.WriteString(strconv.Itoa(leastArea.QTD))
		leastArea.Areas = leastArea.Areas.LeastAreaQTD
		for leastArea.Areas != nil {
			sb.WriteString("\nleast_employees|")
			sb.WriteString(dat.Areas[0].Nome)
			sb.WriteString("|")
			sb.WriteString(strconv.Itoa(dat.Areas[0].Qtd))
			leastArea.Areas = leastArea.Areas.LeastAreaQTD
		}
		os.Stdout.WriteString(sb.String())
		wg.Done()
	}()

	// most_employees
	go func() {
		// montando a string
		var sb strings.Builder
		sb.WriteString("\nmost_employees|")
		sb.WriteString(mostArea.Areas.Nome)
		sb.WriteString("|")
		sb.WriteString(strconv.Itoa(mostArea.QTD))
		mostArea.Areas = mostArea.Areas.MostAreaQTD
		for mostArea.Areas != nil {
			sb.WriteString("\nmost_employees|")
			sb.WriteString(mostArea.Areas.Nome)
			sb.WriteString("|")
			sb.WriteString(strconv.Itoa(mostArea.QTD))
			mostArea.Areas = mostArea.Areas.MostAreaQTD
		}
		// exibindo
		os.Stdout.WriteString(sb.String())
		wg.Done()
	}()

	// area_max
	go func() {
		var sb strings.Builder
		for contador := 0; contador < sizeArea; contador++ {
			if dat.Areas[contador].Qtd != 0 {
				sb.WriteString("\narea_max|")
				sb.WriteString(dat.Areas[contador].Nome)
				sb.WriteString("|")
				sb.WriteString(dat.Areas[contador].StrMaxSal.Nome)
				sb.WriteString(" ")
				sb.WriteString(dat.Areas[contador].StrMaxSal.Sobrenome)
				sb.WriteString("|")
				sb.WriteString(strconv.FormatFloat(dat.Areas[contador].StrMaxSal.Salario, 'f', 2, 64))
				dat.Areas[contador].StrMaxSal = dat.Areas[contador].StrMaxSal.AreaMaxSal
				for dat.Areas[contador].StrMaxSal != nil {
					sb.WriteString("\narea_max|")
					sb.WriteString(dat.Areas[contador].Nome)
					sb.WriteString("|")
					sb.WriteString(dat.Areas[contador].StrMaxSal.Nome)
					sb.WriteString(" ")
					sb.WriteString(dat.Areas[contador].StrMaxSal.Sobrenome)
					sb.WriteString("|")
					sb.WriteString(strconv.FormatFloat(dat.Areas[contador].StrMaxSal.Salario, 'f', 2, 64))
					dat.Areas[contador].StrMaxSal = dat.Areas[contador].StrMaxSal.AreaMaxSal
				}
			}
		}
		os.Stdout.WriteString(sb.String())
		wg.Done()
	}()

	//  area_min
	go func() {
		// construindo a string
		var sb strings.Builder
		for contador := 0; contador < sizeArea; contador++ {
			if dat.Areas[contador].Qtd != 0 {
				sb.WriteString("\narea_min|")
				sb.WriteString(dat.Areas[contador].Nome)
				sb.WriteString("|")
				sb.WriteString(dat.Areas[contador].StrMinSal.Nome)
				sb.WriteString(" ")
				sb.WriteString(dat.Areas[contador].StrMinSal.Sobrenome)
				sb.WriteString("|")
				sb.WriteString(strconv.FormatFloat(dat.Areas[contador].StrMinSal.Salario, 'f', 2, 64))
				for dat.Areas[contador].StrMinSal != nil {
					sb.WriteString("\narea_min|")
					sb.WriteString(dat.Areas[contador].Nome)
					sb.WriteString("|")
					sb.WriteString(dat.Areas[contador].StrMinSal.Nome)
					sb.WriteString(" ")
					sb.WriteString(dat.Areas[contador].StrMinSal.Sobrenome)
					sb.WriteString("|")
					sb.WriteString(strconv.FormatFloat(dat.Areas[contador].StrMinSal.Salario, 'f', 2, 64))
					dat.Areas[contador].StrMinSal = dat.Areas[contador].StrMinSal.AreaMinSal
				}
			}
		}
		// exibindo
		os.Stdout.WriteString(sb.String())
		wg.Done()
	}()

	// last_name_max
	go func() {
		// construindo a string
		var sb strings.Builder
		for sobreNome, arrayFuncs := range bigSalaryByLastName {
			for idx := 0; idx < len(arrayFuncs); idx++ {
				sb.WriteString("\nlast_name_max|")
				sb.WriteString(sobreNome)
				sb.WriteString("|")
				sb.WriteString(arrayFuncs[idx].Nome)
				sb.WriteString(" ")
				sb.WriteString(sobreNome)
				sb.WriteString("|")
				sb.WriteString(strconv.FormatFloat(math.Round(arrayFuncs[idx].Salario), 'f', 2, 64))
			}
		}
		// exibindo
		os.Stdout.WriteString(sb.String())
		wg.Done()
	}()

	//exibição
	wg.Wait()
	fmt.Println("\n", time.Since(start))
}
