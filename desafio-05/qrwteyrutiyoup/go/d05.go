package main

import (
	"bytes"
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"runtime/pprof"
	"strconv"
	"sync"
	"unsafe"
)

// area represents an area with its name and code.
type area struct {
	name []byte
	code []byte
}

// employee represents an employee with associate name, surname, salary and
// area.
type employee struct {
	name     []byte
	surname  []byte
	salary   float64
	areaCode []byte
}

// salaryStats contains a list of employees with the biggest and lowest
// salaries, as well as info on the total sum of salary they receive, the number
// of employees considered and the salary average for this whole group.
type salaryStats struct {
	// biggest has a lsit of employees that receive the biggest salary.
	biggest []*employee
	// lowest has a list of employees that receive the lowest salary.
	lowest []*employee
	// employeeCount has the number of employees considered in this group.
	employeeCount uint32
	// total is the sum of salaries of the employees in this group.
	total float64
	// average is the salary average of employees in this group.
	average float64
}

// groupSalaryStats containes a list of employees and an associated salaryStats
// for the considered group.
type groupSalaryStats struct {
	// employees is a list of employees in this group.
	employees []*employee
	// salaries is the stats for this group.
	salaries salaryStats
}

// groupSalaryStatsMap is a map of groupSalaryStats.
type groupSalaryStatsMap map[string]*groupSalaryStats

// d05 represents a solution for this problem.
type d05 struct {
	// areas contains the areas the employees work at.
	areas map[string]area
	// salaries contains stats on the salaries for the whole group.
	salaries salaryStats
	// employeeCount is the number of employees.
	employeeCount uint32

	// salaryByArea maps the areas with a group stats.
	salaryByArea groupSalaryStatsMap
	// salaryBySurname maps the surnames with a group stats.
	salaryBySurname groupSalaryStatsMap
	// employeesByArea maps the areas with a list of employees.
	employeesByArea map[string][]*employee
}

const (
	// numberOfBlocksDefault is the default number of concurrent blocks the JSON
	// input file will be broken into for processing.
	numberOfBlocksDefault = 16
)

// WARNING: DO NOT DO THIS AT HOME.
func unsafeString(b []byte) string {
	return *(*string)(unsafe.Pointer(&b))
}

// newD05 creates a new `d05' value to be used as either a partial or global
// solution for the problem.
func newD05() *d05 {
	return &d05{employeesByArea: map[string][]*employee{}, salaryByArea: map[string]*groupSalaryStats{}, salaryBySurname: map[string]*groupSalaryStats{}, areas: map[string]area{}}
}

// merge gets a salaryStats and merge with the current one.
func (s *salaryStats) merge(salary *salaryStats) {
	s.employeeCount += salary.employeeCount
	s.total += salary.total
	s.average = s.total / float64(s.employeeCount)

	if len(s.lowest) == 0 || (len(salary.lowest) > 0 && salary.lowest[0].salary < s.lowest[0].salary) {
		s.lowest = append([]*employee{}, salary.lowest...)
	} else if (len(s.lowest) > 0 && len(salary.lowest) > 0) && s.lowest[0].salary == salary.lowest[0].salary {
		s.lowest = append(s.lowest, salary.lowest...)
	}

	if len(s.biggest) == 0 || (len(salary.biggest) > 0 && salary.biggest[0].salary > s.biggest[0].salary) {
		s.biggest = append([]*employee{}, salary.biggest...)
	} else if (len(s.biggest) > 0 && len(salary.biggest) > 0) && s.biggest[0].salary == salary.biggest[0].salary {
		s.biggest = append(s.biggest, salary.biggest...)
	}
}

// merge receives a groupSalaryStats and merges with the current one.
func (m groupSalaryStatsMap) merge(key string, src *groupSalaryStats) {
	if s, ok := m[key]; ok {
		s.salaries.merge(&src.salaries)
		return
	}
	m[key] = src
}

// stats receives partial solutions from `block' channel and updates the global
// solution.
func (d *d05) stats(wg *sync.WaitGroup, block chan *d05) {
	for {
		select {
		case partialSolution := <-block:
			d.employeeCount += partialSolution.employeeCount

			for k := range partialSolution.areas {
				d.areas[k] = partialSolution.areas[k]
			}

			for k := range partialSolution.employeesByArea {
				d.employeesByArea[k] = append(d.employeesByArea[k], partialSolution.employeesByArea[k]...)
			}

			for k, v := range partialSolution.salaryBySurname {
				d.salaryBySurname.merge(k, v)
			}

			for k, v := range partialSolution.salaryByArea {
				d.salaryByArea.merge(k, v)
			}

			d.salaries.merge(&partialSolution.salaries)
			wg.Done()
		}
	}
}

