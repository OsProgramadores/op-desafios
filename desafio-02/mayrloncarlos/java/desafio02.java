package teste;

import java.util.Scanner;

public class desafio02 {

	public static void main(String[] args) {
		
		int n = 1;
		   int nDivisores = 0;

		  while(n <= 10000){
		    for(int i=1;i<=n;i++){
		      if(n % i == 0){
		        nDivisores++;
		      }
		    }
		    if(nDivisores == 2){
		        System.out.println(n + " é primo");
		      }
		    nDivisores = 0;
		    n++;
		  }
	}
}
