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

    public void frente(){
        System.out.println("Mover para frente");
    }

    public void tras(){
        System.out.println("Mover para tras");
    }

    public void esquerda(){
        System.out.println("Mover para esquerda");
    }

    public void direita(){
        System.out.println("Mover para direita");
    }
}
