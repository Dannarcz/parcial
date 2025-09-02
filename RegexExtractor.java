import java.util.regex.*;
import java.util.*;

public class RegexExtractor {
    public static void main(String[] args) {
        String texto = 
    "Hola, mi correo es juan.perez@example.com y también uso otro: contacto@empresa.org.\n" +
    "Puedes llamarme al +34 612-345-678 o al 987654321.\n" +
    "También visítanos en https://www.miweb.com o http://empresa.net\n" +
    "Nací el 25/12/1990 y mi hermano el 1995-07-14.\n" +
    "La reunión será el 03-09-2025.\n" +
    "Mi servidor usa la IP 192.168.1.1 y el otro 8.8.8.8.\n";

        // Patrones regex
        String patronEmail   = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}";
        String patronTelefono = "(?:\\+34\\s?)?(?:\\d{9}|\\d{3}[-\\s]?\\d{3}[-\\s]?\\d{3})";
        String patronUrl     = "https?://[^\\s]+";
        String patronFecha   = "\\b(?:\\d{2}[/\\-]\\d{2}[/\\-]\\d{4}|\\d{4}[/\\-]\\d{2}[/\\-]\\d{2})\\b";
        String patronIp      = "\\b(?:(25[0-5]|2[0-4]\\d|1?\\d{1,2})\\.){3}(25[0-5]|2[0-4]\\d|1?\\d{1,2})\\b";

        // Buscar coincidencias
        extraer(texto, patronEmail, "Correos encontrados");
        extraer(texto, patronTelefono, "Teléfonos encontrados");
        extraer(texto, patronUrl, "URLs encontradas");
        extraer(texto, patronFecha, "Fechas encontradas");
        extraer(texto, patronIp, "IPs encontradas");
    }

    private static void extraer(String texto, String patron, String titulo) {
        Pattern pattern = Pattern.compile(patron);
        Matcher matcher = pattern.matcher(texto);

        List<String> resultados = new ArrayList<>();
        while (matcher.find()) {
            resultados.add(matcher.group());
        }

        System.out.println(titulo + ": " + resultados);
    }
}
