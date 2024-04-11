package DICCIONARIO;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Dictionary;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map;


public class diccionario1 {

    public static void main(String[] args) {
        //1. Crea un diccionario vacío llamado perro
        Dictionary perro = new Hashtable();
        
        //2. Añade nombre, color, raza, patas y edad al diccionario perro.
       perro.put("nombre", "sacha");
       perro.put("color", "negro");
       perro.put("raza", "calle");
       perro.put("patas", "4");
       perro.put("edad", "3 años");
       
       /*3. Crea un diccionario de estudiante y añade nombre,
       apellido, sexo, edad, estado civil, habilidades, país,
               ciudad y dirección como claves del diccionario*/
       Dictionary estudiante = new Hashtable();
       ArrayList<String> p = new ArrayList();
       p.add("matematicas");
       p.add("ajedrez");
       
       estudiante.put("nombre", "miguel");
       estudiante.put("apellido", "oyola");
       estudiante.put("sexo", "masculino");
       estudiante.put("edad", "20");
       estudiante.put("estadi civil", "soltero");
       estudiante.put("habilidades", p);
       estudiante.put("pais", "colombia");
       estudiante.put("ciudad", "cartagena");
       estudiante.put("direccion", "tierra baja");
       
        
       
       //4. Obtén la longitud del diccionario del alumno
       int longitud = estudiante.size();
        System.out.println("la longitud es: " + longitud);
       
       //5. Obtenga el valor de las habilidades y compruebe el tipo de datos, debe ser una lista
       String valor = (String) estudiante.get("habilidades");
       
       
       //6. Modifique los valores de las habilidades añadiendo una o dos habilidades.
       p.add("calculo");
       p.add("futbol");
       
        //7. Obtener las claves del diccionario como una lista
        //8. Obtener los valores del diccionario como una lista
        //9. Cambie el diccionario a una lista de tuplas utilizando el método items()
        
        //10. Eliminar uno de los elementos del diccionario
        estudiante.remove("direccion");
        System.out.println("los nuevos valores son: " + estudiante );
        
        //11. Borrar uno de los diccionarios
        estudiante.clear();
        
        }
}
