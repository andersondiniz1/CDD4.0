package Encapsulamento;

public class funcionarios {
 
    String nome;
    String endereco;
    private String cpf;
    private String rg;
    private String telefone;
    private String email;
    private Double salario;
    private int q_filhos;

    // public void ajustarcpf(String cpf) {
    //     this.cpf = cpf;
    // }

    public String ajustarcpf(String cpf) {
        //this.cpf = cpf;
        return this.cpf;
    }

    public String ajustarrg(String rg) {
        return this.rg;
    }

    public String ajustartelefone(String telefone) {
        return this.telefone;
    }

    public String ajustaremail(String email) {
        return this.email;
    }

    public Double ajustarsalario(Double salario) {
        return this.salario;
    }

    public int ajustarq_filhos(int q_filhos) {
        return this.q_filhos;
    }
}
