package Polimorfismo;

public class calculadora {

    public static void main(String[] args) {
        metodos i = new metodos();
        double calc1 = i.somar(2, 3);
        System.out.println(calc1);  

        metodos x = new metodos();
        double calc2 = x.somar(2, 3, 5);
        System.out.println(calc2);  
    }
}
