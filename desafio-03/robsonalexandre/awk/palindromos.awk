#!/usr/bin/awk -f
BEGIN {
  if (ARGC<2) {
    print "É necessário informar 2 números:\n  palindromos.awk NUM NUM"
  } else {
    for (num=ARGV[1];num<=ARGV[2];num++) {
      rev=""
      for (c=length(num);c>0;c--) {
        rev=rev substr(num, c, 1)
      }
      if (num == rev)
        print rev
    }
  }
}
