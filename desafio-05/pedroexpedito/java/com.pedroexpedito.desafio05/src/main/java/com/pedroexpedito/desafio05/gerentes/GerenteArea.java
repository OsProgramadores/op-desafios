package com.pedroexpedito.desafio05.gerentes;

import java.util.HashSet;
import java.util.Set;

import com.pedroexpedito.desafio05.models.Area;
import com.pedroexpedito.desafio05.models.Funcionario;

public class GerenteArea {
	
	static Set<AreaData> areasData = new HashSet<AreaData>();

	public void push(Funcionario f) {
		String areaCode = f.getArea();
		// verificando se existe area com esse codigo
		for (AreaData areaData : areasData) {
			if(areaData.areaCode.equals(areaCode)) {
				areaData.push(f);
				return; // se encontrar retorna
			}
		}
		AreaData areaData = new AreaData(areaCode);
		areaData.push(f);
		areasData.add(areaData);
	}
	public void push(Area area) {
		String areaCode = area.getCodigo();
		for (AreaData areaData : areasData) {
			if(areaData.areaCode.equals(areaCode)) {
				areaData.setAreaNome(area.getNome());
				return; 
			}
		}
	}
	
	public void print_areas() {
		for (AreaData areaData : areasData) {
			areaData.print_area();
		}
		
	}
	


	private class AreaData {
		public AreaData(String areaCode) {
			this.areaCode = areaCode;
		}

		String areaCode;
		String AreaNome;

		public String getAreaNome() {
			return AreaNome;
		}

		public void setAreaNome(String areaNome) {
			AreaNome = areaNome;
		}

		Set<Funcionario> f_area_max = new HashSet<Funcionario>();
		Set<Funcionario> f_area_min = new HashSet<Funcionario>();

		double area_max = Double.MIN_VALUE;
		double area_min = Double.MAX_VALUE;

		long funcionarios = 0;

		double soma_salarios_total = 0;
		
		public double get_area_avg() {
			return soma_salarios_total / funcionarios;
		}

		public void push(Funcionario f) {
			funcionarios++;
			soma_salarios_total += f.getSalario();

			push_area_max(f);
			push_area_min(f);
		}

		void push_area_max(Funcionario f) {
			if (area_max < f.getSalario()) {
				area_max = f.getSalario();
				f_area_max.clear();
				f_area_max.add(f);
			} else if (Double.compare(area_max, f.getSalario()) == 0) {
				f_area_max.add(f);
			}
		}
		void push_area_min(Funcionario f) {
			if (area_min > f.getSalario()) {
				area_min = f.getSalario();
				f_area_min.clear();
				f_area_min.add(f);
			} else if (Double.compare(area_min, f.getSalario()) == 0) {
				f_area_min.add(f);
			}
		}
		void print_area() {
			for (Funcionario f : f_area_max) {
				System.out.printf("area_max|%s|%s %s|%.2f\n", getAreaNome(), f.getNome(), f.getSobrenome(), f.getSalario());
			}
			
			for (Funcionario f : f_area_min) {
				System.out.printf("area_min|%s|%s %s|%.2f\n", getAreaNome(), f.getNome(), f.getSobrenome(), f.getSalario());

			}
			System.out.printf("area_avg|%s|%.2f\n",getAreaNome(), get_area_avg());
		}
		
		

	}

}
