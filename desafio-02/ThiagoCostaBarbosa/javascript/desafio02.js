function prime(max) {
  max = parseInt(max)
  if (max < 2) {
    return [];
  }
  var number,
      array = [2],
      prime_lenght,
      check_prime,
      iterator;

  for (number = 3; number <= max; number++) {
    prime_lenght = array.length;
    check_prime = 0;

    //check if divide by prime number
    for (iterator = 0; iterator < prime_lenght; iterator++) {
      if (!(number % array[iterator])) {
        check_prime++;
        iterator = prime_lenght;
      }
    }
    //add prime number to array of primes
    if (check_prime === 0) {
      array.push(number);
    }
    number++;
  }
  return array;
}

prime(10000).forEach( i => { console.log(i) });