// updateSalaries updates the salary stats after processing the info of a single
// employee.
func (d *d05) updateSalaries(s *salaryStats, e *employee) {
	if len(s.biggest) == 0 || e.salary > s.biggest[0].salary {
		s.biggest = []*employee{e}
	} else if s.biggest[0].salary == e.salary {
		s.biggest = append(s.biggest, e)
	}

	if len(s.lowest) == 0 || e.salary < s.lowest[0].salary {
		s.lowest = []*employee{e}
	} else if s.lowest[0].salary == e.salary {
		s.lowest = append(s.lowest, e)
	}
	s.employeeCount++
	s.total += e.salary
	s.average = s.total / float64(s.employeeCount)
}

// calculateSalaries updates a groupSalaryStats map after processing the info of
// a single employee.
func (d *d05) calculateSalaries(s map[string]*groupSalaryStats, key *string, e *employee) {
	gs, ok := s[*key]
	if !ok {
		gs = &groupSalaryStats{}
		s[*key] = gs
	}

	d.updateSalaries(&gs.salaries, e)
}

// processEmployees receive an employee and updates the associated stats.
func (d *d05) processEmployee(e *employee) {
	area := unsafeString(e.areaCode)
	surname := unsafeString(e.surname)

	d.updateSalaries(&d.salaries, e)
	d.calculateSalaries(d.salaryBySurname, &surname, e)
	d.calculateSalaries(d.salaryByArea, &area, e)

	_, ok := d.employeesByArea[area]
	if !ok {
		d.employeesByArea[area] = []*employee{}
	}
	d.employeesByArea[area] = append(d.employeesByArea[area], e)
	d.employeeCount++
}

// parseArea parses an area from the input JSON file.
func (d *d05) parseArea(data []byte) {
	totalQuotes := 0
	var current uint32
	var previous uint32
	a := area{}
	doublequote := byte('"')
	i := uint32(0)
	var idx int
	for {
		if idx = bytes.IndexByte(data[i:], doublequote); idx == -1 {
			break
		}

		totalQuotes++
		previous = current
		current = i + uint32(idx)
		i = current + 1

		switch totalQuotes {
		// {"codigo":"SM", "nome":"Gerenciamento de Software"}
		case 4:
			a.code = make([]byte, current-previous-1)
			copy(a.code, data[previous+1:current])
		case 8:
			a.name = make([]byte, current-previous-1)
			copy(a.name, data[previous+1:current])
			d.areas[unsafeString(a.code)] = a
			return
		}
	}
}

// parseEmployee parses an employee from the input JSON file. If the received
// data is not an employee, it calls parseArea instead.
func (d *d05) parseEmployee(data []byte, start, end uint32) {
	totalQuotes := 0
	var current uint32
	var previous uint32

	e := employee{}

	for i := start; i < end; i++ {
		if data[i] != '"' {
			continue
		}
		totalQuotes++
		previous = current
		current = i

		switch totalQuotes {
		// {"id":1,"nome":"Aahron","sobrenome":"Abaine","salario":68379.29,"area":"PI"}
		case 2:
			// Checking if it is an employee.
			if !bytes.Equal([]byte("id"), data[previous+1:current]) {
				d.parseArea(data[start : end+1])
				return
			}
		case 6:
			e.name = make([]byte, current-previous-1)
			copy(e.name, data[previous+1:current])
		case 10:
			e.surname = make([]byte, current-previous-1)
			copy(e.surname, data[previous+1:current])
		case 13:
			j := current - 2
			for ; j > previous; j-- {
				if data[j] >= '0' && data[j] <= '9' {
					break
				}
			}
			salary, err := strconv.ParseFloat(unsafeString(data[previous+2:j+1]), 64)
			if err != nil {
				log.Printf("oops: error converting %q to float: %v\n", data[previous+2:j+1], err)
			}
			e.salary = salary
		case 16:
			e.areaCode = make([]byte, current-previous-1)
			copy(e.areaCode, data[previous+1:current])
			d.processEmployee(&e)
			return
		}
	}
}

// parseJSONBlock parses a block of JSON data from the input file. This method
// will be run concurrently and generate a partial solution from the data it
// processes, then send the result via the `block' channel.
func (d *d05) parseJSONBlock(data []byte, block chan *d05) {
	var start uint32

	partialSolution := newD05()

	openbracket := byte('{')
	closedbracket := byte('}')
	i := uint32(0)
	var idx int
	for {
		if idx = bytes.IndexByte(data[i:], openbracket); idx == -1 {
			break
		}
		start = i + uint32(idx)
		i = start

		if idx = bytes.IndexByte(data[i:], closedbracket); idx == -1 {
			break
		}
		i += uint32(idx)
		partialSolution.parseEmployee(data, start, i)
		i++

	}

	block <- partialSolution
}

