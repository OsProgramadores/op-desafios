package main

import (
	"bufio"
	"bytes"
	"io"
	"log"
	"os"
)

// in MB size, currently the program uses a max of 2*bufSize iff file size > bufSize
const maxBufSize = int64(250 << (10 * 2))

var stdout *bufio.Writer

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

func main() {
	if len(os.Args) != 2 {
		log.Fatalln("usage: tac [file]")
	}

	fileName := os.Args[1]
	f, err := os.Open(fileName)
	if err != nil {
		log.Fatalf("tac error: %v", err)
	}
	fi, err := f.Stat()
	if err != nil {
		log.Fatalf("tac error: %v", err)
	}

	// buffers stdout by 128kb
	stdout = bufio.NewWriterSize(os.Stdout, 128<<(10))

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
		if err != nil {
			log.Fatalf("tac error: %v", err)
		}

		// search until backwards \n and prints it
		lastEnd := maxRead
		for i := maxRead - 1; i >= 0; i-- {
			if b[i] == '\n' {
				// write everything but '\n', since b[i] == '\n'
				_, err = stdout.Write(b[i+1 : lastEnd])
				if err != nil {
					log.Fatalf("tac error: %v", err)
				}
				// writes accumulated value
				_, err = stdout.Write(lineAcc.Bytes())
				if err != nil {
					log.Fatalf("tac error: %v", err)
				}
				// reset the accumulator to receive next line
				lineAcc.Reset()
				// makes '\n' be printed in next iteration
				lastEnd = i + 1
			}

			// on last iteration, create a new accumulator with [max-read][current-accumulator]
			if i == 0 {
				newAcc := bytes.NewBuffer(nil)
				_, err = newAcc.Write(b[i:lastEnd])
				if err != nil {
					log.Fatalf("tac error: %v", err)
				}
				_, err = newAcc.Write(lineAcc.Bytes())
				if err != nil {
					log.Fatalf("tac error: %v", err)
				}
				lineAcc = newAcc
			}
		}
	}
	// closes the file
	_ = f.Close()

	// prints last chunk of data
	// fmt.Println is unbuffered https://github.com/golang/go/issues/36619
	_, err = stdout.Write(lineAcc.Bytes())
	if err != nil {
		log.Fatalf("tac error: %v", err)
	}

	err = stdout.Flush()
	if err != nil {
		log.Fatalf("tac error: %v", err)
	}
}
