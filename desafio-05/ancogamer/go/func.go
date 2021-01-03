package main

import (
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"sync"

	jsoniter "github.com/json-iterator/go"
)

// Area  struct da area, carregando campos extras para serem utilizados durante os calculos ..
type Area struct {
	Codigo             string `json:"codigo"`
	Nome               string `json:"nome"`
	QTD                int
	AvgSal             float64
	MaxSal             float64
	MinSal             float64
	AreaMinFuncPointer *Employee
	AreaMaxFuncPointer *Employee
	MostAreaQTD        *Area
	LeastAreaQTD       *Area
}

// Employee = funcionario ..
type Employee struct {
	ID                          int     `json:"id"`
	Nome                        string  `json:"nome"`
	Sobrenome                   string  `json:"sobrenome"`
	Salario                     float64 `json:"salario"`
	Area                        string  `json:"area"`
	GlobalMaxSalEmployeePointer *Employee
	GlobalMinSalEmployeePointer *Employee
	AreaMaxSalEmployeePointer   *Employee
	AreaMinSalEmployeePointer   *Employee
}

// JSON união dos 2 para unmarshal ..
type JSON struct {
	EmployeesPointer []Employee `json:"funcionarios"`
	AreasPointer     []Area     `json:"areas"`
}

// MaiorSalGlobal aonde é armazenado o maior valor glogal de salario
type MaiorSalGlobal struct {
	Salario         float64
	EmployeePointer *Employee
}

// MenorSalGlobal aonde é armazenado o menor valor glogal de salario
type MenorSalGlobal struct {
	Salario         float64
	EmployeePointer *Employee
}

// LeastAreaQtd (least_employee) aonde é armazenado a maior(es) area(s) por quantidade de funcionario
type LeastAreaQtd struct {
	QTD          int
	AreasPointer *Area
}

// MostAreaQtd (most_employee)aonde é armazenado a maior(es) area(s) por quantidade de funcionario
type MostAreaQtd struct {
	QTD          int
	AreasPointer *Area
}

type lastNameSal map[string][]*Employee

/*
	calcula o maior salario por sobrenome,
	desconsiderando nomes + sobrenomes
	já existentes durante o calculo.
	Exemplo: se João Vitor, já existir,
	o próximo João Vitor informado é desconsiderado.
*/
func maxSalByLastName(bigSalaryByLastName *lastNameSal, dat JSON, count int) {
	sliceEmployee, found := (*bigSalaryByLastName)[dat.EmployeesPointer[count].Sobrenome]
	if found {
		for _, value := range sliceEmployee {
			if dat.EmployeesPointer[count].Salario == value.Salario {
				if value.Nome == dat.EmployeesPointer[count].Nome {
					return
				}
				(*bigSalaryByLastName)[dat.EmployeesPointer[count].Sobrenome] =
					append((*bigSalaryByLastName)[dat.EmployeesPointer[count].Sobrenome], &dat.EmployeesPointer[count])
				return
			}
			if dat.EmployeesPointer[count].Salario > value.Salario {
				if value.Nome == dat.EmployeesPointer[count].Nome {
					return
				}
				(*bigSalaryByLastName)[dat.EmployeesPointer[count].Sobrenome] = ([]*Employee{&dat.EmployeesPointer[count]})
				return
			}
		}
		return
	}
	(*bigSalaryByLastName)[dat.EmployeesPointer[count].Sobrenome] = []*Employee{&dat.EmployeesPointer[count]}
	return
}

