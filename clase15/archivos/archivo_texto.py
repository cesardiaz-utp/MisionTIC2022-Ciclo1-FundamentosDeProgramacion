# 
#  Creacion de archivo desde cero. Escribir varias lineas
#
def crear_archivo_ejemplo1(nombre_archivo = "prueba1.txt"):
    archivo = open(nombre_archivo, "w")

    archivo.write("Hola Mundo!")
    archivo.write("\n")
    archivo.write("Este es mi primer archivo\n")

    archivo.close()

# 
#  Lectura linea por linea, eliminando cambio de linea
#
def leer_archivo_ejemplo1(nombre_archivo = "prueba1.txt"):
    archivo = open(nombre_archivo, "r")

    for linea in archivo:
        print(linea)
        # print(linea.strip("\n"))

    archivo.close()
    print("Archivo leido")

# 
#  Agregar lineas al final con print.
#
def crear_archivo_ejemplo2(mensaje = "Hola Mundo", nombre_archivo = "prueba1.txt"):
    archivo = open(nombre_archivo, "a")

    print(mensaje, file=archivo)

    archivo.close()

# 
#  Lectura de todas las lineas a una lista, usando with
#
def leer_archivo_ejemplo2(nombre_archivo = "prueba1.txt"):
    with open(nombre_archivo, "r") as archivo:

        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)

    print("Archivo leido")

