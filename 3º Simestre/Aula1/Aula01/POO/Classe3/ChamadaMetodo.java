package Aula01.POO.Classe3;

public class ChamadaMetodo {
    
      public static void main(String[] args) {
        
        JavaMetodos pessoa = new JavaMetodos();
        int pessoaIdade = pessoa.idade();
        double dinheiro = pessoa.valor();
        String nomeCompleto = pessoa.nome();
        boolean status = pessoa.estado();
        System.out.println(pessoaIdade + " " + dinheiro + " " + nomeCompleto + " " + status);
      }
}
