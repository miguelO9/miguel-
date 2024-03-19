
package mains_ejeClase;

import java.util.Scanner;


public class taller {

    public static void main(String[] args) {
        Scanner Scanner = new Scanner(System.in);
        while(true){
            System.out.println("\n1. persona");
            System.out.println("2. vehiculo");
            System.out.println("3. universidades");
            System.out.println("4. notas");
            System.out.println("5. salir");
            
            System.out.println("selecciona una opcion");
             int opcion = Scanner.nextInt();
             
             if (opcion == 1) {
                System.out.println("Hola seleccionaste la opcion Personas");
            } else if (opcion == 2){
                 System.out.println("HOLa seleccionste la opcion vehicuylo");
            }else if (opcion == 3){
                 System.out.println("hola seleccionaste la opcion iniversidad");
            }else if (opcion == 4){
                 System.out.println("hola has seleccionado la opcion nota");
            }else if (opcion == 5){
                 System.out.println("el programa ha finalizado");
                 break;
            }else { System.out.println("obcion no valisdd8a");
                
            }
             
                      
        }
    
         
    }
     
}
    
     

