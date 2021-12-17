package com.pedroexpedito.desafio05.gerentes;

import java.util.HashSet;
import java.util.Set;

import com.pedroexpedito.desafio05.models.Funcionario;

public class GerenteGlobal {

	private Set<Funcionario> f_global_max = new HashSet<Funcionario>();
	private Set<Funcionario> f_global_min = new HashSet<Funcionario>();

	private double global_max = Double.MIN_VALUE;
	private double global_min = Double.MAX_VALUE;

	private long funcionarios = 0;
	private double soma_salarios_total = 0;

	private double get_global_avg() {
		return soma_salarios_total / funcionarios;
	}

	public void print_global() {
		for (Funcionario f : f_global_max) {
			System.out.printf("global_max|%s %s|%.2f\n", f.getNome(), f.getSobrenome(), f.getSalario());
		}

		for (Funcionario f : f_global_min) {
			System.out.printf("global_min|%s %s|%.2f\n", f.getNome(), f.getSobrenome(), f.getSalario());

		}
		if(!f_global_max.isEmpty()) {
			System.out.printf("global_avg|%.2f\n", get_global_avg());
		}
	}

	public void push(Funcionario f) {
		funcionarios++;
		soma_salarios_total += f.getSalario();

		push_global_max(f);
		push_global_min(f);

	}
	private void push_global_max(Funcionario f) {

		if (global_max < f.getSalario()) {
			global_max = f.getSalario();
			f_global_max.clear();
			f_global_max.add(f);
		} else if (Double.compare(global_max, f.getSalario()) == 0) {
			f_global_max.add(f);
		}
	}
	private void push_global_min(Funcionario f) {

		if (global_min > f.getSalario()) {
			global_min = f.getSalario();
			f_global_min.clear();
			f_global_min.add(f);
		} else if (Double.compare(global_min, f.getSalario()) == 0) {
			f_global_min.add(f);
		}
	}


}