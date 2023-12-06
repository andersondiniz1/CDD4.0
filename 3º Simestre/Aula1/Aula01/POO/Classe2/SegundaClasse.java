package Aula01.POO.Classe2;

public class SegundaClasse {
    
    public static void main(String[] args) {
        ClassePessoa aluno01 = new ClassePessoa();
        ClassePessoa aluno02 = new ClassePessoa();
        ClassePessoa aluno03 = new ClassePessoa();

        aluno01.nome = "Anderson";
        aluno02.nome = "João";
        aluno03.nome = "Maria";

        System.out.println(aluno01.nome);
        System.out.println(aluno02.nome);
        System.out.println(aluno03.nome);
        aluno01.comer();
    }
}
