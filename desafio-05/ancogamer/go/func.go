package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

// Area  struct da area, carregando campos extras para serem utilizados durante os calculos ..
type Area struct {
	Codigo string `json:"codigo"`
	Nome   string `json:"nome"`
	Qtd    int
	AvgSal float64
	MaxSal float64
	MinSal float64
	//MenorSFuncionarioPointer *Employee
	StrMinSal strings.Builder
	StrMaxSal strings.Builder
}

//Employee , funcionario ..
type Employee struct {
	ID        int     `json:"id"`
	Nome      string  `json:"nome"`
	Sobrenome string  `json:"sobrenome"`
	Salario   float64 `json:"salario"`
	Area      string  `json:"area"`
}

//JSON união dos 2 para unmarshal ..
type JSON struct {
	Funcs []Employee `json:"funcionarios"`
	Areas []Area     `json:"areas"`
}

var c int

// lastNameSal ..
type lastNameSal struct {
	LastNameMax  strings.Builder
	MaxSal       float64
	SobreNome    string
	Funcionarios []string
}

//X , perdoa a falta de criatividade, a função X, calcula o maior salario por sobrenome, desconsiderando nomes + sobrenomes já existentes durante o calculo..
//exemplo: se João Vitor, já existir, o próximo João Vitor informado é desconsiderado.
func X(bigSalaryByLastName *[]lastNameSal, dat JSON) {
	var l int
	for l = 0; l < len(*bigSalaryByLastName); l++ {
		if dat.Funcs[c].Sobrenome == (*bigSalaryByLastName)[l].SobreNome {
			for k := 0; k < len((*bigSalaryByLastName)[l].Funcionarios); k++ {
				if dat.Funcs[c].Nome == (*bigSalaryByLastName)[l].Funcionarios[k] {
					return
				}
			}
			if dat.Funcs[c].Salario > (*bigSalaryByLastName)[l].MaxSal {
				(*bigSalaryByLastName)[l].MaxSal = dat.Funcs[c].Salario
				(*bigSalaryByLastName)[l].LastNameMax.Reset()
				(*bigSalaryByLastName)[l].LastNameMax.WriteString("\nlast_name_max|")
				(*bigSalaryByLastName)[l].LastNameMax.WriteString(dat.Funcs[c].Sobrenome)
				(*bigSalaryByLastName)[l].LastNameMax.WriteString("|")
				(*bigSalaryByLastName)[l].LastNameMax.WriteString(dat.Funcs[c].Nome)
				(*bigSalaryByLastName)[l].LastNameMax.WriteString(" ")
				(*bigSalaryByLastName)[l].LastNameMax.WriteString(dat.Funcs[c].Sobrenome)
				(*bigSalaryByLastName)[l].LastNameMax.WriteString("|")
				(*bigSalaryByLastName)[l].LastNameMax.WriteString(strconv.FormatFloat(math.Round(dat.Funcs[c].Salario), 'f', 6, 64))
				return
			}
			if dat.Funcs[c].Salario == (*bigSalaryByLastName)[l].MaxSal {
				(*bigSalaryByLastName)[l].LastNameMax.WriteString("\nlast_name_max|")
				(*bigSalaryByLastName)[l].LastNameMax.WriteString(dat.Funcs[c].Sobrenome)
				(*bigSalaryByLastName)[l].LastNameMax.WriteString("|")
				(*bigSalaryByLastName)[l].LastNameMax.WriteString(dat.Funcs[c].Nome)
				(*bigSalaryByLastName)[l].LastNameMax.WriteString(" ")
				(*bigSalaryByLastName)[l].LastNameMax.WriteString(dat.Funcs[c].Sobrenome)
				(*bigSalaryByLastName)[l].LastNameMax.WriteString("|")
				(*bigSalaryByLastName)[l].LastNameMax.WriteString(strconv.FormatFloat(math.Round(dat.Funcs[c].Salario), 'f', 6, 64))
				return
			}
		}
	}
	*bigSalaryByLastName = append(*bigSalaryByLastName, lastNameSal{
		MaxSal:    dat.Funcs[c].Salario,
		SobreNome: dat.Funcs[c].Sobrenome,
	})

	(*bigSalaryByLastName)[l].LastNameMax.WriteString("\nlast_name_max|")
	(*bigSalaryByLastName)[l].LastNameMax.WriteString(dat.Funcs[c].Sobrenome)
	(*bigSalaryByLastName)[l].LastNameMax.WriteString("|")
	(*bigSalaryByLastName)[l].LastNameMax.WriteString(dat.Funcs[c].Nome)
	(*bigSalaryByLastName)[l].LastNameMax.WriteString(" ")
	(*bigSalaryByLastName)[l].LastNameMax.WriteString(dat.Funcs[c].Sobrenome)
	(*bigSalaryByLastName)[l].LastNameMax.WriteString("|")
	(*bigSalaryByLastName)[l].LastNameMax.WriteString(strconv.FormatFloat(math.Round(dat.Funcs[c].Salario), 'f', 6, 64))
	// appendando o funcionario novo ao array de funcionarios de mesmo sobrenome
	(*bigSalaryByLastName)[l].Funcionarios = append((*bigSalaryByLastName)[l].Funcionarios, dat.Funcs[c].Nome)
	return

}

