package Polimorfismo;

public class vaca extends mamiferos {

    public vaca(String nome, String cor) {
        super(nome, cor);
    }
    
    public void som(){
        System.out.println("Muuuuuu!");
    }
}
