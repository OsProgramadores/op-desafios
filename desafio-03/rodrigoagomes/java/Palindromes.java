import java.util.ArrayList;
import java.util.List;

public class Palindromes {

	public static void main(String[] args) {
		boolean hasError = false;
		
		if(args.length != 2) {
			System.out.println("Deve informar os range de valores (inicial e final)");
			hasError = true;
		} 
		
		long start = 0L;
		long end = 0L;
		
		try {
			start = Long.parseLong(args[0]);
			end = Long.parseLong(args[1]);
		} catch (Exception e) {
			//SILENCE
			System.out.println("Os valores informados devem ser números inteiros positivos entre 1 e " + Long.MAX_VALUE);
			hasError = true;
		}
		
		if (start < 0 || end < 0) {
			System.out.println("Os valores informados devem ser números inteiros positivos entre 1 e " + Long.MAX_VALUE);	
			hasError = true;
		}
		
		if (start > end) {
			System.out.println("O valor inicial não pode ser maior que o valor final");
			hasError = true;
		}
		
		if (!hasError) {
			List<Long> palindromeList = new ArrayList<Long>();
			for (long i = start; i <= end; i++) {
				if (isPalindromeComparingChar(i)) {
					palindromeList.add(i);
				}
			}
			
			System.out.println(palindromeList);
		}
	}
	
	public static boolean isPalindromeComparingChar(long number) {
		boolean isPalindrome = true;
		String numberStr = String.valueOf(number);

		char[] characters =  numberStr.toCharArray();
		int arrayLength = characters.length;
		for (int i = 0; i < arrayLength / 2; i++) {
			char a = characters[i];
			char b = characters[arrayLength -1 -i];
			
			isPalindrome &= a == b; 
			
			if(!isPalindrome) {
				break;
			}
		}
		
		return isPalindrome;
	}
	
	//Another way to compare if is palindrome or not. Reversing the string and comparing the two texts (original and reversed)
	public static boolean isPalindromeReverseString(long number) {
		boolean isPalindrome = true;
		String numberStr = String.valueOf(number);
		String reverse = new StringBuilder().append(numberStr).reverse().toString();
		isPalindrome = numberStr.equals(reverse);
		return isPalindrome;
	}
}
