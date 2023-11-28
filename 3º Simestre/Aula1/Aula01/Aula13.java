package Aula01;

public class Aula13 {
    public static void main(String[] args) {

        for(int x = 1; x < 100; x++){

            if (x > 50 && x < 60) {
                    System.out.println("Numero encontrado");
                    break;
            }
            System.out.println(x);
            
        }
    }
}
