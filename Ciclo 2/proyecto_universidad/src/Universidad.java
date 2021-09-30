public class Universidad{
    /**************
     * Atributos
     *************/
    private String nombre;
    private String nit;
    private Facultad[] facultades;

    /***************
     * Constuctor
     **************/
    public Universidad(String nombre, String nit){
        this.nombre = nombre;
        this.nit = nit;
        this.facultades = new Facultad[5];
    }

    public void crear_facultad(String nombre){
        //Crear un objeto de tipo facultad, se envía como referencia/parámetro la clase sobre la cual se crea(Universidad)
        Facultad objFacultad = new Facultad(this);
        
    }
}
