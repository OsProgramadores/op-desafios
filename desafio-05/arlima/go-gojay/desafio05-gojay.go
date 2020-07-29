// Adriano Roberto de Lima
// Desafio 05 - em GO !
// Usando Gojay

package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"math"
	"os"

	"github.com/francoispqt/gojay"
)

type funcrec struct {
	id        int
	nome      string
	sobrenome string
	salario   float64
	area      string
}

type arearec struct {
	codigo string
	nome   string
}

type listareas struct {
	area     *arearec
	nomearea map[string]string
}

type listfuncs struct {
	funcionario *funcrec
	res         resultados
}

type empresa struct {
	funcionarios *listfuncs
	areas        *listareas
}

type resultados struct {
	globalmin      float64
	globalmax      float64
	globalavg      float64
	contaemp       float64
	empmin         []funcrec
	empmax         []funcrec
	empareamin     map[string][]funcrec
	empareamax     map[string][]funcrec
	emplastnamemax map[string][]funcrec
	areaavg        map[string]float64
	areamin        map[string]float64
	areamax        map[string]float64
	countarea      map[string]float64
	lastnamemax    map[string]float64
	countlastname  map[string]float64
}

func (f *funcrec) UnmarshalJSONObject(dec *gojay.Decoder, key string) error {
	switch key {
	case "id":
		return dec.Int(&f.id)
	case "nome":
		return dec.String(&f.nome)
	case "sobrenome":
		return dec.String(&f.sobrenome)
	case "salario":
		return dec.Float64(&f.salario)
	case "area":
		return dec.String(&f.area)
	}
	return nil
}

func (f *funcrec) NKeys() int {
	return 0
}

func (a *arearec) UnmarshalJSONObject(dec *gojay.Decoder, key string) error {
	switch key {
	case "codigo":
		return dec.String(&a.codigo)
	case "nome":
		return dec.String(&a.nome)
	}
	return nil
}

func (a *arearec) NKeys() int {
	return 0
}

func (a *listareas) UnmarshalJSONArray(dec *gojay.Decoder) error {
	if err := dec.Object(a.area); err != nil {
		return err
	}
	a.nomearea[a.area.codigo] = a.area.nome
	return nil
}

func (a listareas) NKeys() int {
	return 0
}

func (f *listfuncs) UnmarshalJSONArray(dec *gojay.Decoder) error {
	if err := dec.Object(f.funcionario); err != nil {
		return err
	}

	sfunc := funcrec{}
	sfunc.id = f.funcionario.id
	sfunc.nome = f.funcionario.nome
	sfunc.sobrenome = f.funcionario.sobrenome
	sfunc.salario = f.funcionario.salario
	sfunc.area = f.funcionario.area

	if f.res.empareamin == nil {
		f.res.empareamin = make(map[string][]funcrec)
		f.res.empareamax = make(map[string][]funcrec)
		f.res.emplastnamemax = make(map[string][]funcrec)
		f.res.areaavg = make(map[string]float64)
		f.res.areamin = make(map[string]float64)
		f.res.areamax = make(map[string]float64)
		f.res.countarea = make(map[string]float64)
		f.res.lastnamemax = make(map[string]float64)
		f.res.countlastname = make(map[string]float64)
	}

	f.res.globalavg += f.funcionario.salario
	f.res.contaemp++

	f.res.areaavg[f.funcionario.area] += f.funcionario.salario
	f.res.countarea[f.funcionario.area]++

	if f.funcionario.salario > f.res.globalmax {
		f.res.globalmax = f.funcionario.salario
		f.res.empmax = []funcrec{sfunc}
	} else {
		if f.funcionario.salario == f.res.globalmax {
			f.res.empmax = append(f.res.empmax, sfunc)
		}
	}

	if f.funcionario.salario < f.res.globalmin {
		f.res.globalmin = f.funcionario.salario
		f.res.empmin = []funcrec{sfunc}
	} else {
		if f.funcionario.salario == f.res.globalmin {
			f.res.empmin = append(f.res.empmin, sfunc)
		}
	}

	if _, ok := f.res.areamin[f.funcionario.area]; !ok {
		f.res.areamin[f.funcionario.area] = f.funcionario.salario
	}

	if f.funcionario.salario < f.res.areamin[f.funcionario.area] {
		f.res.areamin[f.funcionario.area] = f.funcionario.salario
		f.res.empareamin[f.funcionario.area] = []funcrec{sfunc}
	} else {
		if f.funcionario.salario == f.res.areamin[f.funcionario.area] {
			f.res.empareamin[f.funcionario.area] = append(f.res.empareamin[f.funcionario.area], sfunc)
		}
	}

	if f.funcionario.salario > f.res.areamax[f.funcionario.area] {
		f.res.areamax[f.funcionario.area] = f.funcionario.salario
		f.res.empareamax[f.funcionario.area] = []funcrec{sfunc}
	} else {
		if f.funcionario.salario == f.res.areamax[f.funcionario.area] {
			f.res.empareamax[f.funcionario.area] = append(f.res.empareamax[f.funcionario.area], sfunc)
		}
	}

	if f.funcionario.salario > f.res.lastnamemax[f.funcionario.sobrenome] {
		f.res.lastnamemax[f.funcionario.sobrenome] = f.funcionario.salario
		f.res.emplastnamemax[f.funcionario.sobrenome] = []funcrec{sfunc}
	} else {
		if f.funcionario.salario == f.res.lastnamemax[f.funcionario.sobrenome] {
			f.res.emplastnamemax[f.funcionario.sobrenome] = append(f.res.emplastnamemax[f.funcionario.sobrenome], sfunc)
		}
	}

	f.res.countlastname[f.funcionario.sobrenome]++
	return nil
}

