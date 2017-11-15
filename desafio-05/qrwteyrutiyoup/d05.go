package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"sync"
)

type area struct {
	name []byte
	code []byte
}

type employee struct {
	name     []byte
	surname  []byte
	salary   float64
	areaCode []byte
}

type salaryStats struct {
	biggest       []*employee
	lowest        []*employee
	employeeCount uint32
	total         float64
	average       float64
}

type groupSalaryStats struct {
	employees []*employee
	salaries  salaryStats
}

type groupSalaryStatsMap map[string]*groupSalaryStats

type d05 struct {
	areas         map[string]*area
	salaries      salaryStats
	employeeCount uint32

	salaryByArea    groupSalaryStatsMap
	salaryBySurname groupSalaryStatsMap
	employeesByArea map[string][]*employee
}

const (
	numberOfBlocksDefault = 16
)

func (dst *salaryStats) mergeSalaryStats(src *salaryStats) {
	dst.employeeCount += src.employeeCount
	dst.total += src.total
	dst.average = dst.total / float64(dst.employeeCount)

	if len(dst.lowest) == 0 || (len(src.lowest) > 0 && src.lowest[0].salary < dst.lowest[0].salary) {
		dst.lowest = append([]*employee{}, src.lowest...)
	} else if (len(dst.lowest) > 0 && len(src.lowest) > 0) && dst.lowest[0].salary == src.lowest[0].salary {
		dst.lowest = append(dst.lowest, src.lowest...)
	}

	if len(dst.biggest) == 0 || (len(src.biggest) > 0 && src.biggest[0].salary > dst.biggest[0].salary) {
		dst.biggest = append([]*employee{}, src.biggest...)
	} else if (len(dst.biggest) > 0 && len(src.biggest) > 0) && dst.biggest[0].salary == src.biggest[0].salary {
		dst.biggest = append(dst.biggest, src.biggest...)
	}

}

func (dst groupSalaryStatsMap) mergeGroupSalary(key string, src *groupSalaryStats) {
	if s, ok := dst[key]; ok {
		s.salaries.mergeSalaryStats(&src.salaries)
		return
	}
	dst[key] = src
}

func (stats *d05) makeStats(wg *sync.WaitGroup, block chan *d05) {
	for {
		select {
		case s := <-block:
			stats.employeeCount += s.employeeCount

			for k, _ := range s.areas {
				//				log.Printf("stats[k]: %s, s.areas[k]: %s\n", stats.areas[k], s.areas[k])
				stats.areas[k] = s.areas[k]
			}

			for k, _ := range s.employeesByArea {
				stats.employeesByArea[k] = append(stats.employeesByArea[k], s.employeesByArea[k]...)
			}

			for k, v := range s.salaryBySurname {
				stats.salaryBySurname.mergeGroupSalary(k, v)
			}

			for k, v := range s.salaryByArea {
				stats.salaryByArea.mergeGroupSalary(k, v)
			}

			stats.salaries.mergeSalaryStats(&s.salaries)
			wg.Done()
		}
	}
}

func (d *d05) parseArea(data []byte, start, end uint32) {
	totalQuotes := 0
	var current uint32
	var previous uint32
	a := &area{}

	for i := start; i < end; i++ {
		if data[i] != '"' {
			continue
		}
		totalQuotes++
		previous = current
		current = i

		switch totalQuotes {
		// {"codigo":"SM", "nome":"Gerenciamento de Software"}
		case 4:
			a.code = make([]byte, current-previous-1)
			copy(a.code, data[previous+1:current])
		case 8:
			a.name = make([]byte, current-previous-1)
			copy(a.name, data[previous+1:current])
			d.areas[string(a.code)] = a
			return
		}
	}
}

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

func (d *d05) calculateSalaries(s map[string]*groupSalaryStats, key []byte, e *employee) {
	gs, ok := s[string(key)]
	if !ok {
		gs = &groupSalaryStats{}
		s[string(key)] = gs
	}

	d.updateSalaries(&gs.salaries, e)
}

func (d *d05) processEmployee(e *employee) {
	d.updateSalaries(&d.salaries, e)
	d.calculateSalaries(d.salaryBySurname, e.surname, e)
	d.calculateSalaries(d.salaryByArea, e.areaCode, e)

	area := string(e.areaCode)
	_, ok := d.employeesByArea[area]
	if !ok {
		d.employeesByArea[area] = []*employee{}
	}
	d.employeesByArea[area] = append(d.employeesByArea[area], e)
	d.employeeCount++
}

