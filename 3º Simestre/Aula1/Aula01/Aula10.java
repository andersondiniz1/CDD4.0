package Aula01;

public class Aula10 {
    public static void main(String[] args) {

        int numero = 0;

        System.out.println("Numeros Pares: "); 
        while (numero <= 100){
            
            if (numero % 2 == 0){
                System.out.print(numero + " "); 
            }
            numero++;
        }
        numero = 0;

        System.out.println(" "); 
        System.out.println("Numeros ímpares: "); 
        while (numero <= 100){

            if (numero % 2 == 1) {
                System.out.print(numero + " "); 
            }
            numero++;
        }
    }
}
