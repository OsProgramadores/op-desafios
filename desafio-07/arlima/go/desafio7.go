// Adriano Roberto de Lima
// Desafio 07

package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
)

const (
	buffersize = 65535
)

// reverse é uma função para inverter um array de bytes.
func reverse(s []byte) {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}

// processblock é uma função para ler um bloco do dispositivo de entrada e gravar a saida em outro dispositivo.
// Lê o bloco do fim para o começo e a cada \n encontrado manda para o dispositivo de saida
// na ordem correta.
func processblock(f io.ReaderAt, out io.Writer, buffersize int64, position int64, ignorefirstreturn bool, line []byte) ([]byte, error) {
	buffer := make([]byte, buffersize)
	_, err := f.ReadAt(buffer, position)
	if err != nil {
		return nil, err
	}

	for i := buffersize - 1; i >= 0; i-- {
		letter := buffer[i]
		if letter == '\n' {
			reverse(line)
			if !(ignorefirstreturn && (i == buffersize-1)) {
				line = append(line, '\n')
			}
			_, err := out.Write(line)
			if err != nil {
				return nil, err
			}
			line = []byte{}
		} else {
			line = append(line, letter)
		}
	}
	return line, nil
}

func main() {
	var line []byte
	var block int64
	var appendtoend bool
	var filename string

	if len(os.Args) != 2 {
		fmt.Println("ERRO! Sintaxe: desafio7 \"nomedoarquivo\"")
		os.Exit(0)
	} else {
		filename = os.Args[1]
	}

	// Pegando o tamanho do arquivo.
	finfo, err := os.Stat(filename)
	if err != nil {
		log.Fatal(err)
	}

	lenfile := finfo.Size()

	// Calculando a quantidade de blocos inteiros a serem lidos e o tamanho
	// do ultimo bloco que pode não ser inteiro.
	nblocks := lenfile / buffersize
	lenlastblock := lenfile % buffersize

	// Abrindo o arquivo.
	fin, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}

	defer fin.Close()

	// Abrindo o dispositivo de saída.
	out := bufio.NewWriterSize(os.Stdout, 65535)
	defer out.Flush()

	// Verificando se o arquivo tem um \n no final. Caso positivo vamos adicionar ao
	// final da nossa saída também.
	endchar := make([]byte, 1)
	_, err = fin.ReadAt(endchar, lenfile-1)
	if err != nil {
		log.Fatal(err)
	}

	if string(endchar[0]) == "\n" {
		appendtoend = true
	}

	// Processando os blocos inteiros.
	for block = nblocks - 1; block >= 0; block-- {
		line, err = processblock(fin, out, buffersize, block*buffersize+lenlastblock, (block == nblocks-1), line)
		if err != nil {
			log.Fatal(err)
		}
	}

	// Processando o bloco não inteiro.
	line, err = processblock(fin, out, lenlastblock, 0, false, line)
	if err != nil {
		log.Fatal(err)
	}

	// Imprimindo o resto da leitura.
	reverse(line)
	if appendtoend {
		line = append(line, '\n')
	}
	_, err = out.Write(line)
	if err != nil {
		log.Fatal(err)
	}
}
