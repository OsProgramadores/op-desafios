package com.pedroexpedito.desafio05.gerentes;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import com.pedroexpedito.desafio05.models.Funcionario;

public class GerenteLastName {

	Map<String, LastNameData> mapMaioresSobrenome = new HashMap<>();

	public void push(Funcionario f) {
		LastNameData funcionarios = mapMaioresSobrenome.get(f.getSobrenome());
		if (funcionarios != null) {
			funcionarios.incremenetarFunarios();
			double salario = funcionarios.getFirstSalario();
			int cmp = Double.compare(f.getSalario(), salario);
			if (cmp == 0) {
				funcionarios.add(f);
			} else if (cmp > 0) {
				funcionarios.clear();
				funcionarios.add(f);
			}

		} else {
			LastNameData list = new LastNameData();
			list.incremenetarFunarios();
			list.add(f);
			mapMaioresSobrenome.put(f.getSobrenome(), list);
		}
	}

	public void printLastName() {
		mapMaioresSobrenome.entrySet().parallelStream().map((sobrenomeEntry) -> sobrenomeEntry.getValue())
				.filter(x -> x.size() >= 2).forEach((listFuncionario) -> {
					listFuncionario.getSet()
					.forEach((f) -> {
						System.out.printf("last_name_max|%s|%s %s|%.2f\n",
						f.getSobrenome(), f.getNome(),
						f.getSobrenome(), f.getSalario());
					});
				});
	}
	private class LastNameData {
		private int funcionarios = 0;
		private Set<Funcionario> set = new HashSet<Funcionario>();

		public void incremenetarFunarios() {
			funcionarios++;
		}
		public void add(Funcionario f) {
			set.add(f);
		}

		public void clear() {
			set.clear();
		}

		public double getFirstSalario() {
			return set.iterator().next().getSalario();
		}

		public int size() {
			return funcionarios;
		}

		public Set<Funcionario> getSet() {
			return set;
		}
	}
}
