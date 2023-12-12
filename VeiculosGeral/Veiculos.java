package VeiculosGeral;

public class Veiculos {
   
    public String nome;
    public String cor;
    double preco;
    

    public Veiculos(String nome, String cor, double preco) {
        this.nome = nome;
        this.cor = cor;
        this.preco = preco;
    }

    public void locomover(){
        System.out.println("Andou");
    }
}
