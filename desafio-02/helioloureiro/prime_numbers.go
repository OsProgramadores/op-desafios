package main

import (
  "fmt"
  //"math"
  "time"
)

func is_prime(number int) bool {
  /*
  src: https://en.wikipedia.org/wiki/Primality_test
   function is_prime(n)
     if n ≤ 3
        return n > 1
     else if n mod 2 = 0 or n mod 3 = 0
        return false
     let i ← 5
     while i * i ≤ n
        if n mod i = 0 or n mod (i + 2) = 0
            return false
        i ← i + 6
     return true
  */
  if number <= 3 {
    return true
  }
  if number % 2 == 0 {
    return false
  }
  if number %3 == 0 {
    return false
  }
  var i = 5
  for i * i <= number {
    if number%i == 0 {
      return false
    }
    if number%(i+2) == 0 {
      return false
    }
    i += 6
  }
  return true
}

func main() {
  time_start := time.Now()
  var prime_counter = 0
  fmt.Println("Prime numbers")
  for n :=1; n<= 10000; n++ {
    if is_prime(n) == true {
      fmt.Println(n)
      prime_counter++
    }
  }
  fmt.Printf("Prime numbers found: %d\n", prime_counter)
  fmt.Printf("Total time: %v\n", time.Since(time_start))
}