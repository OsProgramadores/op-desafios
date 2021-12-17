package com.pedroexpedito.desafio05.gerentes;

import java.util.HashSet;
import java.util.Set;

import com.pedroexpedito.desafio05.models.Area;
import com.pedroexpedito.desafio05.models.Funcionario;

public class GerenteEmployees {

	Set<EmployeesData> Areas = new HashSet<EmployeesData>();
	Set<EmployeesData> most = new HashSet<EmployeesData>();
	Set<EmployeesData> least = new HashSet<EmployeesData>();

	long most_employees = Long.MIN_VALUE;
	long least_employess = Long.MAX_VALUE;

	public void print_employees() {
		push_least();
		push_most();
		for (EmployeesData eD : most ) {
			System.out.printf("most_employees|%s|%d\n", eD.getAreaNome(), eD.getFuncionarios());
		}
		for (EmployeesData eD : least ) {
			System.out.printf("least_employees|%s|%d\n", eD.getAreaNome(), eD.getFuncionarios());
		}
	}

	void push_most() {
		for (EmployeesData employeesData : Areas) {
			if(employeesData.getFuncionarios() > most_employees) {
				most_employees = employeesData.getFuncionarios();
				most.clear();
				most.add(employeesData);
			} else if (Long.compare(most_employees, employeesData.getFuncionarios()) == 0) {
				most.add(employeesData);
			}
		}
	}
	void push_least() {
		for (EmployeesData employeesData : Areas) {
			if(employeesData.getFuncionarios() < least_employess) {
				least_employess = employeesData.getFuncionarios();
				least.clear();
				least.add(employeesData);
			} else if (Long.compare(most_employees, employeesData.getFuncionarios()) == 0) {
				least.add(employeesData);
			}
		}
	}

	void push(Funcionario f) {
		for (EmployeesData employeesData : Areas ) {
			if(employeesData.getAreaCode().equals(f.getArea())) {
				employeesData.incrementarFuncionarios();
				return;
			}
		}
		EmployeesData employeesData = new EmployeesData(f.getArea());
		employeesData.incrementarFuncionarios();
		Areas.add(employeesData);
	}

	void push(Area area) {
		for (EmployeesData employeesData : Areas ) {
			if(employeesData.getAreaCode().equals(area.getCodigo())) {
				employeesData.setAreaNome(area.getNome());;
				return;
			}
		}
	}

	private class EmployeesData {
		private long funcionarios = 0;
		private String areaNome;
		private String areaCode;

		public long getFuncionarios() {
			return funcionarios;
		}

		public EmployeesData(String areaCode) {
			this.areaCode = areaCode;
		}

		public String getAreaCode() {
			return areaCode;
		}
		public String getAreaNome() {
			return areaNome;
		}

		public void setAreaNome(String areaName) {
			this.areaNome = areaName;
		}

		public void incrementarFuncionarios() {
			funcionarios++;
		}

	}



}
