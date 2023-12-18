package Encapsulamento.pets;

public class meupet {
    public static void main(String[] args) {
        // Criando uma instância de Pet usando o construtor com parâmetros
        pet meuPet = new pet("Fido", "Cachorro", 3);

        // Obtendo informações do pet usando os getters
        System.out.println("Nome: " + meuPet.getNome());
        System.out.println("Animal: " + meuPet.getAnimal());
        System.out.println("Idade: " + meuPet.getIdade());

        // Atualizando informações do pet usando os setters
        meuPet.setNome("Bolinha");
        meuPet.setAnimal("Gato");
        meuPet.setIdade(2);

        // Obtendo informações atualizadas do pet
        System.out.println("\nNome: " + meuPet.getNome());
        System.out.println("Animal: " + meuPet.getAnimal());
        System.out.println("Idade: " + meuPet.getIdade());
    }
}
