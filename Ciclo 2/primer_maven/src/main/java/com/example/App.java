package com.example;

import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        String fecha = pedir_fecha();
        calcular_suerte(fecha);
    }

    public static String pedir_fecha() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Por favor digite su fecha de nacimiento");
        String fecha = sc.nextLine();
        sc.close();
        return (String) fecha;
    }

    public static void calcular_suerte(String fecha) {
        String[] arreglo_fecha = fecha.split("/");
        int suma = Integer.parseInt(arreglo_fecha[0])+Integer.parseInt(arreglo_fecha[1])+Integer.parseInt(arreglo_fecha[2]);
        System.out.println(suma);
    }
}
