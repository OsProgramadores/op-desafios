package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"matbm.net/turing-machine/machine"
	"os"
	"strings"
)

var debug *log.Logger
var stderr *log.Logger

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
		if len(progAndInput) != 2 {
			return fmt.Errorf("%s: invalid format at line %d: '%s' -> expected prog.tur,input", fileName, line, text)
		}

		progFileName, input := progAndInput[0], progAndInput[1]
		progFile, err := os.Open(progFileName)
		if err != nil {
			return fmt.Errorf("failed to open %q program file: %s", progFileName, err)
		}
		turMachine, err := machine.New(progFile, input, debug)
		if err != nil {
			return fmt.Errorf("failed to create %q program with %q input: %s", progFileName, input, err)
		}
		_ = progFile.Close()
		turMachine.Run()

		// output the turMachine processing
		fmt.Printf("%s,%s,%s\n", progFileName, input, turMachine.GetMemory())
	}

	return nil
}

func main() {
	// init stderr log
	stderr = log.New(os.Stderr, "", 0)
	if len(os.Args) != 2 {
		stderr.Fatalf("Programs file required, usage: %s [programs file]", os.Args[0])
	}

	debug = log.New(io.Discard, "", 0)
	// init a debug logger if DEBUG env var is set
	if strings.ToLower(os.Getenv("DEBUG")) == "true" {
		debug = log.New(os.Stderr, "DEBUG ", log.Ldate|log.Ltime|log.Lmicroseconds)
	}

	if err := runPrograms(os.Args[1]); err != nil {
		stderr.Fatalf("Turing machine error: %v", err)
	}
}
