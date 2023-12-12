package Heranca;

import java.util.Date;

public class main {
    public static void main(String[] args) {
        Aluno i = new Aluno("Jose Francisco", "123.456.789-00", new Date());
        System.out.println("Veja como os atributos foram preenchidos\n\nNome: " + i.nome);
        System.out.println("CPF: " + i.cpf);
        System.out.println("Data de Nascimento: " + i.data_nascimento.toString());

        Professor a = new Professor("Anderson Ribeiro", "333.333.789-33", new Date());
        System.out.println("Veja como os atributos foram preenchidos\n\nNome: " + a.nome);
        System.out.println("CPF: " + a.cpf);
        System.out.println("Data de Nascimento: " + a.data_nascimento.toString());

        Funcionario b = new Funcionario("Felipe paiva", "479.595.874-95", new Date());
        System.out.println("Veja como os atributos foram preenchidos\n\nNome: " + b.nome);
        System.out.println("CPF: " + b.cpf);
        System.out.println("Data de Nascimento: " + b.data_nascimento.toString());
    }
}
