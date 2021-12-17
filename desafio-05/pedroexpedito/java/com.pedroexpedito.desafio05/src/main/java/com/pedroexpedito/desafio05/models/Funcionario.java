package com.pedroexpedito.desafio05.models;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class Funcionario {
	private long id;
	@Expose
	@SerializedName("nome")
	private String nome;
	@Expose
	@SerializedName("sobrenome")
	private String sobrenome;
	@Expose
	@SerializedName("salario")
	private double salario;
	@Expose
	@SerializedName("area")
	private String area;

	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getSobrenome() {
		return sobrenome;
	}

	public void setSobrenome(String sobrenome) {
		this.sobrenome = sobrenome;
	}

	public double getSalario() {
		return salario;
	}

	public void setSalario(double salario) {
		this.salario = salario;
	}

	public String getArea() {
		return area;
	}

	public void setArea(String area) {
		this.area = area;
	}

	public Funcionario() {}


	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("id: " + id);
		sb.append(", nome: " + nome);
		sb.append(", sobrenome: " + sobrenome);
		sb.append(", salario: " + salario);
		sb.append(", area: " + area);

		return sb.toString();

	}
}
