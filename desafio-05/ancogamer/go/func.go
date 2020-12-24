package main

import (
	"crypto/md5"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"sync"

	"github.com/jeffotoni/gconcat"
)

//Func ..
type Func struct {
	ID        int     `json:"id"`
	Nome      string  `json:"nome"`
	Sobrenome string  `json:"sobrenome"`
	Salario   float64 `json:"salario"`
	Area      string  `json:"area"`
}

// Area ..
type Area struct {
	Codigo       string `json:"codigo"`
	Nome         string `json:"nome"`
	Qtd          int
	MediaS       float64
	MaiorS       float64
	MenorS       float64
	Funcionarios []*Func

	AreaMax string
	AreaMin string
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
				(*bigSalaryByLastName)[l].LastNameMax = gconcat.Build((*bigSalaryByLastName)[l].LastNameMax, "\nlast_name_max|", dat.Funcs[c].Sobrenome, "|", dat.Funcs[c].Nome,
					" ", dat.Funcs[c].Sobrenome, "|",
					fmt.Sprintf("%.2f", dat.Funcs[c].Salario))
			} else if dat.Funcs[c].Salario == (*bigSalaryByLastName)[l].MaiorS {
				(*bigSalaryByLastName)[l].LastNameMax = gconcat.Build((*bigSalaryByLastName)[l].LastNameMax, "\nlast_name_max|", dat.Funcs[c].Sobrenome, "|", dat.Funcs[c].Nome,
					" ", dat.Funcs[c].Sobrenome, "|",
					fmt.Sprintf("%.2f", dat.Funcs[c].Salario))
			}
			return
		}
	}
	*bigSalaryByLastName = append(*bigSalaryByLastName, SobreS{
		LastNameMax: gconcat.Build("\nlast_name_max|", dat.Funcs[c].Sobrenome, "|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", dat.Funcs[c].Salario)),
		MaiorS:      dat.Funcs[c].Salario,
		SobreNome:   dat.Funcs[c].Sobrenome,
	})

	(*bigSalaryByLastName)[l].Funcionarios = append((*bigSalaryByLastName)[l].Funcionarios, &dat.Funcs[c].Nome)

	return

}

