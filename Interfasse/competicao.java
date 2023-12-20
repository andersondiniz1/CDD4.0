public class competicao {
    
    public static void main(String[] args) {
        triatleta t1 = new triatleta();
        t1.nome = "Marcelo";
        t1.idade = 25;
        String aquecer = t1.aquecer();

        System.out.println(t1.nome + " tem " + t1.idade);
    }
}
