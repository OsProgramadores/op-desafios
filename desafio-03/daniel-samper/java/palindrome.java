package desafio_3;


public class palindrome {
	public static void main(String[] args) {
		int a = 1;
		int b = 2000;

		
		for (int i=a;i<=b;i++) {
			if((Integer.toString(i)).equals(new StringBuilder(Integer.toString(i)).reverse().toString())) {
				System.out.println(i);
			}

		}
	}	
			
}
