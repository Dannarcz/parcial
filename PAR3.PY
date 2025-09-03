import re

def extraer_todo(texto):
    resultados = {}

    # Enteros (positivos y negativos)
    resultados['enteros'] = re.findall(r"(?<![\.\d-])-?\b\d+\b(?!\.\d)", texto)

    # Flotantes (decimales)
    resultados['flotantes'] = re.findall(r"-?\b\d+\.\d+\b", texto)

    # Números en notación científica
    resultados['cientificos'] = re.findall(r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", texto)
    # Booleanos
    resultados['booleanos'] = re.findall(r"\b(True|False)\b", texto)

    # Strings entre comillas dobles
    resultados['strings'] = re.findall(r'"([^"]*)"', texto)

    # Listas de enteros
    resultados['listas'] = re.findall(r"\[(?:\s*-?\d+\s*,)*\s*-?\d+\s*\]", texto)

    # Correos electrónicos
    resultados['emails'] = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto)

    # Teléfonos (con y sin código país)
    resultados['telefonos'] = re.findall(r"(?:\+\d{1,3}\s?)?(\d{3}[-\s]?\d{3}[-\s]?\d{3,4}|\d{7,10})", texto)

    # URLs (http y https)
    resultados['urls'] = re.findall(r"https?://[^\s]+", texto)

    # Fechas (dd/mm/yyyy, dd-mm-yyyy, yyyy/mm/dd, yyyy-mm-dd)
    resultados['fechas'] = re.findall(r"\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2})\b", texto)

    # Direcciones IP (IPv4)
    resultados['ips'] = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", texto)

    # Nombres propios (palabras con mayúscula inicial y al menos 3 letras)
    candidatos = re.findall(r"\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]{2,}\b", texto)
    excluidos = {'True', 'False'}
    resultados['nombres_propios'] = [n for n in candidatos if n not in excluidos]

    # Palabras con números (al menos una letra y un número)
    resultados['palabras_con_numeros'] = re.findall(r"\b(?=\w*[a-zA-Z])(?=\w*\d)\w+\b", texto)

    # Hashtags
    resultados['hashtags'] = re.findall(r"#\w+", texto)

    # Menciones
    resultados['menciones'] = re.findall(r"@\w+", texto)

    # Horas (24h y 12h)
    resultados['horas'] = re.findall(r"\b([01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b", texto)

    # Código postal español (5 dígitos)
    resultados['codigos_postales'] = re.findall(r"\b\d{5}\b", texto)

    # Números con separadores de miles (ej. 1,000,000)
    resultados['numeros_miles'] = re.findall(r"\b\d{1,3}(?:,\d{3})+\b", texto)

    # Números de tarjeta de crédito (simplificado)
    resultados['tarjetas'] = re.findall(r"\b(?:\d{4}[- ]?){3}\d{4}\b", texto)

    return resultados

# Ejemplo de texto para probar
texto = """
En la programación manejamos diversos tipos de datos para representar información: números enteros como 15 o -7,
flotantes como 3.14, -0.5, y notación científica 1.23e-4 o -5E+6.
Booleanos True y False son comunes. Cadenas entre comillas como "Hola mundo".
Listas: [10, 20, 30].
Emails: juan.perez@example.com, contacto@empresa.org.
Teléfonos: +34 612-345-678, 987654321.
URLs: https://www.miweb.com, http://empresa.net.
Fechas: 25/12/1990, 1995-07-14, 03-09-2025.
IPs: 192.168.1.1, 8.8.8.8.
Nombres propios: Juan, María, Pedro, Ana.
Palabras con números: a123, b2b, test1234.
Hashtags: #programacion, #regex.
Menciones: @usuario, @chatgpt.
Horas: 14:30, 02:30 PM, 23:59.
Códigos postales: 28013, 08002.
Números con miles: 1,000,000; 12,345.
Tarjetas de crédito: 1234-5678-1234-5678, 1234 5678 1234 5678.
"""

resultados = extraer_todo(texto)

for categoria, valores in resultados.items():
    print(f"{categoria.capitalize()} encontrados: {valores}")

