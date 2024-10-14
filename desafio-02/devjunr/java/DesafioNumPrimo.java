public class DesafioNumPrimo {
    public static void main(String[] args) {
        int quantMax = 10000;
        System.out.println("\n".repeat(2) + "Números primos de 1 a " + quantMax + "\n");
        while(true){
            for(int i=2; i<=quantMax; i++){
                int contador = 2;
				boolean isPrimo = true;
                while(isPrimo && contador < i){
                    if (i % contador == 0){
                        isPrimo = false;
                    }
                    else{
                        contador++;
                    }
                }
                if (isPrimo){
                    System.out.println(i);
                }
            }
            break;
        }
    }
}