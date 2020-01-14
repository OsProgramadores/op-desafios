package funcionarios

import (
	"fmt"
)

type Funcionario struct {
	ID        int     `json:"id"`
	Nome      string  `json:"nome"`
	Sobrenome string  `json:"sobrenome"`
	Salario   float64 `json:"salario"`
	Area      string  `json:"area"`
}

func (f *Funcionario) NomeCompleto() string {
	return fmt.Sprintf("%s %s", f.Nome, f.Sobrenome)
}
