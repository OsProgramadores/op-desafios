

import java.text.NumberFormat;
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
	NumberFormat formatter = Conversor.seuFormato();

	public Analises(List<Funcionarios> funcionariosList, List<Areas> areasList) {
		this.funcionariosList = funcionariosList;
		areasList.forEach(a -> areasMap.put(a.getCodigo(), a.getNome()));
		funcionariosArea = funcionariosList.parallelStream().collect(Collectors.groupingBy(Funcionarios::getArea));
		funcionariosSobrenome = funcionariosList.parallelStream().collect(Collectors.groupingBy(Funcionarios::getSobrenome));

	}

	public void salariosGlobais() {

		Optional<Funcionarios> maxSalario = funcionariosList.parallelStream()
				.collect(Collectors.maxBy(Comparator.comparingDouble(f -> f.getSalario())));

		Funcionarios maior = maxSalario.get();

		Optional<Funcionarios> minSalario = funcionariosList.parallelStream()
				.collect(Collectors.minBy(Comparator.comparingDouble(f -> f.getSalario())));

		Funcionarios menor = minSalario.get();

		Double avSalario = funcionariosList.parallelStream().collect(Collectors.averagingDouble(f -> f.getSalario()));

		funcionariosList.parallelStream().filter(f -> (f.getSalario().equals(maior.getSalario())))
				.forEach(f -> System.out.printf("global_max|%s|%s\n", f.toString(), formatter.format(f.getSalario())));
		funcionariosList.parallelStream().filter(f -> (f.getSalario().equals(menor.getSalario())))
				.forEach(f -> System.out.printf("global_min|%s|%s\n", f, formatter.format(f.getSalario())));
		System.out.printf("global_avg|%s\n",  formatter.format(avSalario));

	}

	public void salariosArea() {

		funcionariosArea.values().parallelStream().collect(Collectors.toList()).forEach((funcionarios) -> {

			Optional<Funcionarios> maxArea = funcionarios.parallelStream()
					.collect(Collectors.maxBy(Comparator.comparingDouble(f -> f.getSalario())));

			Funcionarios maiorArea = maxArea.get();

			Optional<Funcionarios> minArea = funcionarios.parallelStream()
					.collect(Collectors.minBy(Comparator.comparingDouble(f -> f.getSalario())));
					
			Funcionarios menorArea = minArea.get();

			Double avArea = funcionarios.parallelStream().collect(Collectors.averagingDouble(f -> f.getSalario()));

			funcionarios.parallelStream().filter(f -> (f.getSalario().equals(maiorArea.getSalario())))
					.forEach(f -> System.out.printf("area_max|%s|%s|%s\n", areasMap.get(f.getArea()), f, formatter.format(f.getSalario())));
			funcionarios.parallelStream().filter(f -> (f.getSalario().equals(menorArea.getSalario())))
					.forEach(f -> System.out.printf("area_min|%s|%s|%s\n", areasMap.get(f.getArea()), f, formatter.format(f.getSalario())));
			System.out.printf("area_avg|%s|%s\n", areasMap.get(funcionarios.get(0).getArea()),formatter.format(avArea));
			
			
		});
		
	}
	
	public void funcionariosArea() {
		

			
			Integer max = funcionariosArea.entrySet().parallelStream().mapToInt(areas -> areas.getValue().size()).max()
					.getAsInt();
			Integer min = funcionariosArea.entrySet().parallelStream().mapToInt(areas -> areas.getValue().size()).min()
					.getAsInt();

			funcionariosArea.entrySet().parallelStream().filter(area -> (area.getValue().size() == min))
					.forEach(area -> System.out.printf("least_employess|%s|%d\n", areasMap.get(area.getKey()),
							area.getValue().size()));
			funcionariosArea.entrySet().parallelStream().filter(area -> (area.getValue().size() == max))
					.forEach(area -> System.out.printf("most_employess|%s|%d\n", areasMap.get(area.getKey()),
							area.getValue().size()));

		

	}
		
		public void salarioSobrenome() {

			funcionariosSobrenome.entrySet().parallelStream().map(sobrenome -> sobrenome.getValue()).collect(Collectors.toList())

					.forEach((funcionarios) -> {
						if ((funcionarios.size() > 1)) {

							Double maxSobrenome = funcionarios.parallelStream().mapToDouble(s -> s.getSalario()).max()
									.getAsDouble();
							funcionarios.parallelStream().filter(f -> (f.getSalario().equals(maxSobrenome))).forEach(f -> System.out
									.printf("last_name_max|%s|%s|%s\n", f.getSobrenome(), f, formatter.format(f.getSalario())));

						}
					});

		}
		
		
		

	
	

	
	

}
