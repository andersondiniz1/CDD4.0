package Polimorfismo;

public class aves extends animal {

    public aves(String nome, String cor) {
        super(nome, cor);
    }
    public void voa() {
        System.out.println("Esta voando.");
    }
}
