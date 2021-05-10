Reverse.number <- function(x){ 
  n <- trunc(log10(x))  #retorna a quantidade de potências de 10
  x.rem <- x  #armazena os demais números
  x.out <- 0  #armazena a saída
  for(i in n:0){
    x.out <- x.out + (x.rem %/% 10^i)*10^(n-i) 
    x.rem <- x.rem - (x.rem %/% 10^i)*10^i  
  } 
  return(x.out) 
}

is.palindrom <- function(num){
  num == sapply(num, Reverse.number) #aplica a função Reverse e retorna True ou False
}

resultado <- c()
for (y in 1:100000) {
  if (is.palindrom(y)){ #aplica a função palídromo no vetor
    resultado <- append(resultado, y)
  }
}
length(resultado)
print(resultado)
