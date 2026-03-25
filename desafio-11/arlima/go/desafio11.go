// Adriano Roberto de Lima
// Solução do desafio 11 - osprogramadores.com
// Otimizada para rodar o mais rapido possível
// Processa as sequências sem espaços entre os primos encontrados

package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"math"
	"os"
	"runtime"
	"runtime/pprof"
)

// Estrutura para ser enviada no canal de requests da função startWorkers.
type (
	sRequest struct {
		posInicial  int
		palavra     []byte
		posicao     int
		sequencia   string
		dados       []byte
		lenDados    int
		testaPrimo  []bool
		lenMaiorSeq int
	}

	// Estrutura que vamos usar para retornar as sequencias e a posição onde foram
	// encontradas. Precisamos registrar as posições pois não sabemos a ordem
	// de finalização dos requests que serão processados pelos workers (goroutines)
	sSequencia struct {
		sequencia  string
		posInicial int
	}
)

// geraprimos é uma função para geração de um array que identifica se um
// número é primo ou não. Vamos usar esse array para acelerar a identificação
// de números primos na busca das soluções.
// Referência: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
// Só vamos rodar uma vez.
func geraPrimos(n int64) []bool {
	var (
		i, j int64
	)

	flag1 := make([]bool, n)
	for i = 0; i < n; i++ {
		flag1[i] = true
	}

	flag1[0] = false
	flag1[1] = false

	for i = 2; i < int64(math.Sqrt(float64(n)))+1; i++ {
		if flag1[i] {
			for j = i * i; j < n; j += i {
				flag1[j] = false
			}
		}
	}
	return flag1
}

// palavraToInt converte um array de bytes para um inteiro. Não faz nenhum tipo
// de verificação. Serve para converter a palavra que está na função "geraSequencias".
// É bem mais rápido do que fazer um strconv.Atoi(string(b))
func palavraToInt(b []byte) int {
	n := 0
	for _, ch := range b {
		ch -= '0'
		n = n*10 + int(ch)
	}
	return n
}

// geraSequencias é a função utilizada para encontrar sequencias de numeros primos,
// de no máximo 4 digitos, maiores que lenMaiorSeq, partindo de uma posição p
// de uma sequência de digidos "dados".
func geraSequencias(posInicial int, palavra []byte, posicao int, sequencia string, dados []byte, lenDados int, testaPrimo []bool, lenMaiorSeq int) []sSequencia {
	ret := []sSequencia{}
	novapalavra := append(palavra, dados[posicao])

	// Se o tamanho da palavra é maior que quatro bytes então já ultrapassamos o limite
	// para encontrar um numero primo. Por isso
	// retornamos a sequência que encontramos se ela for maior ou igual a lenMaiorSeq.
	if posicao >= lenDados || len(novapalavra) > 4 {
		if len(sequencia) >= lenMaiorSeq {
			ret = append(ret, sSequencia{sequencia, posInicial})
		}
		return ret
	}

	// Aqui disparamos a busca por novas soluções considerando a novapalavra, partindo
	// da nova posição e a sequencia que já temos.
	r := geraSequencias(posInicial, novapalavra, posicao+1, sequencia, dados, lenDados, testaPrimo, lenMaiorSeq)
	ret = append(ret, r...)

	// Se a nova palavra for um primo, podemos colocá-la na sequencia e continuar
	// a busca por novas palavras válidas.
	if testaPrimo[palavraToInt(novapalavra)] {
		r = geraSequencias(posInicial, []byte{}, posicao+1, sequencia+string(novapalavra), dados, lenDados, testaPrimo, lenMaiorSeq)
		ret = append(ret, r...)
	}

	return ret
}

// worker é a função que faz as chamadas da nossa função geraSequencias usando
// os canais de entrada e retornando as respostas nos canais de saída.
// Eles ficam sempre ativos esperando jobs (ou requests) chegarem para serem
// processados.
func worker(id int, req <-chan sRequest, res chan<- []sSequencia) {
	for c := range req {
		r := geraSequencias(c.posInicial, c.palavra, c.posicao, c.sequencia, c.dados, c.lenDados, c.testaPrimo, c.lenMaiorSeq)
		res <- r
	}
}

