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
		if !(len(text) == 0) && len(progAndInput) != 2 {
			return fmt.Errorf("%s: invalid format at line %d: '%s' -> expected prog.tur,input", fileName, line, text)
		}
		prog, input := progAndInput[0], progAndInput[1]
		turMarchine, err := machine.New(prog, input, debug)
		if err != nil {
			return fmt.Errorf("failed to execute %s with %s input: %s", prog, input, err)
		}
		turMarchine.Run()

		// output the turMarchine processing
		fmt.Printf("%s,%s,%s\n", prog, input, turMarchine.GetMemory())
	}

	return nil
}

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
