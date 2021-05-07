
is.prime <- function(num) {
  if (num == 2) {
    TRUE
  } else if (any(num %% 2:(num-1) == 0)) {
    FALSE
  } else {
    TRUE
  }
}

x <- c()
for (i in 1:10000){
  if (is.prime(i)){
    x <- append(x, i)
  }
}
x
