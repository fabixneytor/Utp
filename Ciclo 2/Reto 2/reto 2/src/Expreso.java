public class Expreso extends Casillero {
    // Constantes
    private final static int TIEMPO = 2;

    // Constructores
    public Expreso(double peso, double tamanio){
        super(peso, tamanio);
    }

    public Expreso(double precioBase){
        super(precioBase);
    }

    public Expreso(){
        super();
    }

    // Metodos
    public double calcularPrecio(){
        // Calculos
        return (getPrecioBase() + (getPeso() * getTamanio() * TIEMPO));
    }

}
