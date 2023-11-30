package Aula01;

public class Aula19 {

    public static void main(String[] args) {

        // int[] intArray = {2, 5};
        // int[] a = new int[2];
        // double[] b = new double[2];
        // int[] c;
        // d = new int[4];

        int[] intArray = {2, 5, 46, 12, 34};

        for(int i = 0; i < intArray.length; i++){ // .lenght vai trazer o tamanho do array
            System.out.print(intArray[i]); //Resultado 25461234
        }
        
        System.out.println();

        for(int x = intArray.length - 1; x >= 0; x--){ // .lenght vai trazer o tamanho do array
            System.out.print(intArray[x]); //Resultado 34124625
        }
    }
}
