package Aula01.POO.Classe4;

public class Calculadora {

    public static void main(String[] args) {

        SomarMetodos conta = new SomarMetodos();
        int soma1 = conta.somar(5,2);
        int soma2 = conta.somar(5,2,8);
        double mult1 = conta.mult(5,2);
        double mult2 = conta.mult(5,2,8);

        System.out.println(soma1 + soma2);
        System.out.println(mult1 * mult2);

    }
}
