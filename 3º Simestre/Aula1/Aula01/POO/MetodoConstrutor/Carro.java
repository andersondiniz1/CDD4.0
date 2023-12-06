package Aula01.POO.MetodoConstrutor;

public class Carro {

    String cor;
    Double preco;
    String modelo;

    // Constructor padrão.
    public Carro() {

    }
    
    // Constructor com 2 parametros.
    public Carro(String modelo, Double preco) {
        // Se for escolhido o construtor sem a cor do veiculo difinimos a cor como preta
        this.cor = "Preta";
        this.modelo = modelo;
        this.preco = preco;
    }

    // Constructor com 3 parametros.
    public Carro(String cor, String modelo, Double preco) {
        this.cor = cor;
        this.modelo = modelo;
        this.preco = preco;
    }

    public String cor() {
        return null;
    }
}
