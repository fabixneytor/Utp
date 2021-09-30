public class Importacion {

    // ---------------------------------------------
    // Atributos
    // ---------------------------------------------

    private double capital;
    private double interes;
    private int tiempo;

    // ---------------------------------------------
    // Métodos
    // ---------------------------------------------

    public  Importacion()
    {
        capital = 0;
        interes = 0;
        tiempo = 0;
    }

    public double calcularInteresSimple( )
    {
        double interesSimple = capital * interes * tiempo;
        return interesSimple;
    }

    public double calcularInteresCompuesto( )
    {
        double interesCompuesto = capital * ( Math.pow(1 + interes, tiempo) - 1);
        return interesCompuesto;
    }

    public String compararInvImportacion (int Tiempo, double Capital, double Interes)
    {
        tiempo = Tiempo;
        capital = Capital;
        interes = Interes;

        double respuesta = calcularInteresCompuesto() - calcularInteresSimple();

        if (respuesta > 0)
        {
            return "La diferencia en el total de intereses generados para el proyecto, si escogemos entre evaluarlo a una tasa de interés Compuesto y evaluarlo a una tasa de interés Simple, asciende a la cifra de: $" + respuesta;
        }
        else
        {
            return "Faltan datos para calcular la diferencia en el total de intereses generados para el proyecto.";
        }

    }

}
