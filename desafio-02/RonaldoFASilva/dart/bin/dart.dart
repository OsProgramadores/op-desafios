void main() {
  int ultimoNumeroAComparar = 10000;
  List<int> numerosPrimos = [];

  for(int i = 1; i <= ultimoNumeroAComparar; i += 1){
    if(verificaSeEhPrimo(i)){
      numerosPrimos.add(i);
    }
  }
  print('=' * 23 + ' Números primos entre 1 e 10.000  ' + '=' * 23);
  imprimeDezNumerosPorLinha(numerosPrimos);
  print('=' * 31 + ' Fim da execução  ' + '=' * 31);
}

bool verificaSeEhPrimo(int numero){
  int quantidadeDivisores = 0;

  for (int i = 1; i <= numero; i += 1){
    if (numero % i == 0){
      quantidadeDivisores += 1;
    }

    if (quantidadeDivisores > 2){
      return false;
    }
  }

  return true;
}

void imprimeDezNumerosPorLinha(List<int> numeros){
  List<int> numerosAImprimir = [];

  for(int i = 0; i < numeros.length; i ++){
    numerosAImprimir.add(numeros[i]);
    if(i > 0 && i % 10 == 0){
      print(numerosAImprimir);
      numerosAImprimir = [];
    }
  }
}