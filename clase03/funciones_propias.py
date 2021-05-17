#-------------------------------------------------------------------------------------------------
# Definición de funciones nuevas (personalizadas)
#-------------------------------------------------------------------------------------------------
#
#def NOMBRE(LISTA_DE_PARAMETROS):
#    """DOCSTRING_DE_FUNCION"""
#    SENTENCIAS
#    RETURN [EXPRESION]
#
#    NOMBRE, es el nombre de la función.
#    LISTA_DE_PARAMETROS, es la lista de parámetros que puede recibir una función.
#    DOCSTRING_DE_FUNCION, es la cadena de caracteres usada para documentar la función.
#    SENTENCIAS, es el bloque de sentencias en código fuente Python que realizar cierta operación dada.
#    RETURN, es la sentencia return en código Python.
#    EXPRESION, es la expresión o variable que devuelve la sentencia return.

def mi_funcion():
    print("Imprimiendo desde la función")

mi_funcion()

# Parametros
def saludo(nombre):
    print("Hola", nombre)

saludo("Cesar")
saludo("Andres")
saludo("Pablo")

# Varios parámetros
def nombre_completo(nombre, apellido = "Abad"):
    """Generación del nombre completo de la persona
    Parámetros
        nombre: Identifica a la persona
        apellido: Representa la famiilia del padre y la madre
    Retorna
        La unión de los dos parametros ingresados
    """
    return nombre + " " + apellido

print(nombre_completo("Cesar", "Diaz"))
print(nombre_completo("Andrea", "Martinez"))
print(nombre_completo("Carolina"))
print(nombre_completo(apellido="Noriega", nombre = "Paulo"))


print(nombre_completo.__doc__)
