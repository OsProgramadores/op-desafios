package main

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"log"
	"os"
)

const bufferSize = 64 * 1024

func printReverse(w io.Writer, s []byte, lastLine bool) int {
	lineLen := 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '\n' {
			w.Write(s[i+1 : i+lineLen+1])
			lineLen = 0
		}
		lineLen++
	}
	if lastLine {
		w.Write(s[:lineLen])
	}
	return lineLen
}

func tac(w io.Writer, r io.ReaderAt, fileSize, bufferSize int64) error {
	buffer := make([]byte, bufferSize)
	offset := fileSize

	for {
		if offset -= bufferSize; offset < 0 {
			break
		}
		read, err := r.ReadAt(buffer, offset)
		if err != nil && err != io.EOF {
			return err
		}

		lineLen := int64(printReverse(w, buffer[:read], false))
		if lineLen >= bufferSize {
			return errors.New("line is too long")
		}
		offset += lineLen
	}

	if offset < 0 {
		read, err := r.ReadAt(buffer[:bufferSize+offset], 0)
		if err != nil && err != io.EOF {
			return err
		}
		printReverse(w, buffer[:read], true)
	}
	return nil
}

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("Usage: %s [FILE]", os.Args[0])
		return
	}

	file, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	stat, err := file.Stat()
	if err != nil {
		log.Fatal(err)
	}

	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	if err := tac(writer, file, stat.Size(), bufferSize); err != nil {
		log.Fatal(err)
	}
}
