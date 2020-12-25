package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

// Area ..
type Area struct {
	Codigo string `json:"codigo"`
	Nome   string `json:"nome"`
	Qtd    int
	MediaS float64
	MaiorS float64
	MenorS float64
	//MenorSFuncionarioPointer *Func

	AreaMax string
	AreaMin string
}

//Func ..
type Func struct {
	ID        int     `json:"id"`
	Nome      string  `json:"nome"`
	Sobrenome string  `json:"sobrenome"`
	Salario   float64 `json:"salario"`
	Area      string  `json:"area"`
}

//JSON ..
type JSON struct {
	Funcs []Func `json:"funcionarios"`
	Areas []Area `json:"areas"`
}

//2
var (
	AvgA        string
	AreasMax    string
	AreasMin    string
	c           int
	LastNameMax string
)

//SobreS .
type SobreS struct {
	LastNameMax  string
	MaiorS       float64
	SobreNome    string
	Funcionarios []*string
}

//X ..
func X(bigSalaryByLastName *[]SobreS, dat JSON) {
	var l int
	for l = 0; l < len(*bigSalaryByLastName); l++ {
		if dat.Funcs[c].Sobrenome == (*bigSalaryByLastName)[l].SobreNome {
			for k := 0; k < len((*bigSalaryByLastName)[l].Funcionarios); k++ {
				if &dat.Funcs[c].Nome == (*bigSalaryByLastName)[l].Funcionarios[k] {
					return
				}
			}
			if dat.Funcs[c].Salario > (*bigSalaryByLastName)[l].MaiorS {
				(*bigSalaryByLastName)[l].MaiorS = dat.Funcs[c].Salario
				(*bigSalaryByLastName)[l].LastNameMax = ""
				(*bigSalaryByLastName)[l].LastNameMax = Build((*bigSalaryByLastName)[l].LastNameMax, "\nlast_name_max|", dat.Funcs[c].Sobrenome, "|", dat.Funcs[c].Nome,
					" ", dat.Funcs[c].Sobrenome, "|",
					fmt.Sprintf("%.2f", dat.Funcs[c].Salario))
			} else if dat.Funcs[c].Salario == (*bigSalaryByLastName)[l].MaiorS {
				(*bigSalaryByLastName)[l].LastNameMax = Build((*bigSalaryByLastName)[l].LastNameMax, "\nlast_name_max|", dat.Funcs[c].Sobrenome, "|", dat.Funcs[c].Nome,
					" ", dat.Funcs[c].Sobrenome, "|",
					fmt.Sprintf("%.2f", dat.Funcs[c].Salario))
			}
			return
		}
	}
	*bigSalaryByLastName = append(*bigSalaryByLastName, SobreS{
		LastNameMax: Build("\nlast_name_max|", dat.Funcs[c].Sobrenome, "|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", dat.Funcs[c].Salario)),
		MaiorS:      dat.Funcs[c].Salario,
		SobreNome:   dat.Funcs[c].Sobrenome,
	})

	(*bigSalaryByLastName)[l].Funcionarios = append((*bigSalaryByLastName)[l].Funcionarios, &dat.Funcs[c].Nome)

	return

}

