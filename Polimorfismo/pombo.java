package Polimorfismo;

public class pombo extends aves {

    public pombo(String nome, String cor) {
        super(nome, cor);
    }
       
    
    public void som(){
        System.out.println("Pruuuu Pruuuu!");
    }

    public void frente(){
        System.out.println("Voar para frente");
    }

    public void tras(){
        System.out.println("Voar para tras");
    }

    public void esquerda(){
        System.out.println("Voar para esquerda");
    }

    public void direita(){
        System.out.println("Voar para direita");
    }
}
