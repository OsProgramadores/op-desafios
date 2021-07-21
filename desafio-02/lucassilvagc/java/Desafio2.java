package com.company;

public class Desafio2 {

  public static void printPrime() {
    int numeroASerChecado = 2;
    do {
      boolean numPrimo = true;
      int contadorI = 2;
      while (contadorI <= numeroASerChecado / 2) {
        if (numeroASerChecado % contadorI == 0) {
          numPrimo = false;
          break;
        }
        contadorI++;
      }
      if (numPrimo) System.out.println(numeroASerChecado);
      numeroASerChecado++;
    } while (numeroASerChecado <= 10000);
  }

  public static void main(String[] args) {
    printPrime();
  }
}
