import re

# Texto de ejemplo
texto = """
Hola, mi correo es juan.perez@example.com y también uso otro: contacto@empresa.org.
Puedes llamarme al +34 612-345-678 o al 987654321.
También visítanos en https://www.miweb.com o http://empresa.net
Nací el 25/12/1990 y mi hermano el 1995-07-14.
La reunión será el 03-09-2025.
Mi servidor usa la IP 192.168.1.1 y el otro 8.8.8.8.
"""

# Patrones regex
patron_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
patron_telefono = r"(?:\+34\s?)?\d{3}[-\s]?\d{3}[-\s]?\d{3}"
patron_url = r"https?://[^\s]+"
patron_fecha = r"\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2})\b"
patron_ip = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

# Buscar coincidencias
emails = re.findall(patron_email, texto)
telefonos = re.findall(patron_telefono, texto)
urls = re.findall(patron_url, texto)
fechas = re.findall(patron_fecha, texto)
ips = re.findall(patron_ip, texto)

# Mostrar resultados
print("Correos encontrados:", emails)
print("Teléfonos encontrados:", telefonos)
print("URLs encontradas:", urls)
print("Fechas encontradas:", fechas)
print("IPs encontradas:", ips)
