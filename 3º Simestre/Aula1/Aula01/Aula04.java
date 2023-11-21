package Aula01;

public class Aula04 {
    
    public static void main(String[] args) {

        int a = 3;
        int b = 4;
        int c = 7;

        System.out.println((a + b) / c); // 1
        System.out.println(!((a > b) && (a < c))); 
        //                      f          v
        //                         !(f) = True

        if(a++ >= b)
            System.out.println(--c);
        else
            System.out.println(c++);
    }   
}
