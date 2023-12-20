public class triatleta implements ciclista, nadador, corredor {

    @Override
    public String aquecer() {
        return "Foi aquecer";
    }

    @Override
    public String correr() {
        return "Foi correr";
    }

    @Override
    public String nadar() {
        return "Foi nadar";
    }

    @Override
    public String pedalar() {
        return "Foi pedalar";
    }


}
