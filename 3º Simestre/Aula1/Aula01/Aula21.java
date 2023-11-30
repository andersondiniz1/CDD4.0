package Aula01;

public class Aula21 {

    public static void main(String[] args) {
    
        int[] arrayNum = {1,2,3,4,5,6,7,8,9,10};
        int total = 0;

        // Adiciona o valor de cada elemento ao total
        for(int i : arrayNum){
        total += 1;
        }

        System.out.printf("Total de aelementos arrayNum: %d\n", total);
        
    
    }
    
}
