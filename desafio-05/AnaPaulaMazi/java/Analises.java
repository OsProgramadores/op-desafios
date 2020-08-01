package desafio05;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Analises {

	private List<Funcionarios> funcionariosList;
	private Map<String, String> areasMap = new HashMap<>();
	private Map<String, List<Funcionarios>> funcionariosArea;
	private Map<String, List<Funcionarios>> funcionariosSobrenome;

	public Analises(List<Funcionarios> funcionariosList, List<Areas> areasList) {
		this.funcionariosList = funcionariosList;
		areasList.forEach(a -> areasMap.put(a.getCodigo(), a.getNome()));
		funcionariosArea = funcionariosList.stream().collect(Collectors.groupingBy(Funcionarios::getArea));
		funcionariosSobrenome = funcionariosList.stream().collect(Collectors.groupingBy(Funcionarios::getSobrenome));

	}

	public void salariosGlobais() {

		Double maxSalario = funcionariosList.stream().mapToDouble(f -> f.getSalario()).max().getAsDouble();

		Double minSalario = funcionariosList.stream().mapToDouble(f -> f.getSalario()).min().getAsDouble();

		Double avSalario = funcionariosList.stream().collect(Collectors.averagingDouble(f -> f.getSalario()));

		funcionariosList.stream().filter(f -> (f.getSalario().equals(maxSalario)))
				.forEach(f -> System.out.printf("global_max|%s|%.2f\n", f.toString(), f.getSalario()));
		funcionariosList.stream().filter(f -> (f.getSalario().equals(minSalario)))
				.forEach(f -> System.out.printf("global_min|%s|%.2f\n", f, f.getSalario()));
		System.out.printf("global_avg|%.2f\n", avSalario);

	}

	public void salariosAreas() {
		funcionariosArea.entrySet().stream().map(areas -> areas.getValue()).collect(Collectors.toList())
				.forEach((funcionarios) -> {

					Double maxArea = funcionarios.stream().mapToDouble(a -> a.getSalario()).max().getAsDouble();
					Double minArea = funcionarios.stream().mapToDouble(a -> a.getSalario()).min().getAsDouble();

					Double avArea = funcionarios.stream().collect(Collectors.averagingDouble(f -> f.getSalario()));

					funcionarios.stream().filter(f -> f.getSalario().equals(maxArea)).forEach(f -> System.out
							.printf("Area_max|%s|%s|%.2f\n", areasMap.get(f.getArea()), f, f.getSalario()));
					funcionarios.stream().filter(f -> f.getSalario().equals(minArea)).forEach(f -> System.out
							.printf("Area_min|%s|%s|%.2f\n", areasMap.get(f.getArea()), f, f.getSalario()));
					System.out.printf("area_avg|%s|%.2f\n", areasMap.get(funcionarios.get(0).getArea()), avArea);

				});

	}

	public void quantidadeFuncionarioArea() {

		Integer max = funcionariosArea.entrySet().stream().mapToInt(areas -> areas.getValue().size()).max().getAsInt();
		Integer min = funcionariosArea.entrySet().stream().mapToInt(areas -> areas.getValue().size()).min().getAsInt();

		funcionariosArea.entrySet().stream().filter(area -> (area.getValue().size() == min)).forEach(area -> System.out
				.printf("least_employess|%s|%d\n", areasMap.get(area.getKey()), area.getValue().size()));
		funcionariosArea.entrySet().stream().filter(area -> (area.getValue().size() == max)).forEach(area -> System.out
				.printf("most_employees|%s|%d\n", areasMap.get(area.getKey()), area.getValue().size()));

	}

	public void salariosSobrenome() {

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
