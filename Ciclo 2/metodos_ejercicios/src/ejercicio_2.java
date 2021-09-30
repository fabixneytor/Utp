import java.util.Scanner;

public class ejercicio_2 {
    

    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        System.out.println("Introduce un numero entero: ");
        var numero = sc.nextInt();

        var digitos = numero_digitos(numero);
        System.out.println("El numero tiene " + digitos + " cifras");
    }
    public static int numero_digitos(int numero) {
        var cifras = 0;

        while (numero != 0) {
            numero /= 10;
            cifras++;
        }
        return cifras;
    }
}
