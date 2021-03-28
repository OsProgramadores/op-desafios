package atividade.expressao;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.LineNumberReader;
import java.util.LinkedList;
import java.util.Queue;

import atividade.expressao.dependencias.Eval;
import atividade.expressao.dependencias.excessao.SyntaxErrorExpression;

public class Expressao {
    public static void main(String[] args) throws IOException {
        // passa o caminho do arquivo
        expressao("./entradas_prog/d14.txt");
    }

    public static void expressao (String path) throws IOException{
        LineNumberReader leitor = new LineNumberReader(new FileReader(new File(path)));
        int c = 0;
        Queue<String> lista = new LinkedList<>();
        boolean first = true;
        String temp = "";
        // abaixo é adicionado as linhas na fila, isto é, as expressões -> 1 linha == 1 expressão
        while((c = leitor.read()) != -1) {
            if (first){
                temp = "" + (char)c;
                first = false; 
            } else if (c == '\n') {
                if (!temp.equals("\n")){
                    lista.add(temp);
                }
                first = true;
            } else if (!first && c != '\n') {
                temp += (char)c;
            }
        }
        leitor.close();
        do {
            try{
                System.out.println(Eval.calculadora(lista.poll()));
            } catch (SyntaxErrorExpression e) {
                System.out.println("ERR SYNTAX");
            } catch (ArithmeticException e) {
                System.out.println("ERR DIVBYZERO");
            }
        } while (!lista.isEmpty());
    }

    public static Queue<Integer> procura_element(char expressao[]) {
        Queue<Integer> fila = new LinkedList<>();
        int cont = 0;
        for (char c : expressao) {
            if (c == '^') {
                fila.add(cont);
            }
            cont++;
        }
        fila.add(00);
        return fila;
    }
}
