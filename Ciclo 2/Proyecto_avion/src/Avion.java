/**
 * Fecha: 06 de Julio de 2021
 * Autor: Darío Andrés Peña Quintero
 * Empresa: UTP - MINTIC
 * Proyecto: Fabrica de aviones
 * Clase: Clase que representa un avión
 */
public class Avion {
    /*************
     * Atributos
     *************/
    private String color;
    private int tamanio;

    /*********************
     * Método constructor
     *********************/
    public Avion(String color, int tamanio){
        this.color = color;
        this.tamanio = tamanio;
    }
    /*
    public Avion(){
        this.color = "";
        this.tamanio = 0;
    }
    */

    /**************************
     * Métodos consultores
     * (Getters)
     ************************/
    public String getColor(){
        return this.color;
    }
    public int getTamanio(){
        return this.tamanio;
    }

    /*************************
     * Métodos modificadores
     * (Setters)
     *************************/
    public void setColor(String color){
        this.color = color;
    }

    /************
     * Métodos
     ************/
    public void aterrizar(){
        System.out.println("Aterrizando...");
    }

    public void despegar(){
        System.out.println("Despegando...");
    }

    public void frenar(){
        System.out.println("Frenando...");
    }

    
}


/************
 * https://gitlab.com/mision_tic_2022/utp/ciclo2_2021/p16/proyecto_avion
 */