func main() {
	/*
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
	*/
	//rawdata, err := ioutil.ReadFile(os.Args[len(os.Args)-1])
	rawdata, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		panic(err)
	}

	dat := JSON{}
	json := jsoniter.ConfigFastest
	if err = json.Unmarshal(rawdata, &dat); err != nil {
		panic(err)
	}

	var sizeArea int = len(dat.AreasPointer)

	var mediaGlobalSal float64

	globalMaxSal := MaiorSalGlobal{}
	globalMinSal := MenorSalGlobal{}
	bigSalaryByLastName := lastNameSal{}

	mostArea := MostAreaQtd{}
	leastArea := LeastAreaQtd{}

	var count int
	for count = 0; count < len(dat.EmployeesPointer); count++ {
		// calculo maior salario por sobrenome
		maxSalByLastName(&bigSalaryByLastName, dat, count)

		// calculo global_max
		if dat.EmployeesPointer[count].Salario > globalMaxSal.Salario {
			globalMaxSal.Salario = dat.EmployeesPointer[count].Salario
			globalMaxSal.EmployeePointer = &dat.EmployeesPointer[count]
		} else if dat.EmployeesPointer[count].Salario == globalMaxSal.Salario {
			globalMaxSal.EmployeePointer.GlobalMaxSalEmployeePointer = &dat.EmployeesPointer[count]
		}
		// calculo glogal_min
		if count == 0 {
			globalMinSal.Salario = dat.EmployeesPointer[count].Salario
			globalMinSal.EmployeePointer = &dat.EmployeesPointer[count]
		} else if dat.EmployeesPointer[count].Salario < globalMinSal.Salario {
			globalMinSal.Salario = dat.EmployeesPointer[count].Salario
			globalMinSal.EmployeePointer = &dat.EmployeesPointer[count]
		} else if dat.EmployeesPointer[count].Salario == globalMinSal.Salario {
			globalMinSal.EmployeePointer.GlobalMaxSalEmployeePointer = &dat.EmployeesPointer[count]
		}

		mediaGlobalSal += dat.EmployeesPointer[count].Salario

		for areaCount := 0; areaCount < sizeArea; areaCount++ {
			if dat.EmployeesPointer[count].Area == dat.AreasPointer[areaCount].Codigo {
				// calculo menor salario
				if dat.AreasPointer[areaCount].QTD == 0 {
					dat.AreasPointer[areaCount].MinSal = dat.EmployeesPointer[count].Salario
					dat.AreasPointer[areaCount].AreaMinFuncPointer = &dat.EmployeesPointer[count]
				} else if dat.EmployeesPointer[count].Salario == dat.AreasPointer[areaCount].MinSal {
					dat.AreasPointer[areaCount].AreaMinFuncPointer.AreaMinSalEmployeePointer = &dat.EmployeesPointer[count]
				}

				if dat.EmployeesPointer[count].Salario < dat.AreasPointer[areaCount].MinSal {
					dat.AreasPointer[areaCount].MinSal = dat.EmployeesPointer[count].Salario
					dat.AreasPointer[areaCount].AreaMinFuncPointer = &dat.EmployeesPointer[count]
				}

				dat.AreasPointer[areaCount].QTD++

				// calculo maior salario
				if dat.EmployeesPointer[count].Salario == dat.AreasPointer[areaCount].MaxSal {
					dat.AreasPointer[areaCount].AreaMaxFuncPointer.AreaMaxSalEmployeePointer = &dat.EmployeesPointer[count]
				}
				if dat.EmployeesPointer[count].Salario > dat.AreasPointer[areaCount].MaxSal {
					dat.AreasPointer[areaCount].MaxSal = dat.EmployeesPointer[count].Salario
					dat.AreasPointer[areaCount].AreaMaxFuncPointer = &dat.EmployeesPointer[count]
				}

				dat.AreasPointer[areaCount].AvgSal += dat.EmployeesPointer[count].Salario

				// calculo das areas most employee e least employee
				if dat.AreasPointer[areaCount].QTD == mostArea.QTD {
					mostArea.AreasPointer.MostAreaQTD = &dat.AreasPointer[areaCount]
				}
				if dat.AreasPointer[areaCount].QTD > mostArea.QTD {
					mostArea.QTD = dat.AreasPointer[areaCount].QTD
					mostArea.AreasPointer = &dat.AreasPointer[areaCount]
				}

			}
		}
	}
	wg := sync.WaitGroup{}
	wg.Add(8)

	leastArea.QTD = mostArea.QTD

	// exibindo global_avg

	os.Stdout.WriteString("global_avg|")
	os.Stdout.WriteString(strconv.FormatFloat(mediaGlobalSal/float64(count), 'f', 2, 64))

	// area avg
	// area_avg|<nome da área>|<salário médio>
	go func() {
		var sb strings.Builder
		for contador := 0; contador < sizeArea; contador++ {
			if dat.AreasPointer[contador].QTD != 0 {
				sb.WriteString("\narea_avg|")
				sb.WriteString(dat.AreasPointer[contador].Nome)
				sb.WriteString("|")
				sb.WriteString(strconv.FormatFloat(dat.AreasPointer[contador].AvgSal/float64(dat.AreasPointer[contador].QTD), 'f', 2, 64))
			}
		}
		// exibindo o area_avg
		os.Stdout.WriteString(sb.String())

		wg.Done()
	}()

	// glogal_max
	// global_max|<Nome Completo>|<Salário>
	go func() {
		// construindo a string
		var sb strings.Builder
		sb.WriteString("\nglobal_max|")
		sb.WriteString(globalMaxSal.EmployeePointer.Nome)
		sb.WriteString(" ")
		sb.WriteString(globalMaxSal.EmployeePointer.Sobrenome)
		sb.WriteString("|")
		sb.WriteString(strconv.FormatFloat(globalMaxSal.EmployeePointer.Salario, 'f', 2, 64))
		for globalMaxSal.EmployeePointer.GlobalMaxSalEmployeePointer != nil {
			sb.WriteString("\nglobal_max|")
			sb.WriteString(globalMaxSal.EmployeePointer.GlobalMaxSalEmployeePointer.Nome)
			sb.WriteString(" ")
			sb.WriteString(globalMaxSal.EmployeePointer.GlobalMaxSalEmployeePointer.Sobrenome)
			sb.WriteString("|")
			sb.WriteString(strconv.FormatFloat(globalMaxSal.EmployeePointer.GlobalMaxSalEmployeePointer.Salario, 'f', 2, 64))
			globalMaxSal.EmployeePointer.GlobalMaxSalEmployeePointer =
				globalMaxSal.EmployeePointer.GlobalMaxSalEmployeePointer.GlobalMaxSalEmployeePointer
		}
		// exibindo
		os.Stdout.WriteString(sb.String())

		wg.Done()
	}()

	// glogal_min
	// global_min|<nome completo>|<salário>
	go func() {
		// construindo a string
		var sb strings.Builder
		sb.WriteString("\nglobal_min|")
		sb.WriteString(globalMinSal.EmployeePointer.Nome)
		sb.WriteString(" ")
		sb.WriteString(globalMinSal.EmployeePointer.Sobrenome)
		sb.WriteString("|")
		sb.WriteString(strconv.FormatFloat(globalMinSal.EmployeePointer.Salario, 'f', 2, 64))
		for globalMinSal.EmployeePointer.GlobalMinSalEmployeePointer != nil {
			sb.WriteString("\nglobal_min|")
			sb.WriteString(globalMinSal.EmployeePointer.GlobalMinSalEmployeePointer.Nome)
			sb.WriteString(" ")
			sb.WriteString(globalMinSal.EmployeePointer.GlobalMinSalEmployeePointer.Sobrenome)
			sb.WriteString("|")
			sb.WriteString(strconv.FormatFloat(globalMinSal.EmployeePointer.GlobalMinSalEmployeePointer.Salario, 'f', 2, 64))
			globalMinSal.EmployeePointer.GlobalMaxSalEmployeePointer =
				globalMinSal.EmployeePointer.GlobalMinSalEmployeePointer.GlobalMinSalEmployeePointer
		}
		// exibindo
		os.Stdout.WriteString(sb.String())

		wg.Done()
	}()

	// least_employe
	// least_employees|<nome da área>|<número de funcionários>
	go func() {
		// calculando
		for contador := 1; contador < sizeArea; contador++ {
			if dat.AreasPointer[contador].QTD != 0 {
				if dat.AreasPointer[contador].QTD == leastArea.QTD {
					leastArea.AreasPointer.LeastAreaQTD = &dat.AreasPointer[contador]
				}
				if dat.AreasPointer[contador].QTD < leastArea.QTD {
					leastArea.QTD = dat.AreasPointer[contador].QTD
					leastArea.AreasPointer = &dat.AreasPointer[contador]
				}
			}

		}
		// construindo a string
		var sb strings.Builder
		sb.WriteString("\nleast_employees|")
		sb.WriteString(leastArea.AreasPointer.Nome)
		sb.WriteString("|")
		sb.WriteString(strconv.Itoa(leastArea.QTD))
		leastArea.AreasPointer = leastArea.AreasPointer.LeastAreaQTD
		for leastArea.AreasPointer != nil {
			sb.WriteString("\nleast_employees|")
			sb.WriteString(dat.AreasPointer[0].Nome)
			sb.WriteString("|")
			sb.WriteString(strconv.Itoa(dat.AreasPointer[0].QTD))
			leastArea.AreasPointer = leastArea.AreasPointer.LeastAreaQTD
		}
		// exibindo
		os.Stdout.WriteString(sb.String())

		wg.Done()
	}()

	// most_employees
	// most_employees|<nome da área>|<número de funcionários>
	go func() {
		// construindo a string
		var sb strings.Builder
		sb.WriteString("\nmost_employees|")
		sb.WriteString(mostArea.AreasPointer.Nome)
		sb.WriteString("|")
		sb.WriteString(strconv.Itoa(mostArea.QTD))
		mostArea.AreasPointer = mostArea.AreasPointer.MostAreaQTD
		for mostArea.AreasPointer != nil {
			sb.WriteString("\nmost_employees|")
			sb.WriteString(mostArea.AreasPointer.Nome)
			sb.WriteString("|")
			sb.WriteString(strconv.Itoa(mostArea.QTD))
			mostArea.AreasPointer = mostArea.AreasPointer.MostAreaQTD
		}
		// exibindo
		os.Stdout.WriteString(sb.String())

		wg.Done()
	}()

	// area_max
	// area_max|<nome da área>|<nome completo>|<salário máximo>
	go func() {
		// construindo 1 string para, com o valor de todas as areas
		var sb strings.Builder
		for contador := 0; contador < sizeArea; contador++ {
			if dat.AreasPointer[contador].QTD != 0 {
				sb.WriteString("\narea_max|")
				sb.WriteString(dat.AreasPointer[contador].Nome)
				sb.WriteString("|")
				sb.WriteString(dat.AreasPointer[contador].AreaMaxFuncPointer.Nome)
				sb.WriteString(" ")
				sb.WriteString(dat.AreasPointer[contador].AreaMaxFuncPointer.Sobrenome)
				sb.WriteString("|")
				sb.WriteString(strconv.FormatFloat(dat.AreasPointer[contador].AreaMaxFuncPointer.Salario, 'f', 2, 64))
				dat.AreasPointer[contador].AreaMaxFuncPointer = dat.AreasPointer[contador].AreaMaxFuncPointer.AreaMaxSalEmployeePointer
				for dat.AreasPointer[contador].AreaMaxFuncPointer != nil {
					sb.WriteString("\narea_max|")
					sb.WriteString(dat.AreasPointer[contador].Nome)
					sb.WriteString("|")
					sb.WriteString(dat.AreasPointer[contador].AreaMaxFuncPointer.Nome)
					sb.WriteString(" ")
					sb.WriteString(dat.AreasPointer[contador].AreaMaxFuncPointer.Sobrenome)
					sb.WriteString("|")
					sb.WriteString(strconv.FormatFloat(dat.AreasPointer[contador].AreaMaxFuncPointer.Salario, 'f', 2, 64))
					dat.AreasPointer[contador].AreaMaxFuncPointer = dat.AreasPointer[contador].AreaMaxFuncPointer.AreaMaxSalEmployeePointer
				}
			}
		}

		// exibindo
		os.Stdout.WriteString(sb.String())

		wg.Done()
	}()

	//  area_min
	//  area_min|<nome da área>|<nome completo>|<salário>
	go func() {
		// construindo a string
		var sb strings.Builder
		// construindo 1 string para, com o valor de todas as areas
		for contador := 0; contador < sizeArea; contador++ {
			if dat.AreasPointer[contador].QTD != 0 {
				sb.WriteString("\narea_min|")
				sb.WriteString(dat.AreasPointer[contador].Nome)
				sb.WriteString("|")
				sb.WriteString(dat.AreasPointer[contador].AreaMinFuncPointer.Nome)
				sb.WriteString(" ")
				sb.WriteString(dat.AreasPointer[contador].AreaMinFuncPointer.Sobrenome)
				sb.WriteString("|")
				sb.WriteString(strconv.FormatFloat(dat.AreasPointer[contador].AreaMinFuncPointer.Salario, 'f', 2, 64))
				dat.AreasPointer[contador].AreaMinFuncPointer = dat.AreasPointer[contador].AreaMinFuncPointer.AreaMinSalEmployeePointer
				for dat.AreasPointer[contador].AreaMinFuncPointer != nil {
					sb.WriteString("\narea_min|")
					sb.WriteString(dat.AreasPointer[contador].Nome)
					sb.WriteString("|")
					sb.WriteString(dat.AreasPointer[contador].AreaMinFuncPointer.Nome)
					sb.WriteString(" ")
					sb.WriteString(dat.AreasPointer[contador].AreaMinFuncPointer.Sobrenome)
					sb.WriteString("|")
					sb.WriteString(strconv.FormatFloat(dat.AreasPointer[contador].AreaMinFuncPointer.Salario, 'f', 2, 64))
					dat.AreasPointer[contador].AreaMinFuncPointer = dat.AreasPointer[contador].AreaMinFuncPointer.AreaMinSalEmployeePointer
				}
			}
		}
		// exibindo
		os.Stdout.WriteString(sb.String())

		wg.Done()
	}()

	// last_name_max
	// last_name_max|<sobrenome do funcionário>|<nome completo>|<salário>
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
				sb.WriteString(strconv.FormatFloat(arrayFuncs[idx].Salario, 'f', 2, 64))
			}
		}
		// exibindo
		os.Stdout.WriteString(sb.String())
		wg.Done()
	}()

	wg.Wait()
	os.Stdout.WriteString("\n")
}
