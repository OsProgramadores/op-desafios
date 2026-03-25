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
)

const (
	// Read chunk size in bytes. This must be larger than the largest text
	// line in the file, or the program will fail.
	chunkSize = 64 * 1024

	// Output buffer size (in bytes).
	writeBufSize = 16 * 1024
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
	size := fi.Size()

	f, err := os.OpenFile(fname, os.O_RDONLY, 0)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	// Use bufio.NewWriter instead of fmt.Printf for performance reasons.
	out := bufio.NewWriterSize(os.Stdout, writeBufSize)
	defer out.Flush()

	if err := reverse(f, out, size); err != nil {
		log.Fatal(err)
	}
}

// reverse reads data from r and writes text lines to w in reverse order.
func reverse(r io.ReaderAt, w io.Writer, size int64) error {
	var (
		offset         int64
		bufsize        int64
		buf            []byte
		forcePrintLast bool
	)

	bufsize = min(chunkSize, size)
	offset = max(size-chunkSize, 0)

	for {
		// Reallocate if size doesn't match.
		if int64(len(buf)) != bufsize {
			buf = make([]byte, bufsize)
		}
		if _, err := r.ReadAt(buf, offset); err != nil && err != io.EOF {
			return err
		}

		count := int64(revprint(w, buf, (offset == 0), forcePrintLast))
		if offset == 0 {
			break
		}
		if count == chunkSize {
			return fmt.Errorf("chunk size is too small: %v", chunkSize)
		}

		forcePrintLast = true

		// Move the offset back enough to make the current first line to be
		// the last on the next iteration.
		offset = offset - chunkSize + count
		if offset < 0 {
			bufsize = chunkSize + offset
			offset = 0
		}
	}
	return nil
}

// revprint prints the bytes slice backwards, using \n as line separators.
//
// This function expects the bytes slice to be a "window" of bytes from a file.
// We always assume the first line in the slice to be incomplete and don't
// print it unless printfirst is set to true. The caller will set printfirst to
// true once it is sure the first line is complete (usually then the file read
// offset == 0)
//
// If the last line is blank and forcePrintprintLast is false, don't print it
// or we'll end up with an extra line at the beginning of the reversed output
// for files ending in a newline (common case). Please note that tac behaves
// differently in such situations.
//
// Returns the full length of the first line, newline included. In most cases
// this line will not have been printed.
func revprint(w io.Writer, buf []byte, printfirst, forcePrintLast bool) int32 {
	var (
		count int32
		ix    int32
		start int32
	)

	buflimit := int32(len(buf) - 1)
	for ix = buflimit; ix >= 0; ix-- {
		//fmt.Println("ix=", ix, "count=", count)
		// If we found a newline and it's the last character in the file, only
		// print it if forcePrintLast is set. Otherwise, we're in the middle of
		// the buffer, so set the next start to this position + 1
		if buf[ix] == '\n' {
			start = ix + 1
			if ix == buflimit {
				if !forcePrintLast {
					// count = 1 to include this newline.
					count = 1
					continue
				}
				start = ix
			}
			w.Write(buf[start : start+count])
			count = 0
		}
		count++
	}

	if printfirst {
		w.Write(buf[0:count])
	}
	//fmt.Println("count =", count)
	return count
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
