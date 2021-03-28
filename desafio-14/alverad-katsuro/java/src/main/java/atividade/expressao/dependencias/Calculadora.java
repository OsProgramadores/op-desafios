//Classe pertencente ao pacote "classes"
package atividade.expressao.dependencias;
//Importando a função raiz quadrada
import java.lang.Math;

public class Calculadora {

    // Construtor para o uso da calculadora elementar
    private Calculadora(){}

    // Está função tem a responsabilidade de realizar as somas
    public static double soma(double a, double b){
        return (a+b);
    }
    
    // Está função tem a responsabilidade de realizar as subtrações
    public static double subtracao(double a, double b){
        return (a-b);
    }

    // Está função tem a responsabilidade de realizar e retornar os valores da divisão
    public static double divisao(double a, double b){
        if (b == 0){
            throw new ArithmeticException();
        } else {
            return (a/b);
        }
    }

    // Está função tem a responsabilidade retorna o resto da divisão
    public static double resto(double a, double b){
        return (a%b);
    }
    
    // Está função tem a responsabilidade retorna o resultado da multiplicação
    public static double multiplicacao(double a, double b){
        return (a*b);
    }

    // Aqui temos o metodo responsavel pela potencia
    public static double exponenciacao(double a, double b){
        // Realiza a exponenciacao --> importado da biblioteca Math
        return Math.pow(a, b);
    }
}