func main() {

	var arquivo string
	_, err := fmt.Scanf("%s", &arquivo)
	if err != nil {
		log.Fatal(err)
	}

	ctx, err := ioutil.ReadFile(arquivo)
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
			GlobalMax = gconcat.Build("global_max|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", maiorValor))
		case dat.Funcs[c].Salario == maiorValor:
			GlobalMax = gconcat.Build(GlobalMax, "\nglobal_max|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", maiorValor))
		}
		switch {
		case dat.Funcs[c].Salario < menorValor:
			GlobalMin = ""
			menorValor = dat.Funcs[c].Salario
			GlobalMin = gconcat.Build("global_min|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", menorValor))
		case dat.Funcs[c].Salario == menorValor:
			GlobalMin = gconcat.Build(GlobalMin, "\nglobal_min|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|", fmt.Sprintf("%.2f", menorValor))
		}
		mediaS += dat.Funcs[c].Salario

		for a := 0; a < sizeA; a++ {
			if dat.Funcs[c].Area == dat.Areas[a].Codigo {
				dat.Areas[a].Qtd++
				dat.Areas[a].Funcionarios = append(dat.Areas[a].Funcionarios, &dat.Funcs[c])
				//2
				if dat.Funcs[c].Salario > dat.Areas[a].MaiorS {
					dat.Areas[a].MaiorS = dat.Funcs[c].Salario
					dat.Areas[a].AreaMax = ""
					dat.Areas[a].AreaMax = gconcat.Build(dat.Areas[a].AreaMax, "\narea_max|", dat.Areas[a].Nome, "|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|",
						fmt.Sprintf("%.2f", dat.Areas[a].MaiorS))

				} else if dat.Funcs[c].Salario == dat.Areas[a].MaiorS {
					dat.Areas[a].AreaMax = gconcat.Build(dat.Areas[a].AreaMax, "\narea_max|", dat.Areas[a].Nome, "|", dat.Funcs[c].Nome, " ", dat.Funcs[c].Sobrenome, "|",
						fmt.Sprintf("%.2f", dat.Areas[a].MaiorS))
				}
				dat.Areas[a].MenorS = dat.Areas[a].MaiorS
				dat.Areas[a].MediaS += dat.Funcs[c].Salario
				//==================================================================
				//3
				if dat.Areas[a].Qtd > maiorArea {
					maiorArea = dat.Areas[a].Qtd
					MostEmploy = ""
					MostEmploy = gconcat.Build(MostEmploy, "\nmost_employees|", dat.Areas[a].Nome, "|", dat.Areas[a].Qtd)
				} else if dat.Areas[a].Qtd == maiorArea {
					MostEmploy = gconcat.Build(MostEmploy, "\nmost_employees|", dat.Areas[a].Nome, "|", dat.Areas[a].Qtd)

				}
				//==================================================================
			}
		}

	}

	wg := sync.WaitGroup{}
	wg.Add(2)
	//2
	go func() {
		for a := 0; a < sizeA; a++ {
			for k := 0; k < len(dat.Areas[a].Funcionarios); k++ {
				if dat.Areas[a].Funcionarios[k].Salario < dat.Areas[a].MenorS {
					dat.Areas[a].MenorS = dat.Areas[a].Funcionarios[k].Salario
					dat.Areas[a].AreaMin = ""
					dat.Areas[a].AreaMin = gconcat.Build(dat.Areas[a].AreaMin, "\narea_min|", dat.Areas[a].Nome, "|", dat.Areas[a].Funcionarios[k].Nome, " ",
						dat.Areas[a].Funcionarios[k].Sobrenome, "|",
						fmt.Sprintf("%.2f", dat.Areas[a].MenorS))
				} else if dat.Areas[a].Funcionarios[k].Salario == dat.Areas[a].MenorS {
					dat.Areas[a].AreaMin = gconcat.Build(dat.Areas[a].AreaMin, "\narea_min|", dat.Areas[a].Nome, "|", dat.Areas[a].Funcionarios[k].Nome, " ",
						dat.Areas[a].Funcionarios[k].Sobrenome, "|",
						fmt.Sprintf("%.2f", dat.Areas[a].MenorS))
				}
			}
			//2
			AreasMin = gconcat.Build(AreasMin, dat.Areas[a].AreaMin)
			AreasMax = gconcat.Build(AreasMax, dat.Areas[a].AreaMax)
			if dat.Areas[a].Qtd == 0 {

			} else {
				AvgA = gconcat.Build(AvgA, "\narea_avg|", dat.Areas[a].Nome, "|", fmt.Sprintf("%.2f", dat.Areas[a].MediaS/float64(dat.Areas[a].Qtd)))
			}
		}
		wg.Done()
	}()
	go func() {
		//3
		menorArea = dat.Areas[0].Qtd
		for a := 1; a < sizeA; a++ {
			if dat.Areas[a].Qtd == 0 {
			} else {
				if dat.Areas[a].Qtd < menorArea {
					LeastEmploy = ""
					LeastEmploy = gconcat.Build(LeastEmploy, "\nleast_employees|", dat.Areas[a].Nome, "|", dat.Areas[a].Qtd)
					menorArea = dat.Areas[a].Qtd
				} else if dat.Areas[a].Qtd == menorArea {
					menorArea = dat.Areas[a].Qtd
					LeastEmploy = gconcat.Build(LeastEmploy, "\nleast_employees|", dat.Areas[a].Nome, "|", dat.Areas[a].Qtd)
				}
			}
		}
		wg.Done()
	}()

	for i := 0; i < len(bigSalaryByLastName); i++ {
		LastNameMax = gconcat.Build(LastNameMax, bigSalaryByLastName[i].LastNameMax)
	}
	//exibição
	wg.Wait()

	str := gconcat.Build(GlobalMax, "\n", GlobalMin, "\n", "global_avg|", fmt.Sprintf("%.2f", mediaS/float64(c)), AreasMax, AreasMin, AvgA, MostEmploy, LeastEmploy, LastNameMax)
	fmt.Println(str)
	/*
		file, err := os.Create("result.txt")
		if err != nil {
			log.Fatal(err)
		}
		_, err = file.Write([]byte(str))
		if err != nil {
			log.Fatal(err)
		}
		file.Close()
	*/
	fmt.Printf("%x", md5.Sum([]byte(str)))

}
