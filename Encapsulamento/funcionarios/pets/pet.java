package Encapsulamento.funcionarios.pets;

public class pet {

    // Campos
    private String nome;
    private String animal;
    private int idade;

    // Construtor padrão
    public pet() {
    }

    // Construtor com parâmetros
    public pet(String nome, String animal, int idade) {
        this.nome = nome;
        this.animal = animal;
        this.idade = idade;
    }

    // Métodos Setters
    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setAnimal(String animal) {
        this.animal = animal;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    // Métodos Getters
    public String getNome() {
        return nome;
    }

    public String getAnimal() {
        return animal;
    }

    public int getIdade() {
        return idade;
    }
  
}
