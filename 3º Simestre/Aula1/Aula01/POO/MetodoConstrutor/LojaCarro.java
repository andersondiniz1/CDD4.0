package Aula01.POO.MetodoConstrutor;

public class LojaCarro {
    
    public static void main(String[] args) {
        Carro veiculo1 = new Carro();

        veiculo1.cor = "Rosa";
        veiculo1.modelo = "Fusca";
        veiculo1.preco = 10.000;

        Carro veiculo2 = new Carro("Brazilia", 13.500);

        veiculo2.cor = "Verde";

        Carro veiculo3 = new Carro("Vermelho", "Opala", 19.570);

    }
    
}
