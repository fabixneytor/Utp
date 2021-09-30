public class Facultad {
    /***********
     * Atributos
     **********/
    private String nombre;
    private Universidad universidad;

    /**************
     * Constructor
     *************/
    public Facultad(Universidad universidad){
        this.universidad = universidad;
    }

    //Consultor
    public String getNombre(){
        return this.nombre;
    }

    //Modificador
    public void setNombre(String nombre){
        this.nombre = nombre;
    }


}
