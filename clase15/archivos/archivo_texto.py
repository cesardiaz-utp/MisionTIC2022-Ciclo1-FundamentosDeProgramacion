# 
#  Creacion de archivo desde cero. Escribir varias lineas
#
def crear_archivo_ejemplo1(nombre_archivo = "/home/cdiaz/Escritorio/prueba1.txt"):
    archivo = open(nombre_archivo, "w")

    # \n, \t, \b, \r, \\, \r\n
    archivo.write("Hola Mundo!")
    archivo.write("\n") # Cambio de linea
    archivo.write("Este es mi primer archivo\n")
    archivo.write("Esta linea es la ultima!\n")
    archivo.write("Otra prueba de escritura\n")
    archivo.write("La expresion es {}\n".format(1+5))

    archivo.close()

#crear_archivo_ejemplo1()

# 
#  Lectura linea por linea, eliminando cambio de linea
#
def leer_archivo_ejemplo1(nombre_archivo = "prueba1.txt"):
    archivo = open(nombre_archivo, "r")
    #print(type(archivo))

    for linea in archivo:
        print(linea) # "Hola Mundo\n"
        #print(linea.strip("\n")) # "Hola Mundo"

    archivo.close()
    print("Archivo leido")

#leer_archivo_ejemplo1()

# 
#  Agregar lineas al final con print.
#
def crear_archivo_ejemplo2(mensaje = "Hola Mundo", nombre_archivo = "prueba1.txt"):
    archivo = open(nombre_archivo, "a")

    print(mensaje, file=archivo)
    #print(mensaje, "12354", (1+5), file=archivo)

    archivo.close()

#crear_archivo_ejemplo2(f"Nueva linea de texto {10**3}")

# 
#  Lectura de todas las lineas a una lista, usando with
#
def leer_archivo_ejemplo2(nombre_archivo = "prueba1.txt"):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea.strip("\n"))

    print("Archivo leido")

# leer_archivo_ejemplo2()
