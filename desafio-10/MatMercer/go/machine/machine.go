package machine

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"strings"
)

type state string

type symbol byte
type memory []symbol

type direction byte

type programEntry struct {
	newSym   symbol    // new symbol
	dir      direction // direction
	newState state     // newState new state to set
}
type program map[state]map[symbol]programEntry

type TuringMachine struct {
	pos   int         // the position of the current machine
	prog  program     // the machine program
	state state       // current state
	mem   memory      // memory
	nMem  memory      // negative memory for negative indexes
	debug *log.Logger // logger for debug
}

func (m *TuringMachine) Run() {
	_, hasGlobalState := m.prog["*"]

	for {
		// found program entry
		var e programEntry

		currentSymbol := m.cur()
		// spaces must be lookup as '_' in the entry tree
		if currentSymbol == ' ' {
			currentSymbol = '_'
		}
		m.debug.Printf("cur: %c:%d\n", currentSymbol, currentSymbol)

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
					m.debug.Println("halt at no state found")
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
					m.debug.Println("halt at no symbol found")
					m.error()
					return
				}
				e = g
			}
			m.debug.Printf("entry: %+v\n", e)
		}

		// swap to new symbol
		newSymbol := e.newSym
		// check if new symbol must be a space
		if newSymbol == '_' {
			newSymbol = ' '
		}
		// no operation
		if newSymbol == '*' {
			newSymbol = currentSymbol
		}
		m.debug.Printf("changed %q to %q at %d: %q\n", currentSymbol, newSymbol, m.pos, m.GetMemory())
		m.updateSymbol(newSymbol)

		// set new state
		newState := e.newState
		// halt state detection
		if strings.HasPrefix(string(newState), string(halt)) {
			m.debug.Printf("halt at %q state\n", newState)
			return
		}
		// error state detection
		if strings.HasPrefix(string(newState), string(errState)) {
			m.debug.Printf("halt at %q state\n", newState)
			m.error()
			return
		}
		m.debug.Printf("state change %q -> %q", m.state, newState)
		m.state = newState

		// walk the needle
		if e.dir == left {
			m.debug.Println("left")
			m.pos -= 1
		} else if e.dir == right {
			m.debug.Println("right")
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
func (m *TuringMachine) cur() symbol {
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
func (m *TuringMachine) currentSymbol(mem *memory, i int) symbol {
	if len(*mem)-1 < i {
		*mem = append(*mem, ' ')
		return ' '
	}
	return (*mem)[i]
}

// updateSymbol updates a symbol with negative index support using nMem
func (m *TuringMachine) updateSymbol(newSymbol symbol) {
	if m.pos < 0 {
		m.nMem[(m.pos*-1)-1] = newSymbol
	} else {
		m.mem[m.pos] = newSymbol
	}

}

// error sets the machine into error, output is ERR and negative memory is empty
func (m *TuringMachine) error() {
	m.nMem = nil
	m.mem = memory("ERR")
}

func (m *TuringMachine) GetMemory() string {
	return strings.TrimSpace(Reverse(string(m.nMem)) + string(m.mem))
}

const (
	left = direction(iota)
	right
	noDir
	invalid
)

const initialState = "0"

const halt = state("halt")

const errState = state("error")

// New creates a new turing machine.
func New(progSource io.Reader, input string, debug *log.Logger) (*TuringMachine, error) {
	fileScanner := bufio.NewScanner(progSource)
	fileScanner.Split(bufio.ScanLines)

	line := 0

	prog := program{}
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
			return nil, fmt.Errorf("invalid syntax at line %d, expected 5 tokens, got %d: %q", line, len(tokens), text)
		}
		// extract program line as bytes
		d := tokens[3]

		// everything ok, create the entry
		targetState := state(tokens[0])
		targetSymbol := symbol(toSingleByte(tokens[1]))
		if prog[targetState] == nil {
			prog[targetState] = map[symbol]programEntry{}
		}

		// validate direction
		dir := parseDirection(d)
		if dir == invalid {
			return nil, fmt.Errorf("invalid direction at line %d: %q -> must be one of l,r,*", line, d)
		}
		prog[targetState][targetSymbol] = programEntry{
			newSym:   symbol(toSingleByte(tokens[2])),
			dir:      dir,
			newState: state(tokens[4]),
		}
	}

	debug.Printf("created program: %+v\n", prog)

	return &TuringMachine{
		pos:   0,
		prog:  prog,
		state: initialState,
		mem:   []symbol(input),
		nMem:  memory{},
		debug: debug,
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
	switch d {
	case "*":
		return noDir
	case "l":
		return left
	case "r":
		return right
	}

	return invalid
}
