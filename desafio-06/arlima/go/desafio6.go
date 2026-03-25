// Adriano Roberto de Lima
// Busca de Anagramas de uma expressão que existem em um dicionario
// Solução inspirada nas dicas que estão em:
// https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1176/assn/anagrams.html#implementation
// e https://github.com/marcopaganini/anagramarama

package main

import (
  "fmt"
  "bufio"
  "os"
  "strings"
  "regexp"
  "sort"
)

var (
  IsLetter = regexp.MustCompile(`^[a-zA-Z]+$`).MatchString
)

type (
	byLen []string
)

//Funcões para poder ordenar um array de strings pelo tamanho da string
func (x byLen) Len() int {
	return len(x)
}

func (x byLen) Swap(i, j int) {
	x[i], x[j] = x[j], x[i]
}

func (x byLen) Less(i, j int) bool {
	leni := len(x[i])
	lenj := len(x[j])
	return leni < lenj
}

func check(e error) {
  if e != nil {
    os.Exit(0)
  }
}

//Le o dicionario do arquivo
func GetDictionary() []string {
  var dictionary []string
  file, err := os.Open("words.txt")
  check(err)
  defer file.Close()
  scanner := bufio.NewScanner(file)
  for scanner.Scan() {
    dictionary = append(dictionary, strings.ToUpper(scanner.Text()))
  }
  check(scanner.Err())
  return dictionary
}

//Le a expressao passada como parametro para o programa
func GetPhrase() string {
  argsWithProg := os.Args
  if len(argsWithProg) !=2 {
    fmt.Println("ERRO! Sintaxe: desafio6 \"expressao\"")
    os.Exit(0)
  }
  phrase := strings.Join(strings.Fields(argsWithProg[1]), "")
  if IsLetter(phrase) == false {
    fmt.Println("ERRO! Use somente caracteres de A-Z na expressao")
    os.Exit(0)
  }
  return strings.ToUpper(phrase)
}

//Criar o mapa de uma palavra
func GetMap(word string) [26]int {
  newmap := [26]int{}
  for _, value := range word {
      newmap[value-'A'] += 1
  }
  return newmap
}

//Verifica se uma palavra está contida em um mapa
func MapContainsWord(inmap [26]int, word string) bool {
  newmap := [26]int{}
  for _, char := range word {
    c := char-'A'
    newmap[c] += 1
    if newmap[c] > inmap[c] {
      return false
    }
  }
  return true
}

//Verifica se um mapa está vazio
func MapIsEmpty(inmap [26]int) bool {
  for i:=0; i<26; i++{
    if inmap[i]!=0{
      return false
    }
  }
  return true
}

//Calcula quantos caracteres existem no mapa
func MapLen(inmap [26]int) int {
  s:=0
  for i:=0; i<26; i++{
    s += inmap[i]
  }
  return s
}

//Subtrai uma lista de palavras de um mapa
func RemainingMap(inmap [26]int, list []string) [26]int {
  newmap := [26]int{}
  ret := [26]int{}

  for _, word := range list {
    for _, value := range word {
      newmap[value-'A'] += 1
    }
  }

  for i:=0; i<26; i++{
    ret[i]=inmap[i]-newmap[i]
  }
  return ret
}

//Função recursiva para calcular os anagramas
func Anagrams(choices []string, result []string, map_phrase [26]int) []string{
  ret := []string{}
  respartial := []string{}

  // Calcular o mapa com os caracteres restantes. Ou seja, a expressão inicial
  // menos todas as palavras do resultado até o momento
  remainingmap := RemainingMap(map_phrase, result)

  // Se o mapa estiver vazio, achamos um anagrama
  if MapIsEmpty(remainingmap) {
    for _, value := range result{
      respartial = append(respartial, value)
    }
    sort.Strings(respartial)
    ret = append(ret, strings.Join(respartial," "))
  }

  s := MapLen(remainingmap)

  for k := 0; k < len(choices); k++ {
    word := choices[k]
    // Se a palavra for maior que o mapa de caracteres restantes, podemos parar
    // pois daqui para frente todas as palavras são iguais ou maiores
    if len(word) > s {
      break
    }
    // Se a palavra está no mapa restante queremos gerar uma nova
    // arvore de buscas. Caso contrário não
    if MapContainsWord(remainingmap, word) {
      r := Anagrams(choices[k+1:], append(result, word), map_phrase)
      ret = append(ret, r...)
    }
  }
  return ret
}

//Funcão main
func main(){
  var dictionary []string
  var result []string

  // Preparando as coisas
  phrase := GetPhrase()
  phrasemap := GetMap(phrase)
  fulldictionary := GetDictionary()

  // Criando o dicionário de palavras válidas. Ou seja, somente aquelas que
  // estão no mapa da expressão fornecedida

  for _, word := range fulldictionary {
    if len(word) > len(phrase){
      continue
    }
    if MapContainsWord(phrasemap, word){
      dictionary = append(dictionary, word)
    }
  }

  // Ordenar pelo tamanho das strings vai ser importante no algoritmo de
  // geração de anagramas

  sort.Sort(byLen(dictionary))

  r := Anagrams(dictionary, result, phrasemap)

  sort.Strings(r)

  for _, word := range r {
    fmt.Println(word)
  }
}
