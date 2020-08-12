package desafio05;

import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;
import classes.*;


public class Analises {

	private final List<Funcionarios> funcionariosList;
	Map<String, String> areasMap = new HashMap<>();
	private final Map<String, List<Funcionarios>> funcionariosArea;
	private final Map<String, List<Funcionarios>> funcionariosSobrenome;

	public Analises(List<Funcionarios> funcionariosList, List<Areas> areasList) {
		this.funcionariosList = funcionariosList;
		areasList.forEach(a -> areasMap.put(a.getCodigo(), a.getNome()));
		funcionariosArea = funcionariosList.stream().collect(Collectors.groupingBy(Funcionarios::getArea));
		funcionariosSobrenome = funcionariosList.stream().collect(Collectors.groupingBy(Funcionarios::getSobrenome));

	}

	public void salariosGlobais() {

		Optional<Funcionarios> maxSalario = funcionariosList.stream()
				.collect(Collectors.maxBy(Comparator.comparingDouble(f -> f.getSalario())));

		Funcionarios maior = maxSalario.get();

		Optional<Funcionarios> minSalario = funcionariosList.stream()
				.collect(Collectors.minBy(Comparator.comparingDouble(f -> f.getSalario())));

		Funcionarios menor = minSalario.get();

		Double avSalario = funcionariosList.stream().collect(Collectors.averagingDouble(f -> f.getSalario()));

		funcionariosList.stream().filter(f -> (f.getSalario().equals(maior.getSalario())))
				.forEach(f -> System.out.printf("global_max|%s|%.2f\n", f.toString(), f.getSalario()));
		funcionariosList.stream().filter(f -> (f.getSalario().equals(menor.getSalario())))
				.forEach(f -> System.out.printf("global_min|%s|%.2f\n", f, f.getSalario()));
		System.out.printf("global_avg|%.2f\n",  avSalario);

	}

	public void salariosArea() {

		funcionariosArea.values().stream().collect(Collectors.toList()).forEach((funcionarios) -> {

			Optional<Funcionarios> maxArea = funcionarios.stream()
					.collect(Collectors.maxBy(Comparator.comparingDouble(f -> f.getSalario())));

			Funcionarios maiorArea = maxArea.get();

			Optional<Funcionarios> minArea = funcionarios.stream()
					.collect(Collectors.minBy(Comparator.comparingDouble(f -> f.getSalario())));

			Funcionarios menorArea = minArea.get();

			Double avArea = funcionarios.stream().collect(Collectors.averagingDouble(f -> f.getSalario()));

			funcionarios.stream().filter(f -> (f.getSalario().equals(maiorArea.getSalario())))
					.forEach(f -> System.out.printf("area_max|%s|%s|%.2f\n", areasMap.get(f.getArea()), f, f.getSalario()));
			funcionarios.stream().filter(f -> (f.getSalario().equals(menorArea.getSalario())))
					.forEach(f -> System.out.printf("area_min|%s|%s|%.2f\n", areasMap.get(f.getArea()), f, f.getSalario()));
			System.out.printf("area_avg|%s|%.2f\n", areasMap.get(funcionarios.get(0).getArea()),avArea);
			
			
		});
		
	}
	
	public void funcionariosArea() {
		

			
			Integer max = funcionariosArea.entrySet().stream().mapToInt(areas -> areas.getValue().size()).max()
					.getAsInt();
			Integer min = funcionariosArea.entrySet().stream().mapToInt(areas -> areas.getValue().size()).min()
					.getAsInt();

			funcionariosArea.entrySet().stream().filter(area -> (area.getValue().size() == min))
					.forEach(area -> System.out.printf("least_employess|%s|%d\n", areasMap.get(area.getKey()),
							area.getValue().size()));
			funcionariosArea.entrySet().stream().filter(area -> (area.getValue().size() == max))
					.forEach(area -> System.out.printf("most_employees|%s|%d\n", areasMap.get(area.getKey()),
							area.getValue().size()));

		

	}
		
		public void salarioSobrenome() {

			funcionariosSobrenome.entrySet().stream().map(sobrenome -> sobrenome.getValue()).collect(Collectors.toList())

					.forEach((funcionarios) -> {
						if ((funcionarios.size() > 1)) {

							Double maxSobrenome = funcionarios.stream().mapToDouble(s -> s.getSalario()).max()
									.getAsDouble();
							funcionarios.stream().filter(f -> (f.getSalario().equals(maxSobrenome))).forEach(f -> System.out
									.printf("last_name_max|%s|%s|%.2f\n", f.getSobrenome(), f, f.getSalario()));

						}
					});

		}
		
		
		

	
	

	
	

}
