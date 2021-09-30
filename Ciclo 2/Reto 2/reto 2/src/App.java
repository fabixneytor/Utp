public class App {
    public static void main(String[] args) {
        // Caso de Prueba 1
        Casillero casillero[] = new Casillero[5];
        casillero[0] = new Despacho(500.0, 100.0);
        casillero[1] = new Despacho(2000);
        casillero[2] = new Expreso(1150, 200.0);
        casillero[3] = new Expreso();
        casillero[4] = new Despacho();
        PrecioTotal solucion = new PrecioTotal(casillero);
        solucion.mostrarTotales();
        }
}
