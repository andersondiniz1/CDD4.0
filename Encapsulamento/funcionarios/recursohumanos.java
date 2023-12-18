package Encapsulamento.funcionarios;

public class recursohumanos {
 
    public static void main(String[] args) {
        funcionarios f1 = new funcionarios();
        f1.nome = "Marcelo da Silva";
        f1.endereco = "Rua da cacha prego";
        f1.ajustarcpf("123.123.123.33");
        f1.ajustarrg("321.321.32");
        f1.ajustartelefone("81 91234-4321");
        f1.ajustaremail("Marcelo@gmail.com");
        f1.ajustarsalario(10.000);
        f1.ajustarq_filhos(2);
    }

}
