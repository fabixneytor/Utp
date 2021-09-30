
public class PrecioTotal {
    // Atributos

    private double totalPrecios;
    private double totalDespacho;
    private double totalExpreso;

    private Casillero casillero[] ;

    // Constructores
    public PrecioTotal(Casillero[] casillero){
        this.casillero = casillero;
    }

    // Metodos
    public void calcularTotales(){
        
        for(int i = 0; i < casillero.length; i++){
            totalPrecios += casillero[i].calcularPrecio();

            if(casillero[i].getClass() == Despacho.class){
                totalDespacho += casillero[i].calcularPrecio();
            }else{
                totalExpreso += casillero[i].calcularPrecio();
            }
        }
    }


    public void mostrarTotales() {
        // Calculo de totales
        calcularTotales();
        System.out.println("Total Casillero " + totalPrecios);
        System.out.println("Total Despachos " + totalDespacho);
        System.out.println("Total Expresos " + totalExpreso);
        }
}
