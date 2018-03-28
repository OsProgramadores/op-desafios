

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import models.Area;
import models.Funcionario;

/**
 *
 * @author Maykon Oliveira
 */
public class Manager {
    private final List<Funcionario> funcionariosList;
    private Map<String, String> areasMap = new HashMap<>();       
    private final Map<String, List<Funcionario>> funcionariosByArea;
    private final Map<String, List<Funcionario>> funcionariosBySobrenome;

    public Manager(List<Funcionario> funcionariosList, List<Area> areasList) {
        this.funcionariosList = funcionariosList;
        areasList.forEach(a -> areasMap.put(a.getCodigo(), a.getNome()));
        funcionariosByArea = funcionariosList.stream().collect(Collectors.groupingBy(Funcionario::getArea));
        funcionariosBySobrenome = funcionariosList.stream().collect(Collectors.groupingBy(Funcionario::getSobrenome));
    }

    public void salariosGlobais() {
        Double maxOfSalary = funcionariosList.stream().mapToDouble(Funcionario::getSalario).max().getAsDouble();
        Double minOfSalary = funcionariosList.stream().mapToDouble(Funcionario::getSalario).min().getAsDouble();
        Double avgOfSalary = funcionariosList.stream().mapToDouble(Funcionario::getSalario).average().getAsDouble();
        
        funcionariosList.stream().filter(f -> (f.getSalario().equals(maxOfSalary))).forEach(f -> System.out.printf("global_max|%s|%.2f\n", f, f.getSalario()));
        funcionariosList.stream().filter(f -> (f.getSalario().equals(minOfSalary))).forEach(f -> System.out.printf("global_min|%s|%.2f\n", f, f.getSalario()));
        System.out.printf("global_avg|%.2f\n", avgOfSalary);
    }
    
    public void salariosPorArea() {
        funcionariosByArea.entrySet().stream().map((area) -> { return area.getValue(); }
        ).forEach((funcionarios) -> {
            Double maxOfSalary = funcionarios.stream().mapToDouble(Funcionario::getSalario).max().getAsDouble();
            Double minOfSalary = funcionarios.stream().mapToDouble(Funcionario::getSalario).min().getAsDouble();
            Double avgOfSalary = funcionarios.stream().mapToDouble(Funcionario::getSalario).average().getAsDouble();
            
            funcionarios.stream().filter(f -> (f.getSalario().equals(maxOfSalary))).forEach(f -> System.out.printf("area_max|%s|%s|%.2f\n", areasMap.get(f.getArea()), f, f.getSalario()));
            funcionarios.stream().filter(f -> (f.getSalario().equals(minOfSalary))).forEach(f -> System.out.printf("area_min|%s|%s|%.2f\n", areasMap.get(f.getArea()), f, f.getSalario()));
            System.out.printf("area_avg|%s|%.2f\n", areasMap.get(funcionarios.get(0).getArea()), avgOfSalary);
        });
    }
    
    public void numeroFuncionarioPorArea() {
        Integer max = funcionariosByArea.entrySet().stream().mapToInt(area -> area.getValue().size()).max().getAsInt();
        Integer min = funcionariosByArea.entrySet().stream().mapToInt(area -> area.getValue().size()).min().getAsInt();
        
        funcionariosByArea.entrySet().stream().filter(area -> (area.getValue().size() == max)).forEach(area -> System.out.printf("most_employees|%s|%d\n", areasMap.get(area.getKey()), area.getValue().size()));
        funcionariosByArea.entrySet().stream().filter(area -> (area.getValue().size() == min)).forEach(area -> System.out.printf("least_employees|%s|%d\n", areasMap.get(area.getKey()), area.getValue().size()));
    }
    
    public void salariosMesmoSobrenome() {
        Map<String, List<Funcionario>> mapMaioresSobrenome = new HashMap<>();
        
        funcionariosBySobrenome.entrySet().forEach((sobrenomeEntry) -> {
            if (sobrenomeEntry.getValue().size() > 1) {
                mapMaioresSobrenome.put(sobrenomeEntry.getKey(), sobrenomeEntry.getValue());
            }
        });
        
        mapMaioresSobrenome.entrySet().stream().map((sobrenomeEntry) -> sobrenomeEntry.getValue()
        ).forEach((listFuncionario) -> {
            Double maxOfSalary = listFuncionario.stream().mapToDouble(Funcionario::getSalario).max().getAsDouble();
            listFuncionario.stream().filter(f -> (f.getSalario().equals(maxOfSalary))).forEach(f -> System.out.printf("last_name_max|%s|%s|%.2f\n", f.getSobrenome(), f, f.getSalario()));
        });
    }
}
