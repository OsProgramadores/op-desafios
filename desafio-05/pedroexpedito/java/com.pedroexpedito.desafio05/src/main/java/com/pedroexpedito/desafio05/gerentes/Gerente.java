package com.pedroexpedito.desafio05.gerentes;

import com.pedroexpedito.desafio05.models.Area;
import com.pedroexpedito.desafio05.models.Funcionario;

public class Gerente {

  static GerenteArea gerenteArea = new GerenteArea();
  static GerenteEmployees gerenteEmployees = new GerenteEmployees();
  static GerenteLastName gerenteLastName = new GerenteLastName();
  static GerenteGlobal gerenteGlobal = new GerenteGlobal();

  public static void push(Funcionario f) {
    gerenteGlobal.push(f);
    gerenteArea.push(f);
    gerenteEmployees.push(f);
    gerenteLastName.push(f);
  }

  public static void push(Area a) {
    gerenteArea.push(a);
    gerenteEmployees.push(a);
  }

  public static void printAll() {
    gerenteLastName.printLastName();
    gerenteGlobal.print_global();
    gerenteGlobal = null;
    gerenteArea.print_areas();
    gerenteArea = null;
    gerenteEmployees.print_employees();
    gerenteEmployees = null;
  }
}
