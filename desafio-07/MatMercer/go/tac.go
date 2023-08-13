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

// min standard math.Min supports only float64
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

func tac(fileName string) error {
	f, err := os.Open(fileName)
	if err != nil {
		return err
	}
	fi, err := f.Stat()
	if err != nil {
		return err
	}

	// buffers stdout by 128kb
	stdout = bufio.NewWriterSize(os.Stdout, 128<<(10))

	fileSize := fi.Size()
	bufSize := min(fileSize, maxBufSize)
	readBuf := make([]byte, bufSize)
	maxRead := bufSize
	start := fileSize
	lineAcc := bytes.NewBuffer([]byte{})
	r := &ReverseReader{f, fileSize}
	for start != 0 {
		start -= bufSize
		if start < 0 {
			// prevent over reading if result is less than buf size
			maxRead += start
			start = 0
		}

		_, err = r.Read(readBuf[:maxRead])
		if err != nil {
			return err
		}

		// search until backwards \n and prints it
		lastEnd := maxRead
		for i := maxRead - 1; i >= 0; i-- {
			if readBuf[i] == '\n' {
				// write everything but '\n', since readBuf[i] == '\n'
				_, err = stdout.Write(readBuf[i+1 : lastEnd])
				if err != nil {
					return err
				}
				// writes accumulated value
				_, err = stdout.Write(lineAcc.Bytes())
				if err != nil {
					return err
				}
				// reset the accumulator to receive next line
				lineAcc.Reset()
				// makes '\n' be printed in next iteration
				lastEnd = i + 1
			}

			// on last iteration, create a new accumulator with [max-read][current-accumulator]
			if i == 0 {
				newAcc := bytes.NewBuffer(nil)
				_, err = newAcc.Write(readBuf[i:lastEnd])
				if err != nil {
					return err
				}
				_, err = newAcc.Write(lineAcc.Bytes())
				if err != nil {
					return err
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
		return err
	}

	err = stdout.Flush()
	if err != nil {
		return err
	}

	return nil
}

func main() {
	logger := log.New(os.Stderr, "", 0)
	if len(os.Args) != 2 {
		logger.Fatalln("usage: tac [file]")
	}

	fileName := os.Args[1]
	err := tac(fileName)
	if err != nil {
		logger.Fatalf("tac error: %v", err)
	}
}
