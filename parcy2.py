import re

def extraer_elementos(texto):
    resultados = {}

    # Números enteros (positivos y negativos)
    patron_enteros = r"(?<![\.\d-])-?\b\d+\b(?!\.\d)"
    resultados['enteros'] = re.findall(patron_enteros, texto)

    # Números flotantes (positivos y negativos)
    patron_flotantes = r"-?\b\d+\.\d+\b"
    resultados['flotantes'] = re.findall(patron_flotantes, texto)

    # Booleanos (True/False)
    patron_booleanos = r"\b(True|False)\b"
    resultados['booleanos'] = re.findall(patron_booleanos, texto)

    # Strings entre comillas dobles
    patron_strings = r'"([^"]*)"'
    resultados['strings'] = re.findall(patron_strings, texto)

    # Listas de números, ejemplo: [1, 2, 3]
    patron_listas = r"\[(?:\s*-?\d+\s*,)*\s*-?\d+\s*\]"
    resultados['listas'] = re.findall(patron_listas, texto)

    # Correos electrónicos
    patron_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    resultados['emails'] = re.findall(patron_email, texto)

    # Teléfonos (incluye opcional código país +34 y formatos comunes)
    patron_telefono = r"(?:\+34\s?)?\d{3}[-\s]?\d{3}[-\s]?\d{3}"
    resultados['telefonos'] = re.findall(patron_telefono, texto)

    # URLs http o https
    patron_url = r"https?://[^\s]+"
    resultados['urls'] = re.findall(patron_url, texto)

    # Fechas en formatos dd/mm/yyyy, dd-mm-yyyy, yyyy/mm/dd, yyyy-mm-dd
    patron_fecha = r"\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2})\b"
    resultados['fechas'] = re.findall(patron_fecha, texto)

    # Direcciones IP
    patron_ip = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    resultados['ips'] = re.findall(patron_ip, texto)

    # Nombres propios (palabras que comienzan con mayúscula y siguen con minúsculas)
    patron_nombres = r"\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\b"
    resultados['nombres_propios'] = re.findall(patron_nombres, texto)

    # Palabras con números dentro (ejemplo "a123", "b2b")
    patron_palabras_numeros = r"\b\w*\d+\w*\b"
    resultados['palabras_con_numeros'] = re.findall(patron_palabras_numeros, texto)

    # Hashtags (#ejemplo) y menciones (@usuario)
    patron_hashtags = r"#\w+"
    patron_menciones = r"@\w+"
    resultados['hashtags'] = re.findall(patron_hashtags, texto)
    resultados['menciones'] = re.findall(patron_menciones, texto)

    return resultados

# Texto ejemplo para probar
texto = """
En la programación manejamos diversos tipos de datos para representar información de forma estructurada; por ejemplo, los números enteros, que pueden ser positivos o negativos como 15 o -7, y los números flotantes que incluyen decimales, como 3.14 o -0.5. Para representar estados o condiciones lógicas utilizamos valores booleanos, que solo pueden ser True o False, lo cual es útil para tomar decisiones en el código, como saber si es_valido = True. Además, trabajamos con cadenas de texto (strings), que son secuencias de caracteres encerradas entre comillas, por ejemplo, "Hola, mundo". Finalmente, tenemos las listas, que son colecciones ordenadas de elementos, a menudo números, como la lista [10, 20, 30]. Cada uno de estos tipos de datos nos permite almacenar y manipular información de manera específica y efectiva dentro de un programa.

Hola, mi correo es juan.perez@example.com y también uso otro: contacto@empresa.org.
Puedes llamarme al +34 612-345-678 o al 987654321.
También visítanos en https://www.miweb.com o http://empresa.net
Nací el 25/12/1990 y mi hermano el 1995-07-14.
La reunión será el 03-09-2025.
Mi servidor usa la IP 192.168.1.1 y el otro 8.8.8.8.
Consulta en #programacion o menciona a @chatgpt para ayuda.
Palabras con números como a123 y b2b están aquí.
"""

# Ejecutar y mostrar resultados
resultados = extraer_elementos(texto)

for clave, valores in resultados.items():
    print(f"{clave.capitalize()} encontrados: {valores}")
