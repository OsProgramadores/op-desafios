// d07 - Prints all lines in a file in reversed order.
//
// This is the solution to a coding challenge in http://osprogramadores.com
// Note: This is not as optimized as it could be.
//
// Marco Paganini <paganini@paganini.net>
package main

import (
	"bufio"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"runtime/pprof"
	"strings"
)

const (
	// Read chunk size in bytes. This must be larger than the largest text
	// line in the file, or the program will fail.
	chunkSize = 256 * 1024
)

func main() {
	var optCPUProfile string

	log.SetFlags(0)

	// Command line processing.
	flag.StringVar(&optCPUProfile, "cpuprofile", "", "write cpu profile to file")
	flag.Parse()
	if len(flag.Args()) != 1 {
		log.Fatalln("Use: d07 arquivo")
	}
	fname := flag.Args()[0]

	// Profiling.
	if optCPUProfile != "" {
		f, err := os.Create(optCPUProfile)
		if err != nil {
			log.Fatal(err)
		}
		pprof.StartCPUProfile(f)
		defer pprof.StopCPUProfile()
	}

	// Retrieve file size.
	fi, err := os.Stat(fname)
	if err != nil {
		log.Fatal(err)
	}
	size := int64(fi.Size())

	f, err := os.OpenFile(fname, os.O_RDONLY, 0)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	// Use bufio.NewWriter instead of fmt.Printf for performance reasons.
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	if err := reverse(f, out, size); err != nil {
		log.Fatal(err)
	}
}

// reverse reads data from r and writes text lines to w in reverse order.
func reverse(r *os.File, w io.Writer, size int64) error {
	var (
		offset    int64
		bufsize   int64
		buf       []byte
		printlast bool
	)

	bufsize = min(chunkSize, size)
	offset = max(int64(size-chunkSize), 0)

	for {
		// Reallocate if size doesn't match.
		if int64(len(buf)) != bufsize {
			buf = make([]byte, bufsize)
		}
		if _, err := r.ReadAt(buf, offset); err != nil && err != io.EOF {
			return err
		}

		lines := strings.Split(string(buf), "\n")
		if len(lines) < 2 {
			return fmt.Errorf("Reading chunk size too small (%d bytes)", chunkSize)
		}

		revprint(w, lines, (offset == 0), printlast)
		if offset == 0 {
			break
		}

		printlast = true

		// Move the offset back enough to make the current first line to be
		// the last on the next iteration.
		offset = offset - chunkSize + int64(len(lines[0]))
		if offset < 0 {
			bufsize = chunkSize + offset
			offset = 0
		}
	}
	return nil
}

// revprint splits the byte slice buffer into lines and prints them backwards.
//
// This function expects the input slice to have been taken from a "window" of
// bytes from a file. We always assume the first line in the slice to be
// incomplete and don't print it unless printfirst is set to true. The caller
// will set printfirst to true once it is sure the first line is complete
// (usually then the file read offset == 0)
//
// If the last line is blank and printlast is false, don't print it or we'll
// end up with an extra line at the beginning of the reversed output for files
// ending in a newline (common case). Please note that tac behaves differently
// in such situations.
func revprint(w io.Writer, lines []string, printfirst, printlast bool) {
	lastline := lines[len(lines)-1]

	if printlast && lastline != "" {
		fmt.Fprintln(w, lastline)
	}
	for i := len(lines) - 2; i > 0; i-- {
		fmt.Fprintln(w, lines[i])
	}
	if printfirst {
		fmt.Fprintln(w, lines[0])
	}
}

// min returns the smallest of two int64 numbers.
func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

// max returns the largest of two int64 numbers.
func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}
