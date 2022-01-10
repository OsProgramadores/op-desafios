package com.pedroexpedito.desafio05.models;

import com.google.gson.annotations.Expose;

public class Area {
  @Expose private String codigo;
  @Expose private String nome;

  public Area() {}

  public String getCodigo() {
    return codigo;
  }

  public void setCodigo(String codigo) {
    this.codigo = codigo;
  }

  public String getNome() {
    return nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }
}
