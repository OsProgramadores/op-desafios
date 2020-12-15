package funcionarios

import (
	"math"
	"sort"
)

type Funcionarios struct {
	Funcionarios []Funcionario `json:"funcionarios"`

	Areas []struct {
		Codigo string `json:"codigo"`
		Nome   string `json:"nome"`
	} `json:"areas"`
}

func (f *Funcionarios) ObterAreas() map[string]string {
	areas := make(map[string]string)

	for _, area := range f.Areas {
		areas[area.Codigo] = area.Nome
	}

	return areas
}

func (f *Funcionarios) NumeroDeFuncionarios() int {
	return len(f.Funcionarios)
}

func (f *Funcionarios) MediaSalarial() float64 {
	var media float64

	for _, funcionario := range f.Funcionarios {
		media += funcionario.Salario
	}

	return media / float64(len(f.Funcionarios))
}

func (f *Funcionarios) MaiorSalario() *Funcionarios {
	maiorSalario := f.Funcionarios[0]

	for _, funcionario := range f.Funcionarios {
		if funcionario.Salario > maiorSalario.Salario {
			maiorSalario = funcionario
		}
	}

	return extrairFuncionariosComMesmoSalario(maiorSalario, f)
}

func (f *Funcionarios) MenorSalario() *Funcionarios {
	menorSalario := f.Funcionarios[0]

	for _, funcionario := range f.Funcionarios {
		if funcionario.Salario < menorSalario.Salario {
			menorSalario = funcionario
		}
	}

	return extrairFuncionariosComMesmoSalario(menorSalario, f)
}

func (f *Funcionarios) ObterFuncionariosPorArea() map[string]Funcionarios {
	funcionariosPorArea := make(map[string]Funcionarios)

	temp := Funcionarios{Areas: f.Areas}

	for _, funcionario := range f.Funcionarios {
		temp.Funcionarios = append(funcionariosPorArea[funcionario.Area].Funcionarios, funcionario)

		funcionariosPorArea[funcionario.Area] = temp
	}

	return funcionariosPorArea
}

func (f *Funcionarios) FuncionariosPorSobrenome() map[string]Funcionarios {
	funcionarios := make(map[string]Funcionarios)
	porSobrenome := make(map[string]Funcionarios)

	for _, funcionario := range f.Funcionarios {
		funcionarios[funcionario.Sobrenome] = Funcionarios{Funcionarios: append(funcionarios[funcionario.Sobrenome].Funcionarios, funcionario)}
	}

	for k, f := range funcionarios {
		if f.NumeroDeFuncionarios() > 1 {
			porSobrenome[k] = Funcionarios{Funcionarios: append(porSobrenome[k].Funcionarios, f.MaiorSalario().Funcionarios...)}
		}
	}

	return porSobrenome
}

func NumeroDeFuncionariosPorArea(m map[string]Funcionarios) (map[string]int, map[string]int) {
	numeroDeFuncionariosPorArea := make(map[string]int)

	keys := make([]string, 0)

	for k := range m {
		keys = append(keys, k)
	}

	sort.Strings(keys)

	var (
		maiorNumeroDeFuncionarios int
		menorNumeroDeFuncionarios int
	)

	for _, k := range keys {
		f := m[k]

		numeroDeFuncionariosPorArea[k] = f.NumeroDeFuncionarios()

		if numeroDeFuncionariosPorArea[k] < maiorNumeroDeFuncionarios {
			menorNumeroDeFuncionarios = int(math.Min(float64(numeroDeFuncionariosPorArea[k]), float64(maiorNumeroDeFuncionarios)))
		}
		maiorNumeroDeFuncionarios = int(math.Max(float64(numeroDeFuncionariosPorArea[k]), float64(maiorNumeroDeFuncionarios)))

	}

	return extrairAreasComMesmoNumeroDeFuncionarios(maiorNumeroDeFuncionarios, numeroDeFuncionariosPorArea),
		extrairAreasComMesmoNumeroDeFuncionarios(menorNumeroDeFuncionarios, numeroDeFuncionariosPorArea)
}

func extrairFuncionariosComMesmoSalario(n Funcionario, f *Funcionarios) *Funcionarios {
	fn := &Funcionarios{}

	for _, funcionario := range f.Funcionarios {
		if funcionario.Salario == n.Salario {
			fn.Funcionarios = append(fn.Funcionarios, funcionario)
		}
	}
	return fn
}

func extrairAreasComMesmoNumeroDeFuncionarios(n int, m map[string]int) map[string]int {
	nm := make(map[string]int)

	for k, v := range m {
		if n == v {
			nm[k] = v
		}
	}
	return nm
}
