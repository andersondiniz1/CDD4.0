package Aula01;

import java.util.Scanner;

public class Aula08 {
    
        public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("Quantos alunos tem em sua sala: "); 
        int resp = entrada.nextInt();
        int contador = resp;
        double soma = 0;
        double media = 0;

        while (resp >= 0){
            
            System.out.println("Digite a nota do "+resp+"º aluno:"); 
            int nota = entrada.nextInt();
            soma = nota + soma;
            resp--;
        }

        media = soma / contador;
        System.out.println("Sua média é: "+media); 
        entrada.close();
    }
}

