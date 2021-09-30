import java.util.Scanner;

public class par_o_impar {
    
    public static void main(String[] args) throws Exception {
        determinar_par();
    }

        //metodo para pedir un numero y mostrar si es par o impar
        public static void determinar_par() {
            //scanner
            Scanner leer = new Scanner(System.in);
            System.out.println("Por favor ingrese un entero");
            //captura un entero
            int numero = leer.nextInt();
            //cerrar el scanner
            leer.close();
            //variable que almacena un mensaje
            String mensaje = (numero%2 == 0) ? numero+" es par" : numero+" es impar";
            System.out.println(mensaje);
    }
}
