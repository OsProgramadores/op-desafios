package com.pedroexpedito.desafio05;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

import com.google.gson.Gson;
import com.google.gson.stream.JsonReader;
import com.pedroexpedito.desafio05.gerentes.Gerente;
import com.pedroexpedito.desafio05.models.Area;
import com.pedroexpedito.desafio05.models.Funcionario;

public class Main {
	public static void main(String[] args) {

		if(args.length <= 0) {
			System.out.println("Use: java -jar desafio-05 <path>");
			System.exit(1);
		}

		try {
			String path = args[0];
			InputStream inputStream = new FileInputStream(path);
			
			readJsonStream(inputStream);

			Gerente.printAll();
		} catch (FileNotFoundException e) {
			System.err.println("Arquivo não encontrado: " + e.getMessage());
		} catch (IOException e) {
			System.err.println("Erro inesperado: " + e.getMessage());
		}

	}

	static public void readJsonStream(InputStream in) throws IOException {
		Gson gson = new Gson();
		JsonReader reader = new JsonReader(new InputStreamReader(in, "UTF-8"));

		// lendo funcionarios
		reader.beginObject();
		reader.nextName();
		reader.beginArray();
		while(reader.hasNext()) {
			Funcionario funcionario = gson.fromJson(reader, Funcionario.class);
			Gerente.push(funcionario);
		}
		// lendo areas
		reader.endArray();
		reader.nextName();
		reader.beginArray();
		while(reader.hasNext()) {
			Area area = gson.fromJson(reader, Area.class);
			Gerente.push(area);
		}
		reader.endArray();
		reader.close();
		
	}

}