func main() {
	start := time.Now()
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

	ctx, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	var dat JSON
	err = json.Unmarshal(ctx, &dat)
	if err != nil {
		log.Fatal(err)
	}

	var maiorValor float64 = dat.Funcs[0].Salario

	var menorValor float64 = dat.Funcs[0].Salario

	var maiorArea int
	var menorArea int = 1

	var mediaS float64

	var GlobalMax string
	var GlobalMin string
	var MostEmploy string
	var LeastEmploy string

	var sizeA int = len(dat.Areas)

	var bigSalaryByLastName []SobreS

	for c = 0; c < len(dat.Funcs); c++ {
		//4
		X(&bigSalaryByLastName, dat)

		//1
		switch {
		case dat.Funcs[c].Salario > maiorValor:
			GlobalMax = ""
			maiorValor = dat.Funcs[c].Salario
			GlobalMax = Build("global_max|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", maiorValor))
		case dat.Funcs[c].Salario == maiorValor:
			GlobalMax = Build(GlobalMax, "\nglobal_max|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", maiorValor))
		}
		switch {
		case dat.Funcs[c].Salario < menorValor:
			GlobalMin = ""
			menorValor = dat.Funcs[c].Salario
			GlobalMin = Build("global_min|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", menorValor))
		case dat.Funcs[c].Salario == menorValor:
			GlobalMin = Build(GlobalMin, "\nglobal_min|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", menorValor))
		}
		mediaS += dat.Funcs[c].Salario

		for a := 0; a < sizeA; a++ {
			if dat.Funcs[c].Area == dat.Areas[a].Codigo {
				if dat.Areas[a].Qtd == 0 {
					dat.Areas[a].MenorS = dat.Funcs[c].Salario
				}
				dat.Areas[a].Qtd++
				//2
				//calculo menor salario
				if dat.Funcs[c].Salario < dat.Areas[a].MenorS {
					dat.Areas[a].MenorS = dat.Funcs[c].Salario
					dat.Areas[a].AreaMin = ""
					var sb strings.Builder
					sb.WriteString(dat.Areas[a].AreaMin)
					sb.WriteString("\narea_min|")
					sb.WriteString(dat.Areas[a].Nome)
					sb.WriteString("|")
					sb.WriteString(dat.Funcs[c].Nome)
					sb.WriteString(" ")
					sb.WriteString(dat.Funcs[c].Sobrenome)
					sb.WriteString("|")
					sb.WriteString(fmt.Sprintf("%.2f", dat.Funcs[c].Salario))
					dat.Areas[a].AreaMin = sb.String()
					//dat.Areas[a].AreaMin = Build(dat.Areas[a].AreaMin, "\narea_min|", dat.Areas[a].Nome, "|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", dat.Funcs[c].Salario))

				}
				if dat.Funcs[c].Salario == dat.Areas[a].MenorS {
					var sb strings.Builder
					sb.WriteString(dat.Areas[a].AreaMin)
					sb.WriteString("\narea_min|")
					sb.WriteString(dat.Areas[a].Nome)
					sb.WriteString("|")
					sb.WriteString(dat.Funcs[c].Nome)
					sb.WriteString(" ")
					sb.WriteString(dat.Funcs[c].Sobrenome)
					sb.WriteString("|")
					sb.WriteString(fmt.Sprintf("%.2f", dat.Funcs[c].Salario))
					dat.Areas[a].AreaMin = sb.String()
					//dat.Areas[a].AreaMin = Build(dat.Areas[a].AreaMin, "\narea_min|", dat.Areas[a].Nome, "|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", dat.Funcs[c].Salario))
				}
				//calculo maior salario
				if dat.Funcs[c].Salario > dat.Areas[a].MaiorS {
					dat.Areas[a].MaiorS = dat.Funcs[c].Salario
					dat.Areas[a].AreaMax = ""
					dat.Areas[a].AreaMax = Build(dat.Areas[a].AreaMax, "\narea_max|", dat.Areas[a].Nome, "|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|",
						fmt.Sprintf("%.2f", dat.Areas[a].MaiorS))

				} else if dat.Funcs[c].Salario == dat.Areas[a].MaiorS {
					dat.Areas[a].AreaMax = Build(dat.Areas[a].AreaMax, "\narea_max|", dat.Areas[a].Nome, "|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|",
						fmt.Sprintf("%.2f", dat.Areas[a].MaiorS))
				}
				dat.Areas[a].MediaS += dat.Funcs[c].Salario
				//==================================================================
				//3

				if dat.Areas[a].Qtd > maiorArea {
					a := a
					var sb strings.Builder
					maiorArea = dat.Areas[a].Qtd
					MostEmploy = ""

					sb.WriteString(MostEmploy)
					sb.WriteString("\nmost_employees|")
					sb.WriteString(dat.Areas[a].Nome)
					sb.WriteString("|")
					sb.WriteString(strconv.Itoa(dat.Areas[a].Qtd))
					MostEmploy = sb.String()

					//	MostEmploy = Build(MostEmploy, "\nmost_employees|", dat.Areas[a].Nome, "|", dat.Areas[a].Qtd)
				} else if dat.Areas[a].Qtd == maiorArea {
					var sb strings.Builder
					sb.WriteString(MostEmploy)
					sb.WriteString("\nmost_employees|")
					sb.WriteString(dat.Areas[a].Nome)
					sb.WriteString("|")
					sb.WriteString(strconv.Itoa(dat.Areas[a].Qtd))
					MostEmploy = sb.String()
					//MostEmploy = Build(MostEmploy, "\nmost_employees|", dat.Areas[a].Nome, "|", dat.Areas[a].Qtd)
				}

				//==================================================================
			}
		}

	}

	wg := sync.WaitGroup{}
	wg.Add(2)
	go func() {
		//3
		menorArea = dat.Areas[0].Qtd
		for a := 1; a < sizeA; a++ {
			if dat.Areas[a].Qtd != 0 {
				var sb strings.Builder
				sb.WriteString(AvgA)
				sb.WriteString("\narea_avg|")
				sb.WriteString(dat.Areas[a].Nome)
				sb.WriteString("|")
				sb.WriteString(fmt.Sprintf("%.2f", dat.Areas[a].MediaS/float64(dat.Areas[a].Qtd)))
				AvgA = sb.String()
				/*	AvgA = Build(AvgA,
					"\narea_avg|",
					dat.Areas[a].Nome,
					"|",
					fmt.Sprintf("%.2f", dat.Areas[a].MediaS/float64(dat.Areas[a].Qtd)))*/
			}
			var sb strings.Builder
			sb.WriteString(AreasMax)
			sb.WriteString(dat.Areas[a].AreaMax)
			AreasMax = sb.String()
			sb.Reset()
			//AreasMax = Build(AreasMax, dat.Areas[a].AreaMax)
			sb.WriteString(AreasMin)
			sb.WriteString(dat.Areas[a].AreaMin)
			AreasMin = sb.String()
			//AreasMin = Build(AreasMin, dat.Areas[a].AreaMin)
			if dat.Areas[a].Qtd == 0 {
			} else {
				if dat.Areas[a].Qtd < menorArea {
					LeastEmploy = ""
					LeastEmploy = Build(LeastEmploy, "\nleast_employees|", dat.Areas[a].Nome, "|", dat.Areas[a].Qtd)
					menorArea = dat.Areas[a].Qtd
				} else if dat.Areas[a].Qtd == menorArea {
					menorArea = dat.Areas[a].Qtd
					LeastEmploy = Build(LeastEmploy, "\nleast_employees|", dat.Areas[a].Nome, "|", dat.Areas[a].Qtd)
				}
			}
		}
		wg.Done()
	}()
	go func() {
		for i := 0; i < len(bigSalaryByLastName); i++ {
			var sb strings.Builder
			sb.WriteString(LastNameMax)
			sb.WriteString(bigSalaryByLastName[i].LastNameMax)
			LastNameMax = sb.String()
			//LastNameMax = Build(LastNameMax, bigSalaryByLastName[i].LastNameMax)
		}
		wg.Done()
	}()

	//exibição
	wg.Wait()
	var sb strings.Builder

	sb.Reset()
	sb.WriteString(GlobalMax)
	sb.WriteString("\n")
	sb.WriteString(GlobalMin)
	sb.WriteString("global_avg|")
	sb.WriteString(fmt.Sprintf("%.2f", mediaS/float64(c)))
	sb.WriteString(AreasMax)
	sb.WriteString(AreasMin)
	sb.WriteString(AvgA)
	sb.WriteString(MostEmploy)
	sb.WriteString(LeastEmploy)
	sb.WriteString(LastNameMax)
	sb.WriteString(AreasMax)
	os.Stdout.WriteString(sb.String())

	//os.Stdout.WriteString(Build(GlobalMax, "\n", GlobalMin, "\n", "global_avg|", fmt.Sprintf("%.2f", mediaS/float64(c)), AreasMax, AreasMin, AvgA, MostEmploy, LeastEmploy, LastNameMax))

	fmt.Print("\n took ", time.Since(start))

	/*
		file, err := os.Create("result.txt")
		if err != nil {
			log.Fatal(err)
		}
		_, err = file.Write([]byte(sb.String()))
		if err != nil {
			log.Fatal(err)
		}
		file.Close()

	*/
	//	fmt.Printf("%x", md5.Sum([]byte()))

}

//Versão simplista da https://github.com/jeffotoni/gconcat/blob/master/main.go
func Build(strs ...interface{}) string {
	var sb strings.Builder
	for _, str := range strs {
		sb.WriteString(buildStr(str))
	}
	return sb.String()
}

//buildStr monta a string
func buildStr(str interface{}) string {
	switch str.(type) {
	case string:
		return string(str.(string))
	case int:
		return strconv.Itoa(str.(int))
	}
	return ""
}
