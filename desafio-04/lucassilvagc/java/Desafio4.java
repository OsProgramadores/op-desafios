/*
Desafio 04 - Os Programadores
Lucas Silva - github.com/lucassilvagc

Instruções para Execução:

1) javac -d . Desafio4.java
2) java br.lucassilvagc.Desafio4
*/

package br.lucassilvagc;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Desafio4 {

  static Scanner scanner = new Scanner(System.in);
  static String[] pecas = {"Vazio", "Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei"};

  public static void main(String[] args) {
    System.out.println(
        "O Xadrez é um jogo de tabuleiro estratégico que consiste em um tabuleiro de 8 linhas e"
            + " colunas.");
    System.out.println("No total, são 64 (sessenta e quatro) posições, em uma matriz 8x8.");
    System.out.println(
        "São utilizadas as seguintes peças e quantidades:"
            + "\n"
            + "1 - Peão - 8 peças\n"
            + "2 - Bispo - 2 peças\n"
            + "3 - Cavalo - 2 peças\n"
            + "4 - Torre - 2 peças\n"
            + "5 - Rainha - 1 peça\n"
            + "6 - Rei - 1 peça\n");
    System.out.println(
        "Este código consiste na criação de uma matriz 8x8 e, posteriormente, com a detecção de"
            + " quantas peças de cada tipo estão inseridas na matriz.");
    System.out.println(
        "Na tabela acima, existirão os números de referência, que vão de 1 a 6, e que ajudarão a"
            + " determinar quantas peças de cada tipo existem na matriz.");
    System.out.println(
        "Você deverá inserir, portanto, 64 (sessenta e quatro) números, variando de 0 a 6, onde 0 é"
            + " vazio, considerando a tabela acima.");
    List<Integer> list = generateList();
    listVerifier(list);
  }

  private static List<Integer> generateList() {
    List<Integer> list = new ArrayList<>();
    for (Integer i = 1; i <= 8; i++) {
      System.out.println(
          "Esta é a "
              + i
              + "ª linha. Você deverá inserir 8 (oito) números maiores ou iguais a 0 e menores ou"
              + " iguais a 6.");
      for (Integer j = 1; j <= 8; j++) {
        System.out.println("Insira o " + j + "º valor: ");
        list.add(verifyNumber(scanner.next()));
      }
      System.out.println("Você finalizou a " + i + "ª linha com sucesso.");
    }
    return list;
  }

  public static void listVerifier(List<Integer> list) {
    System.out.println("Agora, verificaremos a lista que você enviou.");
    System.out.println("Foram encontradas as seguintes peças em seu tabuleiro:\n");

    for (int i = 1; i < pecas.length; i++) {
      StringBuilder stringBuilder = new StringBuilder();
      stringBuilder
          .append(pecas[i])
          .append(": ")
          .append(Collections.frequency(list, i))
          .append(" peça(s).");
      System.out.println(stringBuilder.toString());
    }
  }

  /*
   * Este método verifica se o número é maior ou igual a 0 e é menor ou igual a 6, usando condicionais para tal.
   * O restante do código, no que tange à funcionalidade principal (contagem), não utiliza nenhuma condicional.
   * */
  private static Integer verifyNumber(String number) {
    Integer numberVerifier = 0;
    Boolean passed = false;
    while (!passed) {
      try {
        numberVerifier = Integer.parseInt(number);
        if (numberVerifier >= 0 && numberVerifier <= 6) {
          passed = true;
        } else {
          System.out.println(
              "O número que você enviou ("
                  + number
                  + ") não é aceitável (está menor que zero). Ele deve ser maior ou igual a 0 "
                  + "e menor ou igual a 6. "
                  + "Insira um novo número para continuar: ");
          number = scanner.next();
          passed = false;
        }
      } catch (Exception ex) {
        System.out.println(
            "O número que você enviou ("
                + number
                + ") não é aceitável (não é um número inteiro). Ele deve ser maior ou igual a 0 e"
                + " menor ou igual que 6. Insira um novo número para continuar: ");
        number = scanner.next();
      }
    }
    return numberVerifier;
  }
}
