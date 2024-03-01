import pandas as pd

# Definición de la clase DatosPersonales
class DatosPersonales:
    # Constructor de la clase
    def __init__(self, nombre_completo, carnet_identidad, pueblo, patria):
        # Inicialización de atributos de datos personales
        self.nombre = nombre_completo
        self.poblacion = pueblo
        self.dni = carnet_identidad
        self.pais = patria 

    # Método para validar y formatear el nombre, solo acepta letras y transforma la primera en mayusculas
    def validar_nombre(self, nombre_completo):
        while True:
            try:
                if not nombre_completo.replace(' ', '').isalpha():
                    raise ValueError("\nEl nombre debe contener solo letras.")
            except ValueError:
                nombre_completo = input("Vuelve a introducir el nombre correctamente: ")
            else:
                # Convertir el nombre a formato de título, la primera letra de cada palabra en mayúsculas
                self.nombre = nombre_completo.title()
                return self.nombre 

    # Método para validar y formatear la población, transforma la primera letra en mayusculas de cada palabra
    def validar_poblacion(self, pueblo):
        self.poblacion = pueblo.title()
        return self.poblacion

    # Método para validar el DNI, solo acepta la entrada de 8 numeros y el ultimo tiene que ser una letra
    def validar_dni(self, carnet_identidad):
        while not (len(carnet_identidad) == 9 and carnet_identidad[:-1].isdigit() and carnet_identidad[-1].isalpha()):
            carnet_identidad = input("Vuelve a darme el DNI correctamente, recuerda poner la letra: ")
        self.dni = carnet_identidad  
        return self.dni 

    # Método para validar y formatear el país, transforma todo el string a mayusculas
    def validar_pais(self, patria):
        self.pais = patria.upper()
        return self.pais 

    # Método para obtener los datos en un diccionario
    def obtener_datos(self):
        return {
            'Nombre': self.nombre,
            'Pueblo': self.poblacion,
            'DNI': self.dni,
            'País': self.pais
        }

# Definición de la clase GustoMusical
class GustoMusical:
    # Constructor de la clase
    def __init__(self, cancion_favorita, grupo, estilo_musical):
        # Inicialización de atributos de gustos musicales
        self.cancion_favorita = cancion_favorita
        self.grupo = grupo
        self.estilo_musical = estilo_musical

    # Métodos para validar y formatear canción favorita, transforma la primera letra en mayusculas de cada palabra
    def validar_cancion_favorita(self, cancion_favorita):
        self.cancion_favorita = cancion_favorita.title()
        return self.cancion_favorita

    # Métodos para validar y formatear grupo, transforma la primera letra en mayusculas de cada palabra
    def validar_grupo(self, grupo):
        self.grupo = grupo.title()
        return self.grupo

    # Métodos para validar y formatear estilo musical, transforma todo el string a mayuscula
    def validar_estilo_musical(self, estilo_musical):
        self.estilo_musical = estilo_musical.upper()
        return self.estilo_musical

    # Método para obtener los datos en un diccionario
    def obtener_datos(self):
        return {
            'Canción Favorita': self.cancion_favorita,
            'Grupo Favorito': self.grupo,
            'Estilo Musical': self.estilo_musical
        }

# Definición de la clase Amigo, que hereda de DatosPersonales y GustoMusical
class Amigo(DatosPersonales, GustoMusical):
    # Constructor de la clase
    def __init__(self, nombre_completo, carnet_identidad, pueblo, patria, cancion_favorita, grupo, estilo_musical):
        # Llamada a los constructores de las clases padre
        DatosPersonales.__init__(self, nombre_completo, carnet_identidad, pueblo, patria)
        GustoMusical.__init__(self, cancion_favorita, grupo, estilo_musical)
        
    # Método para obtener la información del amigo en un diccionario combinando DatosPersonales y GustoMusical
    def amigo_informacion(self, amigo):
        amigo = {**DatosPersonales.obtener_datos(self), **GustoMusical.obtener_datos(self)}
        return amigo

# Lista para almacenar la base de datos de amigos
base_de_datos = []

# Función para mostrar el menú principal del programa
def menu():
    print("\nMENU PRINCIPAL")
    print("--------------")
    print("1. Mostrar base de datos")
    print("2. Añadir amigos")
    print("3. Eliminar amigos")
    print("4. Salir")

# Función para mostrar la base de datos de amigos
def mostrar_base_de_datos():
    if len(base_de_datos) == 0:
        print("\nLa base de datos está vacía.\n")
    else:
        print("")
        # Creación de un DataFrame usando pandas para mostrar la base de datos
        df = pd.DataFrame([amigo.amigo_informacion(amigo) for amigo in base_de_datos], columns=['Nombre', 'Pueblo', 'DNI', 'País', 'Canción Favorita', 'Grupo Favorito', 'Estilo Musical'], index=range(1, len(base_de_datos) + 1))
        pd.set_option('display.colheader_justify', 'center')

        # Mostrar el DataFrame
        print(df.to_string())

