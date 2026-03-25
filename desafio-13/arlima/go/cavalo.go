// Solução do desafio 13 - https://osprogramadores.com
// Adriano Roberto de Lima

package main

import (
	"fmt"
	"os"
)

const (
	rows    = 8
	columns = 8
)

type boardPosition struct {
	column int
	row    int
}

func successors(bp boardPosition) []boardPosition {
	locations := []boardPosition{}
	if bp.row+2 < rows && bp.column+1 < columns {
		locations = append(locations, boardPosition{bp.column + 1, bp.row + 2})
	}
	if bp.row+2 < rows && bp.column-1 >= 0 {
		locations = append(locations, boardPosition{bp.column - 1, bp.row + 2})
	}
	if bp.row-2 >= 0 && bp.column+1 < columns {
		locations = append(locations, boardPosition{bp.column + 1, bp.row - 2})
	}
	if bp.row-2 >= 0 && bp.column-1 >= 0 {
		locations = append(locations, boardPosition{bp.column - 1, bp.row - 2})
	}
	if bp.row+1 < rows && bp.column+2 < columns {
		locations = append(locations, boardPosition{bp.column + 2, bp.row + 1})
	}
	if bp.row+1 < rows && bp.column-2 >= 0 {
		locations = append(locations, boardPosition{bp.column - 2, bp.row + 1})
	}
	if bp.row-1 >= 0 && bp.column+2 < columns {
		locations = append(locations, boardPosition{bp.column + 2, bp.row - 1})
	}
	if bp.row-1 >= 0 && bp.column-2 >= 0 {
		locations = append(locations, boardPosition{bp.column - 2, bp.row - 1})
	}
	return locations
}

func notInPath(bp boardPosition, path []boardPosition) bool {
	for _, v := range path {
		if v == bp {
			return false
		}
	}
	return true
}

func validSuccessors(bp boardPosition, path []boardPosition) int {
	s := 0
	for _, v := range successors(bp) {
		if notInPath(v, path) {
			s++
		}
	}
	return s
}

func display(path []boardPosition) {
	for _, v := range path {
		fmt.Printf("%c%d\n", 'a'+v.column, v.row+1)
	}
}

// https://en.wikipedia.org/wiki/Knight%27s_tour
func warnsdorff(start boardPosition) []boardPosition {
	path := []boardPosition{}
	position := start
	path = append(path, position)
	for len(path) < rows*columns {
		min := 8
		posMin := boardPosition{}
		for _, v := range successors(position) {
			if notInPath(v, path) {
				m := validSuccessors(v, path)
				if m < min {
					min = m
					posMin = v
				}
			}
		}
		position = posMin
		path = append(path, position)
	}
	return path
}

func getStartPosition() boardPosition {
	argsWithProg := os.Args
	if len(argsWithProg) != 2 {
		fmt.Println("ERRO! Sintaxe: desafio13 posição")
		os.Exit(0)
	}
	parameter := argsWithProg[1]
	return boardPosition{int(parameter[0] - 'a'), int(parameter[1] - '1')}
}

func main() {
	solution := warnsdorff(getStartPosition())
	display(solution)
}
