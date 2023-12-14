package Polimorfismo;

public class mamiferos extends animal {

    public mamiferos(String nome, String cor) {
        super(nome, cor);
    }
    
    public void mamar() {
        System.out.println("Esta mamando");
    }
}
