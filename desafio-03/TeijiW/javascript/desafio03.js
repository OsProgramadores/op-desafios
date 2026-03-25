palindrome = (start, end) => {
  for (let i = start;i<end;i++){
    let stringify = i.toString()
    let reverseString= stringify.split('').reverse().join('')
    if (reverseString === stringify){
      console.log(reverseString)
    }
  }
}

palindrome(1,10000)