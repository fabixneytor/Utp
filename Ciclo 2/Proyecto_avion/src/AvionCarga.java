public class AvionCarga extends Avion{

    /*********************
     * Método constructor
     *********************/
    public AvionCarga(String color, int tamanio){
        super(color, tamanio);
    }

    /************
     * Métodos
     ***********/
    public void cargar(){
        System.out.println("Cargando...");
    }
    public void descargar(){
        System.out.println("Descargando...");
    }
    
}

