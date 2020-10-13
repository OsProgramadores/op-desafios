#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

short int palindromo( uint64_t num) {
  char numeroString[99];

  // convertendo o inteiro 'num' para o buffer numeroString
  sprintf(numeroString, "%ld", num);

  // tamanho da palavra
  uint16_t tamanhoDoNumero = (uint16_t) strlen(numeroString);

  // verificando se é palindromo
  for(uint16_t index = 0; index < tamanhoDoNumero; index++) {
    if(numeroString[index] != numeroString[tamanhoDoNumero-index-1]) {
      return 0;
    }
  }

  return 1;
}

int main(void) {

  // limites 
  uint64_t limInf, limSup;

  printf("Digite o limite inferior: ");
  scanf("%ld", &limInf);

  while (limInf < 1) {
    printf("Por favor, digite um número inteiro positivo: ");
    scanf("%ld", &limInf);
  }

  printf("\nDigite o limite superior: ");
  scanf("%ld", &limSup);

  while (limSup > 99999999999999999) {
    printf("Por favor, digite um limite superior menor: ");
    scanf("%ld", &limSup);
  }

  // se o limite inferior for maior que o superior
  if(limInf > limSup) {
    printf("\nLimite superior não pode ser maior que o inferior!");
    return -1;
  }

  for(int64_t n = limInf; n <= limSup; n++) {
    if(palindromo(n)) {
      printf("\n%ld eh palindromo", n);
    }
  }

  return 0;
}
