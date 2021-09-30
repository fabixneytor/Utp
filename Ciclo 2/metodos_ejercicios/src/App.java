import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        String nombre = pedir_nombre();
        saludar(nombre);
    }

    //Metodo saludar
    public static void saludar(String nombre){
        System.out.println("Hello, "+nombre);
    }

    //Metodo para solicitar el nombre de la persona
    public static String pedir_nombre() {
        //Crear objeto scanner
        Scanner sc = new Scanner(System.in);
        System.out.print("Por favor digite su nombre: ");
        String nombre = sc.next();
        sc.close();
        return nombre;
    }


}
