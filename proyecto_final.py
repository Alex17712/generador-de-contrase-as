import random
import string

# Función para validar la longitud
def validar_longitud():
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))
            
            if longitud < 8:
                print(" La longitud debe ser mínimo 8. Intente nuevamente.\n")
            else:
                return longitud
        
        except ValueError:
            print("Error: Debe ingresar un número válido.\n")

# Función para generar la contraseña
def generar_contrasena(longitud):
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    especiales = string.punctuation
    
    contrasena = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiales)
    ]
    
    todos = mayusculas + minusculas + numeros + especiales
    
    for i in range(longitud - 4):
        contrasena.append(random.choice(todos))
    
    random.shuffle(contrasena)
    return ''.join(contrasena)

# Función principal
def main():
    longitud = validar_longitud()
    password = generar_contrasena(longitud)
    print("\n Su Contraseña Generada es Segura:", password)

# Ejecutar programa
main()

    
   