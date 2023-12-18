public class retangulo {
    // Atributos privados
    private double base;
    private double altura;
    private double area;
    private double perimetro;

    // Construtor que recebe base e altura
    public retangulo(double base, double altura) {
        setBase(base);
        setAltura(altura);
    }

    // Métodos getters e setters para base
    public double getBase() {
        return base;
    }

    public void setBase(double base) {
        this.base = base;
        calcularArea(); // Recalcula a área ao modificar a base
        calcularPerimetro(); // Recalcula o perímetro ao modificar a base
    }

    // Métodos getters e setters para altura
    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
        calcularArea(); // Recalcula a área ao modificar a altura
        calcularPerimetro(); // Recalcula o perímetro ao modificar a altura
    }

    // Métodos getters para área e perímetro
    public double getArea() {
        return area;
    }

    public double getPerimetro() {
        return perimetro;
    }

    // Método privado para calcular a área do retângulo
    private void calcularArea() {
        this.area = base * altura;
    }

    // Método privado para calcular o perímetro do retângulo
    private void calcularPerimetro() {
        this.perimetro = 2 * (base + altura);
    }
}
