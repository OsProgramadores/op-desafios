package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

func runPrograms(fileName string) error {
	f, err := os.Open(fileName)
	if err != nil {
		return err
	}
	fileScanner := bufio.NewScanner(f)
	fileScanner.Split(bufio.ScanLines)

	line := 0
	for fileScanner.Scan() {
		line++
		// expect line: prog.tur,input
		text := strings.TrimSpace(fileScanner.Text())
		if len(text) == 0 {
			continue
		}

		progAndInput := strings.Split(text, ",")
		if !(len(text) == 0) && len(progAndInput) != 2 {
			return fmt.Errorf("%s: invalid format at line %d: '%s' -> expected prog.tur,input", fileName, line, text)
		}
		prog, input := progAndInput[0], progAndInput[1]
		machine, err := createMachine(prog, input)
		if err != nil {
			return fmt.Errorf("failed to execute %s with %s input: %s", prog, input, err)
		}
		machine.run()

		// output the machine processing
		fmt.Printf("%s,%s,%s\n", prog, input, machine.getMemory())
	}

	return nil
}

type state string

type symbol byte
type memory []symbol

func (m memory) String() string {
	return string(m)
}

type direction byte

type programEntry struct {
	// n new symbol
	n symbol
	// d direction
	d direction
	// s new state to set
	s state
}
type program map[state]map[symbol]programEntry

type turingMachine struct {
	// pos the position of the current machine
	pos int
	// prog the machine program
	prog program
	// state current state
	state state
	// mem memory
	mem memory
	// nMem negative memory for negative indexes
	nMem memory
}

func (m *turingMachine) run() {
	_, hasGlobalState := m.prog["*"]

	for {
		// found program entry
		var e programEntry

		currentSymbol := m.cur()
		// spaces must be lookup as '_' in the entry tree
		if currentSymbol == ' ' {
			currentSymbol = '_'
		}
		debug.Printf("cur: %state:%d\n", currentSymbol, currentSymbol)

		// check for exact entries in global state, since precedence
		var matchGlobalEntry bool
		if hasGlobalState {
			ge, ok := m.prog["*"][currentSymbol]
			if ok {
				matchGlobalEntry = true
				e = ge
			}
		}

		// no global entry found do normal entry logic
		if !matchGlobalEntry {
			// get current entry tree
			et, ok := m.prog[m.state]
			if !ok {
				// halt, no way to continue
				if !hasGlobalState {
					debug.Println("halt at no state found")
					m.error()
					return
				}
				et = m.prog["*"]
			}

			// try to find a matching entry by symbol
			e, ok = et[currentSymbol]
			if !ok {
				// try to find a generic entry symbol
				g, ok := et['*']
				// halt, no way to continue
				if !ok {
					debug.Println("halt at no symbol found")
					m.error()
					return
				}
				e = g
			}
			debug.Printf("entry: %+v\n", e)
		}

		// swap to new symbol
		newSymbol := e.n
		// check if new symbol must be a space
		if newSymbol == '_' {
			newSymbol = ' '
		}
		// no operation
		if newSymbol == '*' {
			newSymbol = currentSymbol
		}
		debug.Printf("changed %state to %state at %d: %s\n", currentSymbol, newSymbol, m.pos, m.getMemory())
		m.updateSymbol(newSymbol)

		// set new state
		newState := e.s
		// halt state detection
		if strings.HasPrefix(string(newState), string(halt)) {
			debug.Printf("halt at '%s' state\n", newState)
			return
		}
		// error state detection
		if strings.HasPrefix(string(newState), string(errState)) {
			debug.Printf("halt at '%s' state\n", newState)
			m.error()
			return
		}
		debug.Printf("state change %s -> %s", m.state, newState)
		m.state = newState

		// walk the needle
		if e.d == left {
			debug.Println("left")
			m.pos -= 1
		} else if e.d == right {
			debug.Println("right")
			m.pos += 1
		}
	}
}

// Reverse reverses a string
func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// cur returns current symbol, negative indexes are supported
func (m *turingMachine) cur() symbol {
	// deal with negative memory
	if m.pos < 0 {
		// real index of negative memory is
		// -1 = 0
		// -2 = 1
		return m.currentSymbol(&m.nMem, (m.pos*-1)-1)
	}
	return m.currentSymbol(&m.mem, m.pos)
}

