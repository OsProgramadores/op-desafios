package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"sort"
)

// Funcionarios : agregação de estrutura
type Funcionarios struct {
	Funcionarios []Funcionario `json:"funcionarios"`
}

// Funcionario : estrutura de pessoal
type Funcionario struct {
	ID        int     `json:"id"`
	Nome      string  `json:"nome"`
	Sobrenome string  `json:"sobrenome"`
	Salario   float64 `json:"salario"`
	Area      string  `json:"area"`
}

// Areas : grupo de areas
type Areas struct {
	Areas []Area `json:"areas"`
}

// Area : descrição de cada área
type Area struct {
	Codigo string `json:"codigo"`
	Nome   string `json:"nome"`
}

func usage() {
	fmt.Println("Use:", os.Args[0], " <file json>")
}

func readJSONFuncionarios(filename string) Funcionarios {
	//fmt.Println("Json file:", filename)
	jsonFile, err := os.Open(filename)
	defer jsonFile.Close()
	if err != nil {
		log.Fatal("Failed to read file: ", filename)
	}

	byteValue, err := ioutil.ReadAll(jsonFile)
	if err != nil {
		log.Fatal("Failed to read file: ", filename)
	}

	var funcionarios Funcionarios
	json.Unmarshal(byteValue, &funcionarios)
	return funcionarios
}

func readJSONAreas(filename string) Areas {
	//fmt.Println("Json file:", filename)
	jsonFile, err := os.Open(filename)
	defer jsonFile.Close()
	if err != nil {
		log.Fatal("Failed to read file: ", filename)
	}

	byteValue, err := ioutil.ReadAll(jsonFile)
	if err != nil {
		log.Fatal("Failed to read file: ", filename)
	}

	var areas Areas
	json.Unmarshal(byteValue, &areas)
	return areas
}

func printOut(funcionarios Funcionarios) {
	var totalSalary float64
	numberEmployees := len(funcionarios.Funcionarios)
	for i := 0; i < numberEmployees; i++ {
		fmt.Println("User ID: ", funcionarios.Funcionarios[i].ID)
		fmt.Println("User Nome: " + funcionarios.Funcionarios[i].Nome)
		fmt.Println("User Sobrenome: " + funcionarios.Funcionarios[i].Sobrenome)
		fmt.Println("User Salario: ", funcionarios.Funcionarios[i].Salario)
		fmt.Println("User Area: " + funcionarios.Funcionarios[i].Area)
		fmt.Println()
		totalSalary += funcionarios.Funcionarios[i].Salario
	}
	fmt.Println("Total de salários:", totalSalary)
	fmt.Println("Average salary:", totalSalary/float64(numberEmployees))
}

type funcMapping struct {
	nome    string
	salario float64
	area    string
}

func getAreaMap(areas Areas) map[string]string {
	areasMap := make(map[string]string)
	for i := 0; i < len(areas.Areas); i++ {
		key := areas.Areas[i].Codigo
		value := areas.Areas[i].Nome
		areasMap[key] = value
	}
	return areasMap
}

func getHighestSalaries(funcionarios []Funcionario) []int {
	var highestSalary float64
	var highestPersons []int
	for i := 0; i < len(funcionarios); i++ {
		salary := funcionarios[i].Salario
		if salary > highestSalary {
			highestSalary = salary
			highestPersons = make([]int, 1)
			highestPersons[0] = i
		} else if salary == highestSalary {
			highestPersons = append(highestPersons, i)
		}
	}
	return highestPersons
}

func getLowestSalaries(funcionarios []Funcionario) []int {
	var lowestSalary float64
	var lowestPersons []int

	lowestSalary += 999999
	for i := 0; i < len(funcionarios); i++ {
		salary := funcionarios[i].Salario
		if salary < lowestSalary {
			lowestSalary = salary
			lowestPersons = make([]int, 1)
			lowestPersons[0] = i
		} else if salary == lowestSalary {
			lowestPersons = append(lowestPersons, i)
		}
	}
	return lowestPersons
}

func getAverageSalary(funcionarios []Funcionario) float64 {
	var totalSalary float64
	numberOfEmployees := len(funcionarios)
	for i := 0; i < numberOfEmployees; i++ {
		salary := funcionarios[i].Salario
		totalSalary += salary
	}
	return totalSalary / float64(numberOfEmployees)
}

func printOut1(funcionarios []Funcionario) {
	/*
	  1. Quem mais recebe e quem menos recebe na empresa e a média salarial da empresa.
	  global_max|<Nome Completo>|<Salário>
	  global_min|<nome completo>|<salário>
	  global_avg|<média salarial>
	*/
	globalMax := getHighestSalaries(funcionarios)
	for _, i := range globalMax {
		fullName := fmt.Sprintf("%s %s", funcionarios[i].Nome, funcionarios[i].Sobrenome)
		salary := funcionarios[i].Salario
		fmt.Printf("global_max|%s|%02.2f\n", fullName, salary)
	}

	globalMin := getLowestSalaries(funcionarios)
	for _, i := range globalMin {
		fullName := fmt.Sprintf("%s %s", funcionarios[i].Nome, funcionarios[i].Sobrenome)
		salary := funcionarios[i].Salario
		fmt.Printf("global_min|%s|%02.2f\n", fullName, salary)
	}
	fmt.Printf("global_avg|%02.2f\n", getAverageSalary(funcionarios))
}

