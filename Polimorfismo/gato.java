package Polimorfismo;

public class gato extends mamiferos {

    public gato(String nome, String cor) {
        super(nome, cor);
    }

    public void mamar() {
        System.out.println("mamar");
    }

    public void som(){
        System.out.println("Miauuuuuuuuu");
    }
}
