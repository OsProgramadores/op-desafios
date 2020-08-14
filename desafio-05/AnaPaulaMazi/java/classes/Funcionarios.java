package classes;

public class Funcionarios {
	private Integer id;
	private String nome;
	private String sobrenome;
	private Double salario;
	private String area;

	public Funcionarios(Integer id, String nome, String sobrenome, Double salario, String area) {
		this.id = id;
		this.nome = nome;
		this.sobrenome = sobrenome;
		this.salario = salario;
		this.area = area;
	}

	@Override
	public String toString() {
		return nome + " " + sobrenome;
	}

	public String getArea() {
		return area;
	}

	public void setArea(String area) {
		this.area = area;
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getSobrenome() {
		return sobrenome;
	}

	public void setSobrenome(String sobrenome) {
		this.sobrenome = sobrenome;
	}

	public Double getSalario() {
		return salario;
	}

	public void setSalario(Double salario) {
		this.salario = salario;
	}

}