func (d *d05) parseEmployee(data []byte, start, end uint32) {
	totalQuotes := 0
	var current uint32
	var previous uint32
	id := []byte("id")

	e := &employee{}

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
			if !bytes.Equal(id, data[previous+1:current]) {
				d.parseArea(data, start, end)
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
			salary, err := strconv.ParseFloat(string(data[previous+2:j+1]), 64)
			if err != nil {
				log.Printf("oops: error converting %q to float: %v\n", data[previous+2:j+1], err)
			}
			e.salary = salary
		case 16:
			e.areaCode = make([]byte, current-previous-1)
			copy(e.areaCode, data[previous+1:current])
			d.processEmployee(e)
			return
		}
	}
}

func (d *d05) parseJSONBlock(data []byte, beginning, end uint32, block chan *d05) {
	var start uint32
	partialSolution := newD05()

	employees := partialSolution.parseEmployee
	areas := partialSolution.parseArea
	parse := &employees

	for i := beginning; i < end; i++ {
		switch data[i] {
		case '{':
			start = i
		case '}':
			(*parse)(data, start, i+1)
		case ']':
			if parse == &areas {
				block <- partialSolution
				return
			}
			parse = &areas
		}
	}
	block <- partialSolution
}

func newD05() *d05 {
	return &d05{employeesByArea: map[string][]*employee{}, salaryByArea: map[string]*groupSalaryStats{}, salaryBySurname: map[string]*groupSalaryStats{}, areas: map[string]*area{}}
}

func parseJSON(data []byte, blocksToUse int) *d05 {
	solution := newD05()
	block := make(chan *d05)
	wg := sync.WaitGroup{}

	go solution.makeStats(&wg, block)

	goroutines := uint32(blocksToUse)
	step := uint32(len(data)) / goroutines

	size := uint32(len(data))
	i := step
	start := uint32(0)
	for p := uint32(0); p < goroutines-1; p++ {
		for i < size {
			if data[i] == '{' {
				wg.Add(1)
				go solution.parseJSONBlock(data, start, i-1, block)
				start = i
				i += step
				break
			}
			i++
		}
	}
	// Last block.
	wg.Add(1)
	go solution.parseJSONBlock(data, start, uint32(len(data))-1, block)
	wg.Wait()
	return solution
}

func (d *d05) solve() {
	var i uint32
	var size uint32
	for i, size = 0, uint32(len(d.salaries.biggest)); i < size; i++ {
		fmt.Printf("global_max|%s %s|%.2f\n", d.salaries.biggest[i].name, d.salaries.biggest[i].surname, d.salaries.biggest[i].salary)
	}
	for i, size = 0, uint32(len(d.salaries.lowest)); i < size; i++ {
		fmt.Printf("global_min|%s %s|%.2f\n", d.salaries.lowest[i].name, d.salaries.lowest[i].surname, d.salaries.lowest[i].salary)
	}
	fmt.Printf("global_avg|%.2f\n", d.salaries.average)

	for areaCode, byArea := range d.salaryByArea {
		for i, size = 0, uint32(len(byArea.salaries.biggest)); i < size; i++ {
			fmt.Printf("area_max|%s|%s %s|%.2f\n", d.areas[areaCode].name, byArea.salaries.biggest[i].name, byArea.salaries.biggest[i].surname, byArea.salaries.biggest[i].salary)
		}
		for i, size = 0, uint32(len(byArea.salaries.lowest)); i < size; i++ {
			fmt.Printf("area_min|%s|%s %s|%.2f\n", d.areas[areaCode].name, byArea.salaries.lowest[i].name, byArea.salaries.lowest[i].surname, byArea.salaries.lowest[i].salary)
		}
		fmt.Printf("area_avg|%s|%.2f\n", d.areas[areaCode].name, byArea.salaries.average)
	}

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

	for surname, bySurname := range d.salaryBySurname {
		if bySurname.salaries.employeeCount <= 1 {
			continue
		}
		for i, size = 0, uint32(len(bySurname.salaries.biggest)); i < size; i++ {
			fmt.Printf("last_name_max|%s|%s %s|%.2f\n", surname, bySurname.salaries.biggest[i].name, bySurname.salaries.biggest[i].surname, bySurname.salaries.biggest[i].salary)
		}
	}
}

func main() {
	if len(os.Args) < 2 {
		log.Fatalf("Usage: %s <input file> [number of concurrent blocks]\n", os.Args[0])
	}

	content, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}

	numberOfBlocks := numberOfBlocksDefault
	if len(os.Args) >= 3 {
		n, err := strconv.ParseInt(os.Args[2], 10, 32)
		if err != nil {
			log.Fatal(err)
		}
		numberOfBlocks = int(n)
	}

	problem := parseJSON(content, numberOfBlocks)
	problem.solve()
}
