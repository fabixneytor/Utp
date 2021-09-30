public class AvionMilitar extends Avion{
    /*************
     * Atributos
     *************/
    private int misiles;

    public AvionMilitar(String color, int tamanio, int misiles){
        super(color, tamanio);
        this.misiles = misiles;
    }

    public void detectar_amenaza(boolean amenaza){
        if(amenaza){
            this.disparar();
        }else{
            System.out.println("No es una amenaza");
        }
    }

    private void disparar(){
        if(this.misiles > 0){
            System.out.println("Disparar");
            --this.misiles;
        }else{
            System.out.println("No hay munición");
        }
        
    }

}
