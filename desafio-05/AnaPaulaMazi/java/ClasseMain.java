

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import com.google.gson.Gson;
import com.google.gson.stream.JsonReader;
import classes.*;





public class ClasseMain {
	

	public static void main(String[] args) throws IOException {

		try {

			List<Funcionarios> funcionariosList = new ArrayList<Funcionarios>();
			List<Areas> areasList = new ArrayList<Areas>();
			JsonReader reader;
			
			if(args.length > 0) {
				 reader = new JsonReader(new FileReader(args[0]));
			} else {
				reader =  new JsonReader(new FileReader("funcionarios.json"));
			}
			
		

			

			Gson gson = new Gson();

			InfoGerais geralObject = gson.fromJson(reader, InfoGerais.class);

			for (Funcionarios funcionario : geralObject.getFuncionarios()) {
				funcionariosList.add(funcionario);

			}

			for (Areas area : geralObject.getAreas()) {
				areasList.add(area);

			}

			Analises analise = new Analises(funcionariosList, areasList);
			analise.salarioSobrenome();
			analise.salariosGlobais();
			analise.salariosArea();
			analise.funcionariosArea();

			reader.close();
			

		} catch (FileNotFoundException e) {
			System.out.println("Erro ao abrir o arquivo.");
		}
	}
}
