
is.prime <- function(num) {
  if (num == 1) { #1 nao e primo
    FALSE
  }
  if (num == 2) { #único número par que é primo
    TRUE
  } else if (any(num %% 2:(num-1) == 0)) { #verifica a quantidade de divisores do numero
    FALSE
  } else {
    TRUE
  }
}

resultado <- c()
for (i in 1:10000){
  if (is.prime(i)){ #aplica a funcao no vetor
    resultado <- append(x, i)
  }
}

length(resultado)
print(resultado)
