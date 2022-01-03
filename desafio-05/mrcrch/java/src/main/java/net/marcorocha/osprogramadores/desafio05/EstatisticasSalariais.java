package net.marcorocha.osprogramadores.desafio05;

import java.util.Collection;
import java.util.LinkedList;

class EstatisticasSalariais {

  private final String codigo;
  private String nome;

  private double maiorSalario = Double.MIN_VALUE;
  private double menorSalario = Double.MAX_VALUE;
  private double totalSalarios = 0;
  private int totalFuncionarios = 0;

  private final Collection<String> funcionariosMaiorSalario = new LinkedList<>();
  private final Collection<String> funcionariosMenorSalario = new LinkedList<>();

  EstatisticasSalariais(String codigo) {
    this.codigo = codigo;
    this.nome = "";
  }

  public String getCodigo() {
    return codigo;
  }

  public String getNome() {
    return nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public double getMaiorSalario() {
    return maiorSalario;
  }

  public void setMaiorSalario(double maiorSalario) {
    this.maiorSalario = maiorSalario;
  }

  public double getMenorSalario() {
    return menorSalario;
  }

  public void setMenorSalario(double menorSalario) {
    this.menorSalario = menorSalario;
  }

  public double getTotalSalarios() {
    return totalSalarios;
  }

  public void setTotalSalarios(double totalSalarios) {
    this.totalSalarios = totalSalarios;
  }

  public int getTotalFuncionarios() {
    return totalFuncionarios;
  }

  public void setTotalFuncionarios(int totalFuncionarios) {
    this.totalFuncionarios = totalFuncionarios;
  }

  public Collection<String> getFuncionariosMaiorSalario() {
    return funcionariosMaiorSalario;
  }

  public Collection<String> getFuncionariosMenorSalario() {
    return funcionariosMenorSalario;
  }

  public double getMediaSalarial() {
    return totalSalarios / totalFuncionarios;
  }

  void adicionar(double salario, String nome, String sobrenome) {

    totalSalarios += salario;
    totalFuncionarios++;

    if (salario <= menorSalario) {

      if (salario < menorSalario) {
        funcionariosMenorSalario.clear();
        menorSalario = salario;
      }

      funcionariosMenorSalario.add(nome + " " + sobrenome);
    }

    if (salario >= maiorSalario) {

      if (salario > maiorSalario) {
        funcionariosMaiorSalario.clear();
        maiorSalario = salario;
      }

      funcionariosMaiorSalario.add(nome + " " + sobrenome);
    }
  }

  @Override
  public int hashCode() {
    final int prime = 31;
    int result = 1;
    result = prime * result + (codigo == null ? 0 : codigo.hashCode());
    return result;
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj) {
      return true;
    }
    if (obj == null) {
      return false;
    }
    if (getClass() != obj.getClass()) {
      return false;
    }
    final EstatisticasSalariais other = (EstatisticasSalariais) obj;
    if (codigo == null) {
      if (other.codigo != null) {
        return false;
      }
    } else if (!codigo.equals(other.codigo)) {
      return false;
    }
    return true;
  }
}
