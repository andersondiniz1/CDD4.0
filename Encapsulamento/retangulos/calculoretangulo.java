public class calculoretangulo {

    public static void main(String[] args) {
        
        // Exemplo de uso
        retangulo retangulo = new retangulo(5.0, 3.0);

        // Obtendo e exibindo valores usando getters
        System.out.println("Base do retângulo: " + retangulo.getBase());
        System.out.println("Altura do retângulo: " + retangulo.getAltura());
        System.out.println("Área do retângulo: " + retangulo.getArea());
        System.out.println("Perímetro do retângulo: " + retangulo.getPerimetro());

        // Modificando valores usando setters
        retangulo.setBase(7.0);
        retangulo.setAltura(4.0);

        // Calculando e exibindo a área e o perímetro do retângulo após a modificação
        System.out.println("\nÁrea do retângulo: " + retangulo.getArea());
        System.out.println("Perímetro do retângulo: " + retangulo.getPerimetro());
    }
}
