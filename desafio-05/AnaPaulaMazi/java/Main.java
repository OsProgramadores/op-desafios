package desafio05;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.stream.JsonReader;

public class Main {

	public static void main(String[] args) {

		try {

			List<Funcionarios> funcionariosList = new ArrayList<Funcionarios>();
			List<Areas> areasList = new ArrayList<Areas>();

			JsonReader reader = new JsonReader(
					new FileReader("Funcionarios.json"));

			Gson gson = new Gson();

			InfoGerais geralObject = gson.fromJson(reader, InfoGerais.class);

			for (Funcionarios funcionario : geralObject.getFuncionarios()) {
				funcionariosList.add(funcionario);
			
				

			}

			for (Areas area : geralObject.getAreas()) {
				areasList.add(area);
				
			}

			Analises analises = new Analises(funcionariosList, areasList);
			analises.salariosGlobais();
			analises.salariosAreas();
			analises.quantidadeFuncionarioArea();
			analises.salariosSobrenome();

		} catch (FileNotFoundException e) {
			System.out.println("Erro ao abrir o arquivo.");
		}

	}

}
