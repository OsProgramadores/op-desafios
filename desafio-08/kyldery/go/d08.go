package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

func mdc(n, y int) (int, error) {
	if y == 0 {
		return 0, errors.New("divisão por zero")
	}

	r := n % y

	if r != 0 {
		return mdc(y, r)
	}

	return y, nil
}

func simp(n, y int) (int, int, int, error) {
	c, err := mdc(n, y)

	if err != nil {
		return 0, 0, 0, err
	}

	n /= c
	y /= c
	x := n / y
	r := n % y

	return r, y, x, nil
}

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("Use: <%s> <file>", filepath.Base(os.Args[0]))
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
		l := scanner.Text()

		if strings.Index(l, "/") >= 0 {
			f := strings.Split(l, "/")

			n, _ := strconv.Atoi(f[0])
			y, _ := strconv.Atoi(f[1])

			n, y, x, err := simp(n, y)

			if err != nil {
				fmt.Println("ERR")
				continue
			}

			if y == 1 {
				fmt.Println(x)
				continue
			}

			if x != 0 {
				fmt.Printf("%d ", x)
			}

			fmt.Printf("%d/%d\n", n, y)
		} else {
			fmt.Println(l)
		}
	}
}
