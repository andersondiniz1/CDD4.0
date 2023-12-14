// Permite que o desenvolvedor use o mesmo elemento de formas diferentes. "Muitas formas"

package Polimorfismo;

public class animal {
    
    public String nome;
    public String cor;

    public animal(String nome, String cor) {
        this.nome = nome;
        this.cor = cor;
    }
    
    public void som(){
        System.out.println("Efeito sonoro.");
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