// startWorkers é a nossa função que dispara os workers, dispara os requests para
// os workers e consolida as respostas que vem pelos canais de saída. Retorna todas
// as sequencias encontradas.
func startWorkers(workers int, batchSize int, dados []byte, lenDados int) []sSequencia {
	var (
		sequencias   []sSequencia
		batchResults []sSequencia
	)

	lenMaiorSeq := 1
	testaPrimo := geraPrimos(10000)
	jobs := make(chan sRequest, batchSize)        // Bufferizado no tamanho do batch.
	results := make(chan []sSequencia, batchSize) // Bufferizado no tamanho do batch.

	// Colocando no ar todos os workers.
	for w := 0; w < workers; w++ {
		go worker(w, jobs, results)
	}

	// Disparando os jobs para serem processados pelos workers. Vamos disparar
	// em lotes de tamanho batchSize para podermos pegar resultados intermediarios.
	// Fazemos isso para encontrar o tamanho da maior sequencia e minimizar a
	// quantidade de sequencias obtidas na funçao recursiva. Nos interessam somente
	// as maiores.

	a := 2 //Todo arquivo começa com "3." . Precisamos desconsiderar.
	for a < lenDados {
		if a+batchSize >= lenDados {
			batchSize = lenDados - a
		}
		for b := 0; b < batchSize; b++ {
			req := sRequest{
				posInicial:  a + b,
				palavra:     []byte{},
				posicao:     a + b,
				sequencia:   "",
				dados:       dados,
				lenDados:    lenDados,
				testaPrimo:  testaPrimo,
				lenMaiorSeq: lenMaiorSeq,
			}
			jobs <- req
		}

		//  Coletando os resultados dos canais de saída.
		batchResults = []sSequencia{}
		for b := 0; b < batchSize; b++ {
			r := <-results
			batchResults = append(batchResults, r...)
		}

		// Coletando apenas as maiores sequencias e o valor de lenMaiorSeq para usar.
		// nos proximos batches
		for _, v := range batchResults {
			l := len(v.sequencia)
			if l > lenMaiorSeq {
				lenMaiorSeq = l
				sequencias = []sSequencia{v}
			} else {
				if l == lenMaiorSeq {
					sequencias = append(sequencias, v)
				}
			}
		}
		a += batchSize
	}
	return sequencias
}

func main() {
	var (
		optCPUProfile string
		optBatchSize  int
	)

	runtime.GOMAXPROCS(runtime.NumCPU())
	log.SetFlags(0)

	flag.StringVar(&optCPUProfile, "cpuprofile", "", "escreve a profile de cpu em arquivo")
	flag.IntVar(&optBatchSize, "batchsize", 0, "tamanho do batch de processamento paralelo")
	flag.Parse()

	if len(flag.Args()) != 1 {
		log.Fatalln("Use: desafio 11 <arquivo>")
	}

	if optCPUProfile != "" {
		f, err := os.Create(optCPUProfile)
		if err != nil {
			log.Fatal(err)
		}
		pprof.StartCPUProfile(f)
		defer pprof.StopCPUProfile()
	}

	batchSize := 1000
	if optBatchSize != 0 {
		batchSize = optBatchSize
	}

	dados, err := ioutil.ReadFile(flag.Args()[0])
	if err != nil {
		fmt.Println("ERRO! Não consegui ler o arquivo !")
		log.Fatal(err)
	}

	lenDados := len(dados)
	// Adicionando alguns bytes ao final dos dados para gaarantir que toda
	// a sequência será tratada.
	extras := []byte{0, 0, 0, 0}
	dados = append(dados, extras...)

	// Começando o trabalho de busca das soluções.
	sequencias := startWorkers(runtime.NumCPU(), batchSize, dados, lenDados)

	// Procurando a maior sequencia na menorPosicao.
	menorPosicao := lenDados
	sequenciaMenorPosicao := ""
	for _, v := range sequencias {
		if v.posInicial < menorPosicao {
			menorPosicao = v.posInicial
			sequenciaMenorPosicao = v.sequencia
		}
	}

	fmt.Println(sequenciaMenorPosicao)

	fmt.Print("\n\n")
}
