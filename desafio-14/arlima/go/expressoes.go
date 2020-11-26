// Solução desafio 14
// Adriano Roberto de Lima
// Referências: https://en.wikipedia.org/wiki/Shunting-yard_algorithm

package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

type token struct {
	op       rune
	value    float64
	nodeType string
}

type stack struct {
	tokens []token
}

func (s *stack) push(t token) {
	s.tokens = append(s.tokens, t)
}

func (s *stack) pop() token {
	el := s.tokens[len(s.tokens)-1]
	s.tokens = s.tokens[:len(s.tokens)-1]
	return el
}

func (s *stack) read() token {
	el := s.tokens[len(s.tokens)-1]
	return el
}

func (s *stack) len() int {
	return len(s.tokens)
}

func (s stack) display() {
	for _, v := range s.tokens {
		if v.nodeType == "number" {
			fmt.Printf("%0.2f ", v.value)
		} else {
			fmt.Printf("%c ", v.op)
		}
	}
	fmt.Printf("\n")
}

func processStr(str string) []token {
	el := []token{}
	p := 0
	num := ""
	for p < len(str) {
		c := str[p]
		switch c {
		case '+', '-', '/', '*', '^', '(', ')', ' ':
			if len(num) > 0 {
				value, _ := strconv.ParseFloat(num, 64)
				el = append(el, token{0, value, "number"})
				num = ""
			}
			if c != ' ' {
				el = append(el, token{rune(c), 0, "operator"})
			}
		case '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.':
			num = num + string(c)
		}
		p++
	}
	if len(num) > 0 {
		value, _ := strconv.ParseFloat(num, 64)
		el = append(el, token{0, value, "number"})
		num = ""
	}
	return el
}

func parse(str string) (stack, error) {
	output := stack{}
	operator := stack{}
	precedence := map[rune]int{'^': 4, '*': 3, '/': 3, '+': 2, '-': 2}
	left := map[rune]bool{'^': false, '*': true, '/': true, '+': true, '-': true}
	el := processStr(str)
	for _, v := range el {
		if v.nodeType == "number" {
			output.push(v)
		} else if v.op != '(' && v.op != ')' {
			for operator.len() > 0 && (precedence[operator.read().op] > precedence[v.op] || (precedence[operator.read().op] == precedence[v.op] && left[v.op] == true)) && operator.read().op != '(' {
				el := operator.pop()
				output.push(el)
			}
			operator.push(v)
		} else if v.op == '(' {
			operator.push(v)
		} else if v.op == ')' {
			for {
				if operator.len() > 0 {
					if operator.read().op != '(' {
						el := operator.pop()
						output.push(el)
					} else {
						break
					}
				} else {
					return output, fmt.Errorf("ERR SYNTAX")
				}
			}
			if operator.read().op == '(' {
				operator.pop()
			}
		}
	}

	for operator.len() > 0 {
		el := operator.pop()
		if el.op == ')' || el.op == '(' {
			return output, fmt.Errorf("ERR SYNTAX")
		}
		output.push(el)
	}
	return output, nil
}

func solve(rpn stack) (float64, error) {
	solution := stack{}
	for _, el := range rpn.tokens {
		if el.nodeType == "number" {
			solution.push(el)
		} else {
			if solution.len() < 2 {
				return 0, fmt.Errorf("ERR SYNTAX")
			}
			b := solution.pop().value
			a := solution.pop().value
			switch el.op {
			case '+':
				solution.push(token{0, a + b, "number"})
			case '-':
				solution.push(token{0, a - b, "number"})
			case '/':
				if b == 0 {
					return 0, fmt.Errorf("ERR DIVBYZERO")
				}
				solution.push(token{0, a / b, "number"})
			case '*':
				solution.push(token{0, a * b, "number"})
			case '^':
				solution.push(token{0, math.Pow(float64(a), float64(b)), "number"})
			}
		}
	}
	return solution.read().value, nil
}

func main() {
	log.SetFlags(0)
	flag.Parse()

	if len(flag.Args()) != 1 {
		log.Fatalln("Use: desafio14 <arquivo>")
	}

	file, err := os.Open(flag.Args()[0])
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		formula := scanner.Text()
		rpn, err := parse(formula)
		if err != nil {
			fmt.Println(err)
		} else {
			res, err := solve(rpn)
			if err != nil {
				fmt.Println(err)
			} else {
				fmt.Println(res)
			}
		}
	}
}
