package main

import (
	"bytes"
	"fmt"
	"io"
	"os"
)

const bufSize = int64(32)

func check(e error) {
	if e != nil {
		errAndExit(fmt.Sprintf("tac error: %v", e))
	}
}

func errAndExit(msg string) {
	os.Stderr.WriteString(msg + "\n")
	os.Exit(1)
}

func main() {
	args := os.Args[1:]

	if len(args) != 1 {
		errAndExit("usage: tac [file]")
	}

	fileName := args[0]

	f, err := os.Open(fileName)
	check(err)
	defer f.Close()
	fi, err := f.Stat()
	check(err)

	b := make([]byte, bufSize)
	end := fi.Size()
	maxRead := bufSize
	start := end
	lineAcc := bytes.NewBuffer([]byte{})
	for start != 0 {
		start -= bufSize
		if start < 0 {
			// prevent over reading if result is less than buf size
			maxRead += start
			start = 0
		}

		_, err = f.Seek(start, io.SeekStart)
		check(err)
		_, err = f.Read(b[:maxRead])
		check(err)

		// search until backwards \n and prints it
		lastEnd := maxRead
		for i := maxRead - 1; i >= 0; i-- {
			if b[i] == '\n' {
				// write everything but '\n', since b[i] == '\n'
				out(b[i+1 : lastEnd])
				// need to write accumulated value
				out(lineAcc.Bytes())
				lineAcc.Reset()
				// +1 here makes '\n' be printed in next iteration
				lastEnd = i + 1
			}

			if i == 0 {
				newAcc := bytes.NewBuffer([]byte{})
				_, err = newAcc.Write(b[i:lastEnd])
				check(err)
				_, err = newAcc.Write(lineAcc.Bytes())
				check(err)
				lineAcc.Reset()
				lineAcc = newAcc
			}
		}
	}
	// prints last chunk of data
	out(lineAcc.Bytes())
}

// out outputs to os.Stdout checking for errors
func out(b []byte) {
	// fmt.Println is unbuffered https://github.com/golang/go/issues/36619
	_, err := os.Stdout.Write(b)
	check(err)
}