// currentSymbol returns current symbol, growing mem accordingly
func (m *turingMachine) currentSymbol(mem *memory, i int) symbol {
	if len(*mem)-1 < i {
		*mem = append(*mem, ' ')
		return ' '
	}
	return (*mem)[i]
}

// updateSymbol updates a symbol with negative index support using nMem
func (m *turingMachine) updateSymbol(newSymbol symbol) {
	if m.pos < 0 {
		m.nMem[(m.pos*-1)-1] = newSymbol
	} else {
		m.mem[m.pos] = newSymbol
	}

}

// error sets the machine into error, output is ERR and negative memory is empty
func (m *turingMachine) error() {
	m.nMem = nil
	m.mem = memory("ERR")
}

func (m *turingMachine) getMemory() string {
	return strings.TrimSpace(Reverse(string(m.nMem)) + string(m.mem))
}

const (
	left = direction(iota)
	right
	noDir
)

const initialState = "0"

const halt = state("halt")

const errState = state("error")

func createMachine(progFileName string, input string) (*turingMachine, error) {
	f, err := os.Open(progFileName)
	if err != nil {
		return nil, fmt.Errorf("failed to open %s program file: %s", progFileName, err)
	}
	fileScanner := bufio.NewScanner(f)
	fileScanner.Split(bufio.ScanLines)

	line := 0

	prog := make(program)
	for fileScanner.Scan() {
		line++
		text := strings.TrimSpace(fileScanner.Text())
		// ignore empty lines
		if len(text) == 0 {
			continue
		}

		// ignore comments
		if text[0] == ';' {
			continue
		}

		// sanitize comments like that
		// a b state d e     ; a comment
		text = strings.TrimSpace(strings.Split(text, ";")[0])

		// scan program line and validate it
		tokens := strings.Split(text, " ")
		if len(tokens) != 5 {
			return nil, fmt.Errorf("invalid syntax at line %d, expected 5 tokens, got %d: '%s'", line, len(tokens), text)
		}
		// extract program line as bytes
		d := tokens[3]

		// validate direction
		if d != "l" && d != "r" && d != "*" {
			return nil, fmt.Errorf("invalid direction at line %d: '%s' -> must be one of l,r,*", line, d)
		}

		// everything ok, create the entry
		targetState := state(tokens[0])
		targetSymbol := symbol(toSingleByte(tokens[1]))
		if prog[targetState] == nil {
			prog[targetState] = make(map[symbol]programEntry)
		}
		prog[targetState][targetSymbol] = programEntry{
			n: symbol(toSingleByte(tokens[2])),
			d: parseDirection(d),
			s: state(tokens[4]),
		}
	}

	debug.Printf("created program: %+v\n", prog)

	return &turingMachine{
		pos:   0,
		prog:  prog,
		state: initialState,
		mem:   []symbol(input),
		nMem:  make(memory, 0),
	}, nil
}

// toSingleByte return strings like "a", "v" as their byte values
func toSingleByte(s string) byte {
	if len(s) == 0 {
		return 0
	}

	return []byte(s)[0]
}

func parseDirection(d string) direction {
	var parsedDir direction
	if d == "*" {
		parsedDir = noDir
	}
	if d == "l" {
		parsedDir = left
	}
	if d == "r" {
		parsedDir = right
	}

	return parsedDir
}

var debug *log.Logger
var stderr *log.Logger

func main() {
	// init stderr log
	stderr = log.New(os.Stderr, "", 0)
	if len(os.Args) != 2 {
		stderr.Printf("programs file required, usage: %s [programs file]", os.Args[0])
	}

	// init a debug logger if DEBUG env var is set, else, don't log it
	if strings.ToLower(os.Getenv("DEBUG")) == "true" {
		debug = log.New(os.Stderr, "DEBUG ", log.Ldate|log.Ltime)
	} else {
		debug = log.New(io.Discard, "", 0)
	}

	fileName := os.Args[1]
	err := runPrograms(fileName)
	if err != nil {
		stderr.Fatalf("turing machine error: %v", err)
	}
}
