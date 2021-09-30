public class App {
    public static void main(String[] args) throws Exception {
        //Construcción de un avión de carga
        AvionCarga objAvionCarga = new AvionCarga("Azul", 800);
        objAvionCarga.cargar();
        objAvionCarga.despegar();
        objAvionCarga.aterrizar();
        objAvionCarga.frenar();
        objAvionCarga.descargar();

        System.out.println("----------Avion Pasajeros----------");

        AvionPasajeros objAvionPasajeros = new AvionPasajeros("Verde", 900, 250);
        objAvionPasajeros.despegar();
        objAvionPasajeros.servir();
        objAvionPasajeros.aterrizar();
        objAvionPasajeros.frenar();
        String color = objAvionPasajeros.getColor();
        System.out.println(color);
        objAvionPasajeros.setColor("Azul");
        color = objAvionPasajeros.getColor();
        System.out.println(color);

        System.out.println("----------Avion Militar----------");
        AvionMilitar objAvionMilitar = new AvionMilitar("Verde", 900, 6);
        objAvionMilitar.detectar_amenaza(false);
        for(int i = 0; i < 8; i++){
            objAvionMilitar.detectar_amenaza(true);
        }
        

    }
}

/****************************
 * En unos minutos retomamos...
 **********************/
