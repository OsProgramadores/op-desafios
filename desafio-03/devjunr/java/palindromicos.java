public class palindromicos{
 public static void main(String[]args){
 	int valorInicial = Integer.parseInt(args[0]);
	int valorFinal = Integer.parseInt(args[1]);
	if (args.length<2) {
		System.out.println("Forneça dois valores positivos como argumentos no momento da execução");
	}else if(valorInicial<0 || valorFinal <0){
		System.out.println("Os valores dos argumentos devem ser positivos");
	}else {
		System.out.println("_".repeat(15)+"\n"+"Valor Inicial: "+valorInicial+"\n"+"Valor Final: "+valorFinal+"\n"+"_".repeat(10));
		tratamentoDosValores(valorInicial, valorFinal);
		}
	}
private static void tratamentoDosValores(int valorInicial, int valorFinal){
	System.out.println("Resultado: ");
	for(int i=valorInicial;i<=valorFinal;i++){
		String numero = Integer.toString(i);
		String reversed = new StringBuilder(numero).reverse().toString();
			if (reversed.equals(numero)) {
				System.out.println(numero);
			}
		}
	}
}