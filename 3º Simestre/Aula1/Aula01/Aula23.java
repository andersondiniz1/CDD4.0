package Aula01;

import java.util.Scanner;

public class Aula23 {

    public static void main(String[] args) {
    
        Scanner input = new Scanner(System.in);

        Double[] notas = new Double[5];
        Double soma = 0.0;
        Double media = 0.0;

        for(int i = 0; i < notas.length; i++){
            System.out.println("Digite a nota do " + (i + 1) +"º aluno: " );
            notas[i] = input.nextDouble();
        }

        input.close();

        for (Double num : notas) {
            soma += num;
        }
        media = soma / notas.length;

        System.out.println("Média dos 5 alunos: " + media);
    } 
}