func (f *listfuncs) NKeys() int {
	return 0
}

func (e *empresa) UnmarshalJSONObject(dec *gojay.Decoder, key string) error {
	switch key {
	case "funcionarios":
		return dec.Array(e.funcionarios)

	case "areas":
		return dec.Array(e.areas)
	}
	return nil
}

func (e *empresa) NKeys() int {
	return 0
}

func (f *listfuncs) printresultados(nomearea map[string]string) {
	leastemployees := math.MaxFloat64
	mostemployees := 0.0

	for k := range f.res.countarea {
		if f.res.countarea[k] < leastemployees {
			leastemployees = f.res.countarea[k]
		}

		if f.res.countarea[k] > mostemployees {
			mostemployees = f.res.countarea[k]
		}
	}

	for _, v := range f.res.empmax {
		fmt.Printf("global_max|%s %s|%.2f\n", v.nome, v.sobrenome, v.salario)
	}
	for _, v := range f.res.empmin {
		fmt.Printf("global_min|%s %s|%.2f\n", v.nome, v.sobrenome, v.salario)
	}

	fmt.Printf("global_avg|%.2f\n", f.res.globalavg/f.res.contaemp)

	for k := range nomearea {
		for _, j := range f.res.empareamax[k] {
			fmt.Printf("area_max|%s|%s %s|%.2f\n", nomearea[k], j.nome, j.sobrenome, j.salario)
		}
		for _, j := range f.res.empareamin[k] {
			fmt.Printf("area_min|%s|%s %s|%.2f\n", nomearea[k], j.nome, j.sobrenome, j.salario)
		}
		if f.res.countarea[k] > 0 {
			fmt.Printf("area_avg|%s|%.2f\n", nomearea[k], f.res.areaavg[k]/f.res.countarea[k])
		}

		if f.res.countarea[k] == leastemployees {
			fmt.Printf("least_employees|%s|%.0f\n", nomearea[k], f.res.countarea[k])
		}

		if f.res.countarea[k] == mostemployees {
			fmt.Printf("most_employees|%s|%.0f\n", nomearea[k], f.res.countarea[k])
		}
	}

	for k := range f.res.lastnamemax {
		if f.res.countlastname[k] > 1 {
			for _, j := range f.res.emplastnamemax[k] {
				fmt.Printf("last_name_max|%s|%s %s|%.2f\n", j.sobrenome, j.nome, j.sobrenome, j.salario)
			}
		}
	}
}

func main() {
	var (
		filename string
	)

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

	dados := &empresa{
		funcionarios: &listfuncs{
			funcionario: &funcrec{},
			res:         resultados{globalmin: math.MaxFloat64},
		},
		areas: &listareas{
			area:     &arearec{},
			nomearea: map[string]string{},
		},
	}

	err = gojay.Unsafe.Unmarshal(r, dados)
	if err != nil {
		log.Fatal(err)
	}
	dados.funcionarios.printresultados(dados.areas.nomearea)
}
