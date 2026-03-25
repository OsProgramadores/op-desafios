#!/usr/bin/awk -f
BEGIN {
  for (num=2;num<=10000;num++) {
    primo=1
    md=int(sqrt(num))
    for (div=2;div<=md;div++) {
      if (num%div == 0) {
        primo=0
        break
      }
    }
    if (primo == 1) {
      print num
    }
  }
}
