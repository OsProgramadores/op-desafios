is.prime <- function(num) {
  if (num == 2) { #único número par que é primo
    TRUE
  } else if (any(num %% 2:(num-1) == 0)) { #verifica a quantidade de divisores do número
    FALSE
  } else {
    TRUE
  }
}

resultado <- c()
for (i in 1:10000){
  if (is.prime(i)){ #aplica a função no vetor
    resultado <- append(resultado, i)
  }
}

length(resultado)
print(resultado)