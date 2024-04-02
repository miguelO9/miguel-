
package vectores;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class vectores {

    private static Object collections;

    public static void main(String[] args) {
    //vector vacio
    String[] vacio = new String[0];
    
    //declarar un vector con mas de 5 elementos
    String[] vector= new String[7];
    vector[0]= "1";
    vector[1]= "2";
    vector[2]= "3";
    vector[3]= "4";
    vector[4]= "5";
    vector[5]= "6";
    vector[6]= "7";
          
    
    //encontrar la longitud del vector
    int longitud = vector.length;
        System.out.println("la longitud del vector es: "+ longitud);
        
        //obtener el primer elemento, el elemento central y el ultimo elemento del vcetor
        String primero= vector[0];
        String central = vector[3];
        String ultimo = vector[6];
        System.out.println("\nel primer elemento del vector es: "+ primero);
        System.out.println("el primer elemento del vector es: "+ central);
        System.out.println("el primer elemento del vector es: "+ ultimo);
        
        //Declarar un vector llamado tipos_datos_mezclados y asignarle los valores iniciales:
        String[] tiposDatosMezclados = new String[5];
        tiposDatosMezclados[0]= "miguel";
        tiposDatosMezclados[1]= "20";
        tiposDatosMezclados[2]= "1.82";
        tiposDatosMezclados[3]= "soltero";
        tiposDatosMezclados[4]= "tierra baja";
        System.out.println("\nnombre: "+ tiposDatosMezclados[0]); 
        System.out.println("edad: "+ tiposDatosMezclados[1]);
        System.out.println("estatura: "+ tiposDatosMezclados[2]);
        System.out.println("estado: "+ tiposDatosMezclados[3]);
        System.out.println("direccion: "+ tiposDatosMezclados[4]);
        
        //Declare una variable de lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
        
        String [] lista;
        ArrayList<String> it_companies = new ArrayList();
        it_companies.add("Google");
        it_companies.add("Microsoft");
        it_companies.add("Apple");
        it_companies.add("IBM");
        it_companies.add("Oracle");
        it_companies.add("Amazon");
        it_companies.add("Facebook");
        
         //Añadir una empresa de TI a it_companies utilizando los metodos de insercion
         it_companies.add(1,"Messenger");
         System.out.println("\nLas empresas en la lista son: "+ it_companies);
         
         //Comprobar si una determinada empresa existe en la lista it_companies.
         
         System.out.println("\ntrue si existe y false es que no existe: \n" +it_companies.contains("bb")); 
        
         //Ordena la lista con el método sort()
         Collections.sort(it_companies);
         System.out.println("\nLista ordenada: "+ it_companies);
         
         //Invierte la lista en orden descendente utilizando el método reverse()
         Collections.reverse(it_companies);
         System.out.println("\nLista invertida: "+it_companies);
         
         //Elimine la primera empresa informática de la lista con remove().
         it_companies.remove(0);
         System.out.println("\nAsi quedo la lista: "+ it_companies);
         
         //Eliminar todas las empresas de TI de la lista con clear()
         it_companies.clear();
         System.out.println("\nasi queda la lista: "+ it_companies);
         
    
    }
    }
  