func printOut2(funcionarios []Funcionario, areasMap map[string]string) {
	/*
	  2. Quem mais recebe e quem menos recebe em cada área e a média salarial em cada área.
	  area_max|<nome da área>|<nome completo>|<salário máximo>
	  area_min|<nome da área>|<nome completo>|<salário>
	  area_avg|<nome da área>|<salário médio>
	*/
	areaKeys := make([]string, 0, len(areasMap))
	for key := range areasMap {
		areaKeys = append(areaKeys, key)
	}
	sort.Strings(areaKeys)
	for _, area := range areaKeys {
		//fmt.Println(area)
		var areaEmployees []Funcionario
		for i := 0; i < len(funcionarios); i++ {
			currentArea := funcionarios[i].Area
			if currentArea == area {
				areaEmployees = append(areaEmployees, funcionarios[i])
			}
		}

		areaName := areasMap[area]

		areaMax := getHighestSalaries(areaEmployees)
		for _, i := range areaMax {
			fullName := fmt.Sprintf("%s %s", areaEmployees[i].Nome, areaEmployees[i].Sobrenome)
			salary := areaEmployees[i].Salario
			fmt.Printf("area_max|%s|%s|%02.2f\n", areaName, fullName, salary)
		}

		areaMin := getLowestSalaries(areaEmployees)
		for _, i := range areaMin {
			fullName := fmt.Sprintf("%s %s", areaEmployees[i].Nome, areaEmployees[i].Sobrenome)
			salary := areaEmployees[i].Salario
			fmt.Printf("area_min|%s|%s|%02.2f\n", areaName, fullName, salary)
		}

		areaAVG := getAverageSalary(areaEmployees)
		fmt.Printf("area_avg|%s|%02.2f\n", areaName, areaAVG)
	}
}

func printOut3(funcionarios []Funcionario, areasMap map[string]string) {
	/*
	  Área(s) com o maior e menor número de funcionários
	  most_employees|<nome da área>|<número de funcionários>
	  least_employees|<nome da área>|<número de funcionários>
	*/
	counter := make(map[string]int)
	for i := 0; i < len(funcionarios); i++ {
		area := funcionarios[i].Area
		counter[area]++
	}
	highest := 0
	lowest := 9999
	highAreas := make([]string, 1)
	lowAreas := make([]string, 1)
	for area := range counter {
		count := counter[area]
		if count > highest {
			highest = count
			highAreas = make([]string, 1)
			highAreas[0] = area
		} else if count == highest {
			highAreas = append(highAreas, area)
		}
		if count < lowest {
			lowest = count
			lowAreas = make([]string, 1)
			lowAreas[0] = area
		} else if count == lowest {
			lowAreas = append(lowAreas, area)
		}
	}
	for _, area := range highAreas {
		areaName := areasMap[area]
		count := counter[area]
		fmt.Printf("most_employees|%s|%d\n", areaName, count)
	}
	for _, area := range lowAreas {
		areaName := areasMap[area]
		count := counter[area]
		fmt.Printf("least_employees|%s|%d\n", areaName, count)
	}
}

func printOut4(funcionarios []Funcionario) {
	/*
	   4. Maiores salários para funcionários com o mesmo sobrenome
	   last_name_max|<sobrenome do funcionário>|<nome completo>|<salário>
	*/
	bySurname := make(map[string][]int)
	for i := 0; i < len(funcionarios); i++ {
		surname := funcionarios[i].Sobrenome
		bySurname[surname] = append(bySurname[surname], i)
	}

	for surname := range bySurname {
		if len(bySurname[surname]) < 2 {
			continue
		}
		var employeeSameSurname []Funcionario
		for _, ID := range bySurname[surname] {
			employeeSameSurname = append(employeeSameSurname, funcionarios[ID])
		}
		maxID := getHighestSalaries(employeeSameSurname)
		for _, ID := range maxID {
			fullName := fmt.Sprintf("%s %s", employeeSameSurname[ID].Nome, employeeSameSurname[ID].Sobrenome)
			salary := employeeSameSurname[ID].Salario
			fmt.Printf("last_name_max|%s|%s|%02.2f\n", surname, fullName, salary)
		}
	}
}

func main() {
	if len(os.Args) != 2 {
		usage()
		os.Exit(1)
	}
	filename := os.Args[1]

	funcionarios := readJSONFuncionarios(filename)
	areas := readJSONAreas(filename)
	areasMap := getAreaMap(areas)
	//getFuncMap(funcionarios)

	//printOut(funcionarios)
	printOut1(funcionarios.Funcionarios)
	printOut2(funcionarios.Funcionarios, areasMap)
	printOut3(funcionarios.Funcionarios, areasMap)
	printOut4(funcionarios.Funcionarios)
}
