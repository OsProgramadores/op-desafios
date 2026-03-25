package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"github.com/kyldery/d05/funcionarios"
)

func main() {
	if len(os.Args) < 2 {
		log.Fatalln("Passe o caminho do JSON que será lido")
	}

	data, err := ioutil.ReadFile(os.Args[1])

	if err != nil {
		log.Fatalln(err)
	}

	employees := &funcionarios.Funcionarios{}

	if err = json.Unmarshal(data, employees); err != nil {
		log.Fatalln(err)
	}

	areas := employees.ObterAreas()
	funcionariosPorArea := employees.ObterFuncionariosPorArea()
	maiorNumeroDeFuncionarios, menorNumeroDeFuncionarios := funcionarios.NumeroDeFuncionariosPorArea(funcionariosPorArea)
	funcionariosPorSobrenome := employees.FuncionariosPorSobrenome()

	for _, f := range employees.MaiorSalario().Funcionarios {
		fmt.Printf("global_max|%s|%.2f\n", f.NomeCompleto(), f.Salario)
	}

	for _, f := range employees.MenorSalario().Funcionarios {
		fmt.Printf("global_min|%s|%.2f\n", f.NomeCompleto(), f.Salario)
	}

	fmt.Printf("global_avg|%.2f\n", employees.MediaSalarial())

	for key, f := range funcionariosPorArea {
		for _, maiorSalario := range f.MaiorSalario().Funcionarios {
			fmt.Printf("area_max|%s|%s|%.2f\n", areas[maiorSalario.Area], maiorSalario.NomeCompleto(), maiorSalario.Salario)
		}
		for _, menorSalario := range f.MenorSalario().Funcionarios {
			fmt.Printf("area_min|%s|%s|%.2f\n", areas[menorSalario.Area], menorSalario.NomeCompleto(), menorSalario.Salario)
		}
		fmt.Printf("area_avg|%s|%.2f\n", areas[key], f.MediaSalarial())
	}

	for key, numeroDeFuncionarios := range maiorNumeroDeFuncionarios {
		fmt.Printf("most_employees|%s|%d\n", areas[key], numeroDeFuncionarios)
	}

	for key, numeroDeFuncionarios := range menorNumeroDeFuncionarios {
		fmt.Printf("least_employees|%s|%d\n", areas[key], numeroDeFuncionarios)
	}

	for key, f := range funcionariosPorSobrenome {
		for _, funcionario := range f.MaiorSalario().Funcionarios {
			fmt.Printf("last_name_max|%s|%s|%.2f\n", key, funcionario.NomeCompleto(), funcionario.Salario)
		}
	}
}
