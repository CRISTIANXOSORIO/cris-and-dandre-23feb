
import java.util.ArrayList;
import java.util.Collections;


public class vectorj {

    public static void main(String[] args) {

        ArrayList<String> vacio = new ArrayList();

        ArrayList<String> deportes = new ArrayList();
        deportes.add("futbol");
        deportes.add("baloncesto");
        deportes.add("tenis");
        deportes.add("veisbol");
        deportes.add("bmx");
        deportes.add("atletismo");

        System.out.println("longitud de la lista vacia: " + vacio.size());
        System.out.println("longitud de la lista deportes: " + deportes.size());

        System.out.println(" Primer deporte: " + deportes.get(0));
        System.out.println(" deporte del medio: " + deportes.get(deportes.size() / 2));
        System.out.println(" Ultimo deporte: " + deportes.get(deportes.size() - 1));

        ArrayList<String> Datos_personales = new ArrayList();
        Datos_personales.add("Cristian");
        Datos_personales.add("22");
        Datos_personales.add("1.80");
        Datos_personales.add("soltero");
        Datos_personales.add("villa de la candelaria");

        ArrayList<String> it_companies = new ArrayList();
        it_companies.add("Facebook");
        it_companies.add("Google");
        it_companies.add("Microsoft");
        it_companies.add("Apple");
        it_companies.add("IBM");
        it_companies.add("Oracle");
        it_companies.add("Amazon");

        it_companies.add(4, "Acer");
        System.out.println(it_companies);

        System.out.println(it_companies.contains("IBM"));

        Collections.sort(it_companies);
        System.out.println(it_companies);

        Collections.reverse(it_companies);
        System.out.println(it_companies);

        it_companies.remove(1);
        System.out.println(it_companies);

        it_companies.clear();
        System.out.println(it_companies);
    }
}
