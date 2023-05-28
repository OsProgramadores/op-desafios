package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"os"
)

func main() {
	tac()
}

// in MB size, currently the program uses a max of 2*bufSize iff file size > bufSize
const maxBufSize = int64(250 << (10 * 2))

var stdout *bufio.Writer

func check(e error) {
	if e != nil {
		errAndExit(fmt.Sprintf("tac error: %v", e))
	}
}

func errAndExit(msg string) {
	_, _ = os.Stderr.WriteString(msg + "\n")
	os.Exit(1)
}

func tac() {
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

	// buffers stdout by 128kb
	stdout = bufio.NewWriterSize(os.Stdout, 128<<(10))
	defer stdout.Flush()

	fs := fi.Size()
	bufSize := min(fs, maxBufSize)
	b := make([]byte, bufSize)
	maxRead := bufSize
	start := fs
	lineAcc := bytes.NewBuffer([]byte{})
	r := NewReverseReader(f, fs)
	for start != 0 {
		start -= bufSize
		if start < 0 {
			// prevent over reading if result is less than buf size
			maxRead += start
			start = 0
		}

		_, err = r.Read(b[:maxRead])
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
				newAcc := bytes.NewBuffer(nil)
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
	_, err := stdout.Write(b)
	check(err)
}

func min(x int64, y int64) int64 {
	if x > y {
		return y
	}
	return x
}

type ReverseReader struct {
	f      *os.File
	offset int64
}

func NewReverseReader(f *os.File, size int64) *ReverseReader {
	return &ReverseReader{
		f,
		size,
	}
}

func (r *ReverseReader) Read(b []byte) (n int, err error) {
	r.offset -= int64(len(b))
	_, err = r.f.Seek(r.offset, io.SeekStart)
	if err != nil {
		return 0, err
	}
	read, err := r.f.Read(b)
	if err != nil {
		return 0, err
	}
	return read, nil
}