// parseJSON receives the full JSON data from the input file and calls
// `parseJSONBlocks' to process the smaller blocks. It returns the global
// solution for the problem at hand, once the partial solutions have all been
// accounted for.
func parseJSON(data []byte, blocksToUse uint32) *d05 {
	solution := newD05()
	block := make(chan *d05)
	wg := sync.WaitGroup{}

	// Goroutine that will receive the partial solutions.
	go solution.stats(&wg, block)
	// An average step to form the blocks.
	step := uint32(len(data)) / blocksToUse

	size := uint32(len(data))
	i := step
	start := uint32(1)
	bracket := byte('{')
	var idx int
	for p := uint32(0); p < blocksToUse-1; p++ {
		for i < size {
			if idx = bytes.IndexByte(data[i:], bracket); idx == -1 {
				break
			}

			wg.Add(1)
			i += uint32(idx)
			go solution.parseJSONBlock(data[start:i-1], block)
			start = i
			i += step
			break
		}
	}
	// Last block.
	wg.Add(1)
	go solution.parseJSONBlock(data[start:], block)
	wg.Wait()
	return solution
}

// solve prints the solution for the problem, once everything is done.
func (d *d05) solve() {
	wg := sync.WaitGroup{}
	wg.Add(5)

	go func() {
		for i, size := uint32(0), uint32(len(d.salaries.biggest)); i < size; i++ {
			fmt.Printf("global_max|%s %s|%.2f\n", d.salaries.biggest[i].name, d.salaries.biggest[i].surname, d.salaries.biggest[i].salary)
		}
		wg.Done()
	}()

	go func() {
		for i, size := uint32(0), uint32(len(d.salaries.lowest)); i < size; i++ {
			fmt.Printf("global_min|%s %s|%.2f\n", d.salaries.lowest[i].name, d.salaries.lowest[i].surname, d.salaries.lowest[i].salary)
		}
		wg.Done()
	}()

	fmt.Printf("global_avg|%.2f\n", d.salaries.average)

	go func() {
		var i uint32
		var size uint32

		for areaCode, byArea := range d.salaryByArea {
			for i, size = 0, uint32(len(byArea.salaries.biggest)); i < size; i++ {
				fmt.Printf("area_max|%s|%s %s|%.2f\n", d.areas[areaCode].name, byArea.salaries.biggest[i].name, byArea.salaries.biggest[i].surname, byArea.salaries.biggest[i].salary)
			}
			for i, size = 0, uint32(len(byArea.salaries.lowest)); i < size; i++ {
				fmt.Printf("area_min|%s|%s %s|%.2f\n", d.areas[areaCode].name, byArea.salaries.lowest[i].name, byArea.salaries.lowest[i].surname, byArea.salaries.lowest[i].salary)
			}
			fmt.Printf("area_avg|%s|%.2f\n", d.areas[areaCode].name, byArea.salaries.average)
		}
		wg.Done()
	}()

	go func() {
		lessEmployees := d.employeeCount
		mostEmployees := uint32(0)
		count := uint32(0)
		for _, byArea := range d.employeesByArea {
			count = uint32(len(byArea))
			if count < lessEmployees {
				lessEmployees = count
			}
			if count > mostEmployees {
				mostEmployees = count
			}
		}
		for areaCode, byArea := range d.employeesByArea {
			count = uint32(len(byArea))
			if count == mostEmployees {
				fmt.Printf("most_employees|%s|%d\n", d.areas[areaCode].name, count)
			}
			if count == lessEmployees {
				fmt.Printf("least_employees|%s|%d\n", d.areas[areaCode].name, count)
			}
		}
		wg.Done()
	}()

	go func() {
		for surname, bySurname := range d.salaryBySurname {
			if bySurname.salaries.employeeCount <= 1 {
				continue
			}
			for i, size := uint32(0), uint32(len(bySurname.salaries.biggest)); i < size; i++ {
				fmt.Printf("last_name_max|%s|%s %s|%.2f\n", surname, bySurname.salaries.biggest[i].name, bySurname.salaries.biggest[i].surname, bySurname.salaries.biggest[i].salary)
			}
		}
		wg.Done()
	}()

	wg.Wait()
}

func main() {
	var optCPUProfile string

	flag.StringVar(&optCPUProfile, "cpuprofile", "", "write cpu profile to file")
	flag.Parse()

	if len(flag.Args()) < 2 {
		log.Fatalf("Usage: %s [-cpuprofile=<profile>] <input file> [number of concurrent blocks]\n", os.Args[0])
	}

	// Profiling
	if optCPUProfile != "" {
		f, err := os.Create(optCPUProfile)
		if err != nil {
			log.Fatal(err)
		}
		pprof.StartCPUProfile(f)
		defer pprof.StopCPUProfile()
	}

	content, err := ioutil.ReadFile(flag.Args()[0])
	if err != nil {
		log.Fatal(err)
	}

	numberOfBlocks := uint32(numberOfBlocksDefault)
	if len(os.Args) >= 3 {
		n, err := strconv.ParseUint(flag.Args()[1], 10, 32)
		if err != nil {
			log.Fatal(err)
		}
		numberOfBlocks = uint32(n)
	}

	problem := parseJSON(content, numberOfBlocks)
	problem.solve()
}
