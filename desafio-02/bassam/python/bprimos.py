for nro in range (2,10001):
  p=0
  for i in range(2,nro//2+1):
    if(nro%i==0):
      p=p+1
  if(p<=0):
    print(nro, end=' ')
