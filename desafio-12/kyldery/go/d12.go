package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"path/filepath"
)

func verificarPotenciaDe2(n *big.Int) (bool, uint64) {
	var exp uint64

	for ; n.Cmp(big.NewInt(1)) != 0; exp++ {
		dois := big.NewInt(2)

		resto := new(big.Int).Mod(n, dois)

		if resto.Sign() != 0 || n.Sign() == 0 {
			return false, 0
		}

		n = new(big.Int).Div(n, dois)
	}

	return true, exp
}

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("Use: <%s> <file>\n", filepath.Base(os.Args[0]))
		os.Exit(1)
	}

	file, err := os.Open(os.Args[1])

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()

		bigNum := big.NewInt(0)

		_, ok := bigNum.SetString(line, 0)

		if ok {
			vt, exp := verificarPotenciaDe2(bigNum)

			if vt {
				fmt.Printf("%s %t %d\n", bigNum.Text(10), vt, exp)
			} else {
				fmt.Printf("%v %t\n", bigNum, vt)
			}
		}
	}
}
