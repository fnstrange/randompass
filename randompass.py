import random
import string

def generar_contraseña():
    longitud = random.randint(12, 16)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.joi n(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Genera contraseña aleatoria
contraseña_generada = generar_contraseña()

# Imprime la contraseña
color_amarillo = "\033[93m"  # Código ANSI para color amarillo
reset_color = "\033[0m"       # Código ANSI para resetear el color

print(f"\U0001F512 Contraseña generada: {color_amarillo}{contraseña_generada}{reset_color}")
