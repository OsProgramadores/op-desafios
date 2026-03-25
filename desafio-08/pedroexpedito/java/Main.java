package desafio08;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    if (args.length <= 0) {
      System.out.println("Use: java Main <path/frac.txt>");
      System.exit(1);
    }

    String path = args[0];
    File file = new File(path);

    try {
      Scanner sc = new Scanner(file);
      while (sc.hasNextLine()) {
        String frac = sc.nextLine();
        System.out.println(Fracao.simplificar(frac));
      }
      sc.close();
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }
  }

  static class Fracao {
    int numerador;
    int denominador;

    static final int[] primes = {
      2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
      97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
      193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
      307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
      421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
      547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
      659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
      797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919,
      929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
    };

    public Fracao(String numerorador, String denominador) {
      this.numerador = Integer.parseInt(numerorador);
      this.denominador = Integer.parseInt(denominador);
    }

    boolean isImpropia() {
      return numerador > denominador ? true : false;
    }

    static String simplificar(Fracao fracao) {
      for (int prime : primes) {
        if (fracao.numerador % prime == 0 && fracao.denominador % prime == 0) {
          fracao.numerador /= prime;
          fracao.denominador /= prime;
          simplificar(fracao);
        }
      }
      if (fracao.numerador == fracao.denominador) {
        return fracao.numerador + "";
      }

      return fracao.numerador + "/" + fracao.denominador;
    }

    static String simplificar(String fracaoStr) {

      final String[] splitted = fracaoStr.split("/");

      if (splitted.length < 2) {
        return fracaoStr;
      }
      Fracao fracao1 = new Fracao(splitted[0], splitted[1]);

      if (fracao1.denominador == 0) {
        return "ERR";
      }

      if (fracao1.isImpropia()) {
        int result = fracao1.numerador / fracao1.denominador;
        int modulo = fracao1.numerador % fracao1.denominador;

        return modulo > 0 ? "" + result + " " + modulo + "/" + fracao1.denominador : result + "";

      } else {
        return simplificar(fracao1);
      }
    }
  }
}