# Función para agregar amigos a la base de datos
def anadir_amigos():
    while True:
        print("\nBASE DE DATOS DE GUSTOS MUSICALES DE AMIGOS")
        print("-------------------------------------------\n")
        # Solicitar al usuario los datos del objeto Amigo
        nombre_completo = input("Nombre Completo: ")
        pueblo = input("Ciudad Donde Vive: ")
        carnet_identidad = input("DNI: ")
        patria = input("País: ")
        cancion_favorita = input("Canción Favorita: ")
        grupo = input("Grupo Favorito: ")
        estilo_musical = input("Estilo Musical: ")
        
        # Crear un objeto Amigo 
        amigo = Amigo(nombre_completo, carnet_identidad, pueblo, patria, cancion_favorita, grupo, estilo_musical)
        
        # Realizar las validaciones de datos llamando a sus métodos
        amigo.validar_dni(carnet_identidad)
        amigo.validar_nombre(nombre_completo)
        amigo.validar_poblacion(pueblo)
        amigo.validar_pais(patria)
        amigo.validar_cancion_favorita(cancion_favorita)
        amigo.validar_grupo(grupo)
        amigo.validar_estilo_musical(estilo_musical)
               
        # Obtener información del amigo en forma de diccionario
        amigo.amigo_informacion(amigo)
        
        # Bucle para confirmar si se quieren guardar los datos del amigo actual en la base de datos
        while True:
            try:
                conformidad_guardar_amigo = input("\n¿Quieres guardar los datos? (si/no): ").lower()
                if conformidad_guardar_amigo not in ('si','no'):
                    raise ValueError("Por favor, ingresa si o no.")
            except ValueError as error:
                print(f"Error: {error}")
            else:
                if conformidad_guardar_amigo == 'si':
                    # Agregar el amigo a la base de datos
                    base_de_datos.append(amigo)
                    print("\nSe han guardado los datos correctamente.\n")
                break

        # Bucle para preguntar si se desea ingresar otro amigo
        while True:
            try:
                continuar = input("¿Deseas ingresar otro amigo? (si/no): ").lower()
                if continuar not in ('si','no'):
                    raise ValueError("Por favor, ingresa si o no.")
            except ValueError as error:
                print(f"Error: {error}")
            else:
                if continuar == 'no':
                    return  # Salir de la función y del bucle principal
                else:
                    break   # Romper el bucle 


# Función para eliminar amigos de la base de datos
def eliminar_amigos():
    if not base_de_datos:
        print("\nLa base de datos está vacía.")
        return

    # Mostrar la lista de amigos con sus índices
    print("")
    for indice, amigo in enumerate(base_de_datos, 1):
        print(f'{indice}.-{amigo.nombre}')

    # Bucle para solicitar al usuario el índice del amigo a eliminar
    while True:
        try:
            indice_eliminar = int(input('\nDime a quién quieres eliminar por su índice: ')) - 1
            if 0 <= indice_eliminar < len(base_de_datos):
                break   # Si encuentra el indice rompe el bucle
            else:
                print(f"\nIntroduce un dígito entre el 1 y el {len(base_de_datos)}.")
        except ValueError:
            print(f"\nDebes introducir un número entero entre el 1 y el {len(base_de_datos)}.")

    # Eliminar al amigo seleccionado
    amigo_eliminado = base_de_datos[indice_eliminar]
    base_de_datos.remove(amigo_eliminado)
    print(f"\nUsuario {amigo_eliminado.nombre} eliminado de la lista principal.\n")

# Función principal que maneja el menú del programa
def main():
    while True:
        # Mostrar el menú principal
        menu()
        
        # Solicitar al usuario que elija una opción
        opcion = input("\nDime del 1 al 4 qué función quieres ejecutar: ")

        # Verificar si la entrada es un número
        if opcion.isdigit():
            opcion = int(opcion)

            # Realizar acciones según la opción seleccionada
            if opcion == 1:
                mostrar_base_de_datos()
            elif opcion == 2:
                anadir_amigos()
            elif opcion == 3:
                eliminar_amigos()
            elif opcion == 4:
                # Imprimir mensaje de salida y salir del bucle
                print("\nSaliendo del Menú, gracias y saludos.\n")
                break
            else:
                # Imprimir mensaje de error si la opción no es válida
                print("Opción no válida, vuelve a elegir una opción.")
        else:
            # Imprimir mensaje si la entrada no es un número
            print("Debes indicar la opción con un dígito del 1 al 4.")

# Entrada del Programa
if __name__ == "__main__":
    main()
