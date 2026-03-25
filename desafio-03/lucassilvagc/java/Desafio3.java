/*
Desafio 03 - Os Programadores
Lucas Silva - github.com/lucassilvagc

Instruções para Execução:

1) javac -d . Desafio3.java
2) java br.lucassilvagc.Desafio3
*/

package br.lucassilvagc;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Desafio3 {

  static Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) {
    System.out.println(
        "Insira o número inicial. Ele deverá ser maior que 0 e menor que " + Long.MAX_VALUE + ": ");
    long inicio, fim;
    inicio = verifyNumber(scanner.next());
    System.out.println(
        "Insira o número final. Ele deverá ser maior que 0 e menor que " + Long.MAX_VALUE + ": ");
    fim = verifyEndingNumber(inicio, verifyNumber(scanner.next()));
    System.out.println(
        "Os números detectados são aceitáveis e serão utilizados para a geração da lista.");
    System.out.println(
        "Palíndromos encontrados entre os números "
            + inicio
            + " e "
            + fim
            + ": "
            + returnPalindromeList(inicio, fim));
  }

  private static List<Long> returnPalindromeList(long inicio, long fim) {
    System.out.println("Gerando lista de palíndromos...");
    List<Long> palindromeList = new ArrayList<>();
    System.out.println("Processando lista de palíndromos...");
    for (long i = inicio; i <= fim; i++) {
      String num = String.valueOf(i);
      StringBuilder stringBuilder = new StringBuilder();
      int j = num.length() - 1;
      do {
        stringBuilder.append(num.charAt(j));
        j--;
      } while (j >= 0);
      if (num.equals(stringBuilder.toString())) palindromeList.add(i);
    }
    System.out.println(
        "Lista de palíndromos processada com sucesso. Total de palíndromos encontrados: "
            + palindromeList.size());
    return palindromeList;
  }

  private static long verifyEndingNumber(long inicio, long fim) {
    while (inicio > fim) {
      System.out.println(
          "O número inicial que você enviou ("
              + inicio
              + ") é maior que o número final enviado ("
              + fim
              + "). Insira um novo número para continuar: ");
      fim = verifyNumber(scanner.next());
    }
    return fim;
  }

  private static long verifyNumber(String number) {
    long numberVerifier = 0;
    boolean passed = false;
    while (!passed) {
      try {
        numberVerifier = Long.parseLong(number);
        if (numberVerifier > 0) {
          passed = true;
        } else {
          System.out.println(
              "O número que você enviou ("
                  + number
                  + ") não é aceitável (está menor ou igual a zero). Ele deve ser maior que 0 e"
                  + " menor que "
                  + Long.MAX_VALUE
                  + ". Insira um novo número para continuar: ");
          number = scanner.next();
          passed = false;
        }
      } catch (Exception ex) {
        System.out.println(
            "O número que você enviou ("
                + number
                + ") não é aceitável (não é um número unsigned int). Ele deve ser maior que 0 e"
                + " menor que "
                + Long.MAX_VALUE
                + ". Insira um novo número para continuar: ");
        number = scanner.next();
      }
    }
    return numberVerifier;
  }
}
