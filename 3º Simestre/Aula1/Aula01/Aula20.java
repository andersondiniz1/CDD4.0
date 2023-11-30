package Aula01;

public class Aula20 {
    
    public static void main(String[] args) {

        int[] arrayUM = {1,2,3,4,5,6,7,8,9,10};
        int[] arrayDOIS = {1,2,3,4,5};

        if(arrayDOIS.length >= 5){
            System.out.println("Array Dois é maior que 5");
        } else {
            System.out.println("Array Dois é menor ou igua que 5");
        }

        System.out.println("\n Tamando do ArrayUM = " + arrayUM.length);
    }
}
