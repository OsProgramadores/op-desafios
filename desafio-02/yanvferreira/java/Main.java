public class Main {

    public static boolean verificaPrimos(int numero){
        if (numero == 1){ //número 1 não é primo
            return false;
        }

        for (int divisor = 2; divisor < numero; divisor++){
            if (numero % divisor == 0){ //todo número é divisivel por ele mesmo, portanto, não precisa fazer essa operaçã. Caso a divisão pelo divisor seja zero, então não é
                return false;
            }
        }
        return true;
    }

 public static void main(String[] args) {


    int tamanhoDaLista = 10000;
    int numero = 1;

    while (numero <= tamanhoDaLista) {
        if (verificaPrimos(numero)){
            System.out.println(numero);
        }
        numero++;
    }
 }
}
