// turing.go - Small turing machine simulator.
//
// Idea taken from the excellent "Turing Machine Simulator" by Anthony Morphett
// at http://morphett.info/turing/.
//
// Jan/2019 by Marco Paganini <paganini@paganini.net>

package main

import (
	"bufio"
	"bytes"
	"errors"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

// rule holds one rule to the turing machine.
type rule struct {
	state     string
	symbol    byte
	newSymbol byte
	direction string
	newState  string
}

// dataitem holds one item from the datafile.
type dataitem struct {
	rulefile string
	value    []byte
}

func main() {
	log.SetFlags(0)
	flag.Parse()

	args := flag.Args()
	if len(args) < 1 {
		log.Fatal("Missing datafile")
	}

	// Open and parse config file.
	dfile, err := os.Open(args[0])
	if err != nil {
		log.Fatal(err)
	}
	dfitems, err := loadDatafile(dfile)
	if err != nil {
		log.Fatal(err)
	}
	dfile.Close()

	// Execute once for each test. This is not optimized since we
	// instantiate each test multiple times.
	for _, v := range dfitems {
		r, err := os.Open(v.rulefile)
		if err != nil {
			log.Fatal(err)
		}
		program, err := loadProgram(r)
		if err != nil {
			log.Fatal(err)
		}
		r.Close()

		tape, err := runProgram(program, v.value)
		if err != nil {
			tape = []byte("ERR")
		}
		fmt.Printf("%s,%s,%s\n", v.rulefile, v.value, string(bytes.Trim(tape, " ")))
	}
}

// loadDatafile loads a datafile and returns a slice of dataitem.
func loadDatafile(df io.Reader) ([]dataitem, error) {
	var ret []dataitem

	scanner := bufio.NewScanner(df)
	for scanner.Scan() {
		line := strings.Trim(scanner.Text(), " \t\n\r")
		fields := strings.Split(line, ",")

		if len(fields) != 2 {
			return nil, fmt.Errorf("line does not have exactly two fields: %s", line)
		}
		ret = append(ret, dataitem{
			rulefile: fields[0],
			value:    []byte(fields[1]),
		})
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}
	return ret, nil
}

// loadProgram loads the program from a disk file, with basic checks.
func loadProgram(reader io.Reader) ([]rule, error) {
	var (
		linenum int
		program []rule
	)

	scanner := bufio.NewScanner(reader)
	for scanner.Scan() {
		// Ignore everything to the right of a ";" (inline comments)
		line := strings.Split(scanner.Text(), ";")[0]
		line = strings.Trim(line, " \t\n\r")
		linenum++

		// Ignore comments and blank lines.
		if len(line) == 0 {
			continue
		}

		ins, err := parseLine(line)
		if err != nil {
			return nil, fmt.Errorf("error(%d): %q: %v", linenum, line, err)
		}
		program = append(program, ins)
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}
	return program, nil
}

// parseLine parses a program line, substituting '_' for space where needed.
func parseLine(line string) (rule, error) {
	tok := strings.Fields(line)
	if len(tok) != 5 {
		return rule{}, errors.New("input line must have exactly 5 fields")
	}
	// Replace underscores by spaces to make comparison easier later.
	if tok[1] == "_" {
		tok[1] = " "
	}
	if tok[2] == "_" {
		tok[2] = " "
	}

	// Basic sanity checking on direction (r/l/* only).
	if tok[3] != "l" && tok[3] != "r" && tok[3] != "*" {
		return rule{}, errors.New("direction must be l, r, or *")
	}

	return rule{
		state:     tok[0],
		symbol:    tok[1][0],
		newSymbol: tok[2][0],
		direction: tok[3],
		newState:  tok[4],
	}, nil
}

// runProgram executes the program, reading the "tape" input from the passed
// slice of byte.  Returns the program output as (an untrimmed) slice of bytes.
func runProgram(program []rule, tapeInput []byte) ([]byte, error) {
	tape := make([]byte, len(tapeInput))
	copy(tape, tapeInput)

	state := "0"
	pos := 0
	tape = bytes.Trim(tape, " \t\r\n")

	for {
		ins, err := findRule(program, state, tape[pos])
		if err != nil {
			return nil, err
		}
		// Do not set new symbol if set to '*'.
		if ins.newSymbol != '*' {
			tape[pos] = ins.newSymbol
		}
		// Left.
		if ins.direction == "l" {
			pos--
			if pos < 0 {
				pos = 0
				tape = append([]byte{' '}, tape...)
			}
		}
		// Right
		if ins.direction == "r" {
			pos++
			if pos > len(tape)-1 {
				tape = append(tape, ' ')
			}
		}
		// Change state.
		state = ins.newState
		if strings.HasPrefix(ins.newState, "halt") {
			break
		}
	}
	return tape, nil
}

// findRule returns the program rule for a particular state and symbol.  More
// generic matches on symbol take precedence over less generic ones (when using
// "*").  If two generic matches exist, the first one takes precedence.
// Returns error if it can't find a match for the desired state and symbol.
func findRule(program []rule, state string, symbol byte) (rule, error) {
	var wild rule

	for _, ins := range program {
		switch {
		// Ignore this rule if the rule state is not '*' and it does not match
		// out current state.
		case ins.state != "*" && ins.state != state:
			continue

		// If the rule symbol is '*' and we haven't found a wildcard yet, set
		// our possible wildcard match.
		case ins.symbol == '*' && wild == (rule{}):
			wild = ins
			continue

		// Ignore symbols that do not match.
		case ins.symbol != symbol:
			continue

		// If the rule state == "*", we found a wildcard. In this case, we set
		// our possible wildcard match if another wildcard hasn't been found
		// yet. Continue to see if we can find a more specific rule. Otherwise,
		// just return the current value since we have a specific case.
		case ins.state == "*" && wild == (rule{}):
			wild = ins
			continue
		}

		// If we got here, we have a specific match. Return it immediately.
		return ins, nil
	}

	// No specific match found. Return the wildcard match, if we have one.
	if wild != (rule{}) {
		//fmt.Printf("Got symbol. Returning wildcard %s (%c) (%c) %s %s\n", wild.state, wild.symbol, wild.newSymbol, wild.direction, wild.state)
		return wild, nil
	}

	return rule{}, fmt.Errorf("can't find match for state %q, symbol %q", state, symbol)
}
