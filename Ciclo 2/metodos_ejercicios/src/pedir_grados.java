import java.util.Scanner;

public class pedir_grados {

    public static void main(String[] args) {
        float num = grados();
        centi_fahren(num);
    }

    //metodo
    public static void centi_fahren(float numero){
        float fahren = 32 + (9*numero/5);
        System.out.println("El valor de "+numero+ " centigrados en Fahrenheit es: "+fahren);
    }

    public static float grados(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Por favor digite la cantidad de grados en centigrados: ");
        float num = sc.nextFloat();
        sc.close();
        return (float) num;
    }


}
