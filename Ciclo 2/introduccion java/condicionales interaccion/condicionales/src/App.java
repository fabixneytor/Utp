import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        //Variables
        int variable_1 = 4;
        int variable_2 = 10;
        //Condicionales
        if(variable_1 > variable_2){
            int suma = variable_1 + variable_2;
            System.out.println("La suma es: "+suma);
        }else{
            System.out.println("No cumple la condición");
        }

        //Estructuras de repetición
        System.out.println("------------While----------");
        int cont = 0;
        while(cont < 5){
            System.out.println(cont);
            ++cont;
        }
        System.out.println("Contador = "+cont);
        System.out.println("------------Do-While----------");
        do{
            System.out.println("Contador es mayor a 5");
            ++cont;
        }while(cont < 10);

        System.out.println("------------For----------");
        for(int i=0; i < 5; i++){
            System.out.println(i);
        }

    }
}
