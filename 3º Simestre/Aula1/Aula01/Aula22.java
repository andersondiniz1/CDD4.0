package Aula01;

import java.util.Scanner;

public class Aula22 {

    public static void main(String[] args) {
    
        Scanner input = new Scanner(System.in);

        int[] arrayNum = new int[10];
        int[] arrayDois = new int[10];
        int[] arrayTres = new int[10];
        int[] arrayQuatro = new int[10];

        for(int i = 0; i < arrayNum.length; i++){
            System.out.println("Digite o " + (i + 1) +"º numero da 1º array: " );;
            arrayNum[i] = input.nextInt();
        }

        for(int i = 0; i < arrayDois.length; i++){
            System.out.println("Digite o " + (i + 1) +"º numero da 2º array: " );;
            arrayDois[i] = input.nextInt();
        }

        for(int i = 0; i < arrayTres.length; i++){
            System.out.println("Digite o " + (i + 1) +"º numero da 3º array: " );;
            arrayTres[i] = input.nextInt();
        }

        for(int i = 0; i < arrayQuatro.length; i++){
            System.out.println("Digite o " + (i + 1) +"º numero da 4º array: " );;
            arrayQuatro[i] = input.nextInt();
        }
        input.close();

        System.out.println("Elementos da 1º array:");
        for (int num : arrayNum) {
            System.out.print(num + " ");
        }
        System.out.println();

        System.out.println("Elementos da 2º array:");
        for (int num : arrayDois) {
            System.out.print(num + " ");
        }
        System.out.println();

        System.out.println("Elementos da 3º array:");
        for (int num : arrayTres) {
            System.out.print(num + " ");
        }
        System.out.println();

        System.out.println("Elementos da 4º array:");
        for (int num : arrayQuatro) {
            System.out.print(num + " ");
        }
        System.out.println();
    } 
}