public class palindromicos {
   public static void main(String[] args) {
        try {
            int valorInicial = Integer.parseInt(args[0]);
            int valorFinal = Integer.parseInt(args[1]);
            if (valorInicial > 0 & valorFinal > 0) {
                System.out.println("_".repeat(15)+"\nValor Inicial: " + valorInicial+"\nValor Final: " + valorFinal+"\n"+"_".repeat(15));
                tratamentoDosValores(valorInicial,valorFinal);
            }else if (valorInicial <= 0 || valorFinal <= 0) {
                System.out.println("São aceitos apenas valores positivos");
            }
        } catch (NumberFormatException e) {
            System.out.println("Apenas números inteiros são aceitos");
        } catch (ArrayIndexOutOfBoundsException e){
            System.out.println("É necessário pelo menos dois valores inteiros como argumento");
        }
    }

   public static void tratamentoDosValores(int valorInicial, int valorFinal){
        for(int i = valorInicial;i<=valorFinal;i++){
            String numero = Integer.toString(i);
            String reversed = new StringBuilder(numero).reverse().toString();
            if (reversed.equals(numero)) {
                System.out.println(numero);
            }
        }
    }
}
