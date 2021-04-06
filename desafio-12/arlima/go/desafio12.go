// Adriano Roberto de Lima
// Solução do desafio 12 - osprogramadores.com

package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"math/big"
	"os"
)

func check(s string) {
	p := 0
	n := new(big.Int)
	n, _ = n.SetString(s, 10)
	for {
		if n.Cmp(big.NewInt(0)) == 0 {
			fmt.Println(s, "false")
			break
		}
		if n.Bit(0) == 1 {
			if n.Cmp(big.NewInt(1)) == 0 {
				fmt.Println(s, "true", p)
			} else {
				fmt.Println(s, "false")
			}
			break
		}

		n = n.Rsh(n, 1)
		p++
	}
}

func main() {
	log.SetFlags(0)
	flag.Parse()

	if len(flag.Args()) != 1 {
		log.Fatalln("Use: desafio12 <arquivo>")
	}

	file, err := os.Open(flag.Args()[0])
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		sNumber := scanner.Text()
		check(sNumber)
	}
}
