function primos (a, b) {
  for (i = a; i<= b; i++) {
    let divisores = 0;
    for (n = 1; n<=i; n++) {
      if(i % n === 0) {
        divisores++;
      }
    }
    if (divisores === 2) {
      console.log(i);
    }
  }
}
primos(1, 100);