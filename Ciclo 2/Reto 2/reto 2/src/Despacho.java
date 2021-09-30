public class Despacho extends Casillero {
    // Constantes
    private static final double CAPACIDAD = 8.0;
    // Constructores
    public Despacho(double peso, double tamanio){
        super(peso, tamanio);
    }

    public Despacho(double precioBase){
        super(precioBase);
    }

    public Despacho(){
        super();
    }


    // Metodos
    @Override
    public double calcularPrecio(){
    // Calculos
    double precio = getPrecioBase() + (getPeso() * getTamanio() * CAPACIDAD);
    return precio;
    }

}
