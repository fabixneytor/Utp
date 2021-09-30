public class AvionPasajeros extends Avion{
    /************
     * Atributos
     *************/
    private int pasajeros;

    /***************
     * Método constructor
     * @param color
     * @param tamanio
     **********************/    
    public AvionPasajeros(String color, int tamanio, int pasajeros){
        super(color, tamanio);
        this.pasajeros = pasajeros;
    }

    /****************
     * Método Consultor
     *******************/
    public int getPasajeros(){
        return this.pasajeros;
    }

    /**********************
     * Método Modificador
     ***********************/
    public void setPasajeros(int pasajeros){
        this.pasajeros = pasajeros;
    }

    public void servir(){
        System.out.println("Sirviendo...");
    }
}
