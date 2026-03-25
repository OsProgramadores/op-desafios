const { readFileSync } = require('fs')
const file = process.argv[2]
const words = readFileSync(file, 'utf-8')

const listWords = words.split('\n').filter((word) => {
  return word
})

const inputUser = process.argv[3]

function validateInput(userWord) {
  const pattern = /^[A-Za-z_]+$/

  if (pattern.test(userWord)) {
    userWord = userWord.toUpperCase().split('').filter((i) => {
      return i != '_'
    })
    if (userWord.length <= 16) {
      return userWord
    } else {
      console.log('Palavra inválida: limite de caracteres excedido ')
    }

  } else {
    console.log('Palavra inválida: contém caracteres não permitidos')
    return false
  }
}

function removeWrongWords(userWord, listWords) {
  let newListWords = listWords.filter((word) => {
    let newUserWord = [...userWord]
    if (typeof (word) == 'string') {
      word = word.split('')
    }

    for (letter of word) {
      if (!newUserWord.includes(letter)) {
        return false
      }
      else {
        newUserWord.splice(newUserWord.indexOf(letter), 1)
      }
    }
    return word
  })

  return newListWords
}

function removeIndexWord(userWord, word) {
  for (letter of word) {
    userWord.splice(userWord.indexOf(letter), 1)
  }
}

function buildAnagrams(userWord, listWords, anagram) {
  let word = listWords.shift()

  anagram = [...anagram, word]
  let newListWords = [...listWords];
  let newUserWord = [...userWord];

  removeIndexWord(newUserWord, word)
  newListWords = removeWrongWords(newUserWord, newListWords)

  if (newUserWord.length == 0) {
    return anagram
  }
  else {
    let sizeListWords = newListWords.length
    for (let i = 0; i < sizeListWords; i++) {
      let isAnagram = buildAnagrams(newUserWord, newListWords, anagram)
      if (isAnagram) {
        isAnagram = isAnagram.join(' ')
        console.log(isAnagram)
      }
    }
  }
}

function solvesAnagrams(userWord, listWords) {
  listWords = removeWrongWords(userWord, listWords)

  let sizeListWords = listWords.length
  for (let i = 0; i < sizeListWords; i++) {
    let anagram = []
    buildAnagrams(userWord, listWords, anagram)
  }
}

function main() {
  const userWord = validateInput(inputUser)
  if (userWord) {
    solvesAnagrams(userWord, listWords)
  }
}

main()