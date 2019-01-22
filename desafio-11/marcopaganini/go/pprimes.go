// Primes in pi - Find the longest sequence of prime numbers in pi
// See https://osprogramadores.com/desafios/d11/
// Marco Paganini <paganini@paganini.net>

package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"runtime/pprof"
	"strconv"
	"strings"
)

func main() {
	if len(os.Args) != 2 {
		log.Fatal("Missing pi input file.")
	}

	// Profiling
	f, err := os.Create("cpu.prof")
	if err != nil {
		log.Fatal(err)
	}
	pprof.StartCPUProfile(f)
	defer pprof.StopCPUProfile()

	pi, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	pi = bytes.TrimRight(pi, "\n\r")

	// Fill in static table of primes.
	primetable()

	longest := []string{}

	// Number of simultaneous goroutines.
	sem := make(chan bool, 128)
	results := make(chan []string, len(pi))

	// Skip "3." at beginning.
	for pos := 2; pos < len(pi); pos++ {
		// Block if the channel is full.
		sem <- true
		go func(p int) {
			results <- findprimes(pi, p)
			// Free one slot.
			<-sem
		}(pos)
	}

	// Block until all workers finished.
	for i := 0; i < cap(sem); i++ {
		sem <- true
	}

	// Process results, find the longest.
	for i := 2; i < len(pi); i++ {
		result := <-results
		if allLen(result) > allLen(longest) {
			longest = result
		}
	}
	fmt.Println(strings.Join(longest, ""))
}

// allLen returns the total length of all string elements in the slice.
func allLen(digits []string) int {
	var size int
	for i := 0; i < len(digits); i++ {
		size += len(digits[i])
	}
	return size
}

// btoi converts a byte slice to an integer.
func btoi(b []byte, offset, size int) int {
	var ret int

	mult := 1
	end := offset + size
	for i := end - 1; i >= offset; i-- {
		ret += int(b[i]-'0') * mult
		mult *= 10
	}
	return ret
}

// findprimes recursively finds primes at the given position in a slice of
// bytes.
func findprimes(pi []byte, start int) []string {
	var longest []string

	for size := 1; size <= 4; size++ {

		// Don't run over the end of pi.
		if start+size > len(pi) {
			continue
		}

		num := btoi(pi, start, size)
		if !primes[num] {
			continue
		}

		r := findprimes(pi, start+size)

		if allLen(r)+1 > allLen(longest) {
			longest = make([]string, len(r)+1)
			longest[0] = strconv.Itoa(num)
			for i := 1; i <= len(r); i++ {
				longest[i] = r[i-1]
			}
		}
	}
	return longest
}
