package com.example;

public class dolares {
    public static void main( String[] args )
    {
        System.out.println( convertir_a_dolares(3700, 350000) );
    }

    //Convertir de dolares a pesos
    public static double convertir_a_pesos(double valor_dolar, double cant_dolares){
        double resultado = valor_dolar * cant_dolares;
        return resultado;
    }

    //Convertir de pesos a dolares
    public static double convertir_a_dolares(double valor_dolar, double cant_pesos){
        double resultado = cant_pesos/valor_dolar;
        return resultado;
    }


}