func main() {
//	start := time.Now()
	/*
		var optCPUProfile string

		flag.StringVar(&optCPUProfile, "cpuprofile", "", "write cpu profile to file")
		flag.Parse()
		if optCPUProfile != "" {
			println("to aqui")
			f, err := os.Create(optCPUProfile)
			if err != nil {
				log.Fatal(err)
			}
			pprof.StartCPUProfile(f)
			defer pprof.StopCPUProfile()
		}
	*/

	rawdata, err := ioutil.ReadFile(os.Args[len(os.Args)-1])
	if err != nil {
		log.Fatal(err)
	}
	var dat JSON
	err = json.Unmarshal(rawdata, &dat)
	if err != nil {
		log.Fatal(err)
	}

	var maiorValor float64 = dat.Funcs[0].Salario

	var menorValor float64 = dat.Funcs[0].Salario

	var maiorArea int

	var mediaGlobalSal float64

	var globalMax, globalMin strings.Builder
	var mostAndLestEmploy strings.Builder

	var sizeArea int = len(dat.Areas)

	var bigSalaryByLastName []lastNameSal

	for c = 0; c < len(dat.Funcs); c++ {
		// Calculo elementos parte 4
		X(&bigSalaryByLastName, dat)

		// Parte 1
		if dat.Funcs[c].Salario > maiorValor {
			maiorValor = dat.Funcs[c].Salario
			globalMax.Reset()
			globalMax.WriteString("global_max|")
			globalMax.WriteString(dat.Funcs[c].Nome)
			globalMax.WriteString(" ")
			globalMax.WriteString(dat.Funcs[c].Sobrenome)
			globalMax.WriteString("|")
			globalMax.WriteString(strconv.FormatFloat(math.Round(maiorValor), 'f', 6, 64))
		} else if dat.Funcs[c].Salario == maiorValor {
			globalMax.WriteString("\nglobal_max|")
			globalMax.WriteString(dat.Funcs[c].Nome)
			globalMax.WriteString(" ")
			globalMax.WriteString(dat.Funcs[c].Sobrenome)
			globalMax.WriteString("|")
			globalMax.WriteString(strconv.FormatFloat(math.Round(maiorValor), 'f', 6, 64))
		}
		if dat.Funcs[c].Salario < menorValor {
			menorValor = dat.Funcs[c].Salario
			globalMin.Reset()
			globalMin.WriteString("global_min|")
			globalMin.WriteString(dat.Funcs[c].Nome)
			globalMin.WriteString(" ")
			globalMin.WriteString(dat.Funcs[c].Sobrenome)
			globalMin.WriteString("|")
			globalMin.WriteString(strconv.FormatFloat(math.Round(menorValor), 'f', 6, 64))
		} else if dat.Funcs[c].Salario == menorValor {
			globalMin.WriteString("\nglobal_min|")
			globalMin.WriteString(dat.Funcs[c].Nome)
			globalMin.WriteString(" ")
			globalMin.WriteString(dat.Funcs[c].Sobrenome)
			globalMin.WriteString("|")
			globalMin.WriteString(strconv.FormatFloat(math.Round(menorValor), 'f', 6, 64))
		}

		mediaGlobalSal += dat.Funcs[c].Salario

		for a := 0; a < sizeArea; a++ {
			if dat.Funcs[c].Area == dat.Areas[a].Codigo {
				if dat.Areas[a].Qtd == 0 {
					dat.Areas[a].MinSal = dat.Funcs[c].Salario
				}
				dat.Areas[a].Qtd++
				// parte 2
				// calculo menor salario
				switch {
				case dat.Funcs[c].Salario < dat.Areas[a].MinSal:
					dat.Areas[a].MinSal = dat.Funcs[c].Salario
					dat.Areas[a].StrMinSal.Reset()
					dat.Areas[a].StrMinSal.WriteString("\narea_min|")
					dat.Areas[a].StrMinSal.WriteString(dat.Areas[a].Nome)
					dat.Areas[a].StrMinSal.WriteString("|")
					dat.Areas[a].StrMinSal.WriteString(dat.Funcs[c].Nome)
					dat.Areas[a].StrMinSal.WriteString(" ")
					dat.Areas[a].StrMinSal.WriteString(dat.Funcs[c].Sobrenome)
					dat.Areas[a].StrMinSal.WriteString("|")
					dat.Areas[a].StrMinSal.WriteString(strconv.FormatFloat(math.Round(dat.Funcs[c].Salario), 'f', 6, 64))
					break
				case dat.Funcs[c].Salario == dat.Areas[a].MinSal:
					dat.Areas[a].StrMinSal.Reset()
					dat.Areas[a].StrMinSal.WriteString("\narea_min|")
					dat.Areas[a].StrMinSal.WriteString(dat.Areas[a].Nome)
					dat.Areas[a].StrMinSal.WriteString("|")
					dat.Areas[a].StrMinSal.WriteString(dat.Funcs[c].Nome)
					dat.Areas[a].StrMinSal.WriteString(" ")
					dat.Areas[a].StrMinSal.WriteString(dat.Funcs[c].Sobrenome)
					dat.Areas[a].StrMinSal.WriteString("|")
					dat.Areas[a].StrMinSal.WriteString(strconv.FormatFloat(math.Round(dat.Funcs[c].Salario), 'f', 6, 64))
					break
				}
				// calculo maior salario
				switch {
				case dat.Funcs[c].Salario > dat.Areas[a].MaxSal:
					dat.Areas[a].MaxSal = dat.Funcs[c].Salario
					dat.Areas[a].StrMaxSal.Reset()
					dat.Areas[a].StrMaxSal.WriteString("\narea_max|")
					dat.Areas[a].StrMaxSal.WriteString(dat.Areas[a].Nome)
					dat.Areas[a].StrMaxSal.WriteString("|")
					dat.Areas[a].StrMaxSal.WriteString(dat.Funcs[c].Nome)
					dat.Areas[a].StrMaxSal.WriteString(" ")
					dat.Areas[a].StrMaxSal.WriteString(dat.Funcs[c].Sobrenome)
					dat.Areas[a].StrMaxSal.WriteString("|")
					dat.Areas[a].StrMaxSal.WriteString(strconv.FormatFloat(math.Round(dat.Areas[a].MaxSal), 'f', 6, 64))
					break
				case dat.Funcs[c].Salario == dat.Areas[a].MaxSal:
					dat.Areas[a].StrMaxSal.WriteString("\narea_max|")
					dat.Areas[a].StrMaxSal.WriteString(dat.Areas[a].Nome)
					dat.Areas[a].StrMaxSal.WriteString("|")
					dat.Areas[a].StrMaxSal.WriteString(dat.Funcs[c].Nome)
					dat.Areas[a].StrMaxSal.WriteString(" ")
					dat.Areas[a].StrMaxSal.WriteString(dat.Funcs[c].Sobrenome)
					dat.Areas[a].StrMaxSal.WriteString("|")
					dat.Areas[a].StrMaxSal.WriteString(strconv.FormatFloat(math.Round(dat.Areas[a].MaxSal), 'f', 6, 64))
					break
				}
				dat.Areas[a].AvgSal += dat.Funcs[c].Salario

				// parte 3
				switch {
				case dat.Areas[a].Qtd > maiorArea:
					maiorArea = dat.Areas[a].Qtd
					mostAndLestEmploy.Reset()
					mostAndLestEmploy.WriteString("\nmost_employees|")
					mostAndLestEmploy.WriteString(dat.Areas[a].Nome)
					mostAndLestEmploy.WriteString("|")
					mostAndLestEmploy.WriteString(strconv.Itoa(dat.Areas[a].Qtd))
				case dat.Areas[a].Qtd == maiorArea:
					mostAndLestEmploy.Reset()
					mostAndLestEmploy.WriteString("\nmost_employees|")
					mostAndLestEmploy.WriteString(dat.Areas[a].Nome)
					mostAndLestEmploy.WriteString("|")
					mostAndLestEmploy.WriteString(strconv.Itoa(dat.Areas[a].Qtd))
				}
			}
		}
	}

	// exibindo os global_max, global_min, global_avg
	os.Stdout.WriteString(globalMax.String())
	os.Stdout.WriteString("\n")
	os.Stdout.WriteString(globalMin.String())
	os.Stdout.WriteString("global_avg|")
	os.Stdout.WriteString(strconv.FormatFloat(math.Round(mediaGlobalSal/float64(c)), 'f', 6, 64))

	// exibindo os most_employees
	os.Stdout.WriteString(mostAndLestEmploy.String())

	wg := sync.WaitGroup{}
	wg.Add(2)

	// parte 3
	go func() {
		menorArea := dat.Areas[0].Qtd
		for a := 1; a < sizeArea; a++ {
			if dat.Areas[a].Qtd != 0 {
				var sb strings.Builder
				sb.WriteString("\narea_avg|")
				sb.WriteString(dat.Areas[a].Nome)
				sb.WriteString("|")
				sb.WriteString(strconv.FormatFloat(math.Round(dat.Areas[a].AvgSal/float64(dat.Areas[a].Qtd)), 'f', 6, 64))
				os.Stdout.WriteString(sb.String())
			}

			// exibindo o area_max
			os.Stdout.WriteString(dat.Areas[a].StrMaxSal.String())
			// exibindo o area_min
			os.Stdout.WriteString(dat.Areas[a].StrMinSal.String())

			if dat.Areas[a].Qtd == 0 {
			} else {
				if dat.Areas[a].Qtd < menorArea {
					menorArea = dat.Areas[a].Qtd
					mostAndLestEmploy.Reset()
					mostAndLestEmploy.WriteString("\nleast_employees|")
					mostAndLestEmploy.WriteString(dat.Areas[a].Nome)
					mostAndLestEmploy.WriteString("|")
					mostAndLestEmploy.WriteString(strconv.Itoa(dat.Areas[a].Qtd))
				} else if dat.Areas[a].Qtd == menorArea {
					menorArea = dat.Areas[a].Qtd
					mostAndLestEmploy.Reset()
					mostAndLestEmploy.WriteString("\nleast_employees|")
					mostAndLestEmploy.WriteString(dat.Areas[a].Nome)
					mostAndLestEmploy.WriteString("|")
					mostAndLestEmploy.WriteString(strconv.Itoa(dat.Areas[a].Qtd))
				}
			}
		}
		// exibindo os least_employess
		os.Stdout.WriteString(mostAndLestEmploy.String())
		wg.Done()
	}()

	go func() {
		var sb strings.Builder
		for i := 0; i < len(bigSalaryByLastName); i++ {
			sb.WriteString(bigSalaryByLastName[i].LastNameMax.String())
		}
		// exibindo os last_name_max
		os.Stdout.WriteString(sb.String())
		wg.Done()
	}()
	//exibição
	wg.Wait()
}
