#-------------------------------------------------------
# Definición de funciones (clásico)
#-------------------------------------------------------
# Función sin parámetros
def saludar_al_mundo():
    return "Hola Mundo"

# Función con parámetros
def saludar_alguien(quien):
    return "Hola "+str(quien)

# Función con parámetro opcional
def saludar_alguien_adicional(quien, adicional = "!"):
    return "Hola "+str(quien)+str(adicional)

saludar_alguien_adicional("Cesar")
saludar_alguien_adicional("Mundo", "*")
saludar_alguien_adicional(adicional=" :)", quien="Andres")

# Retornar más de 1 valor
def retornar_varios_valores():
    return "Cesar", "Diaz", 40, "Pereira"
valores = retornar_varios_valores() # tupla
nombre, apellido, edad, ciudad = valores

# Recibir cualquier cantidad de parámetros en una tupla (*args)
def suma_variable(*args):
    valor = 0
    for arg in args:
        if isinstance(arg, str):
            arg = ord(arg)
        elif not isinstance(arg, int) and not isinstance(arg, float):
            continue
        valor += arg
    return valor
print("Suma variable:", suma_variable(1,5,3,4,8,9,"A", [10, 20],10,2,6,7))
 
# Recibir cualquier cantidad de parámetros en una tupla con un dato obligatorio 
def promedio_estudiante(codigo, *notas):
    promedio = round(sum(notas)/len(notas),1)
    return f"El estudiante {codigo} obtuvo una nota con promedio {promedio}"
print("Nota final:", promedio_estudiante("1025", 2.5, 3.1, 4.0, 2.0, 4.0))

# Recibir cualquier cantidad de parámetros en un diccionario (**kwargs)
def imprimir_diccionario(**kwargs):
    print(kwargs)
imprimir_diccionario(nombre="Cesar", apellido="Diaz", edad=40)

# Alcance (scope) variables
nombre = "Cesar"
edad = 40
def imprimir_nombre():
    nombre = "Andres" # nueva local
    print("Nombre en función:", nombre, edad)
imprimir_nombre()
print("Nombre fuera de función:", nombre, edad)

# Scope global
def imprimir_nombre_global():
    global nombre
    nombre = "Andres"
    print("Nombre en función global:", nombre)
imprimir_nombre_global()
print("Nombre fuera de función global:", nombre)

# Funciones anidadas
def funcion_padre():
    nombre = "Cesar"
    def funcion_hijo():
        nombre = "Manuel"
        return f"Soy la funcion de {nombre}"
    return f"{nombre}: {funcion_hijo()}"

print("Funcion anidada:",funcion_padre())

#-------------------------------------------------------
# Programación funcional
#-------------------------------------------------------

#
# Funciones Lambda (anonimas)
#
def incrementar(x): return x + 1
incremento = lambda x: x + 1
print("Incremento de 9:", incremento(9), incrementar(9))

# Otros ejemplos
cubo = lambda x: x**3

raiz_cuadrada = lambda x : x**(1/2)

diferencia_cuadrado = lambda x1, x2 = 0: (x1 - x2)**2

nombre_completo = lambda nombres, apellidos: f"{nombres} {apellidos}"

es_par = lambda x : x % 2 == 0

funcion_compleja = lambda x, func: x + func(x)
print(funcion_compleja(2, lambda x: x * x))
print(funcion_compleja(2, lambda x: x + 3))

#
# Closures (envolturas): Crear una funcion que genera funciones
#
def construir_multiplos(factor):
  return lambda valor : valor * factor

multiplos_de_2 = construir_multiplos(2) # lambda valor : valor * 2
multiplos_de_7 = construir_multiplos(7) # lambda valor : valor * 7

multiplos_de_2(10) # 20
multiplos_de_7(2)  # 14

# Otro closure
def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

# Salida
# x = 0, y = 4, z = 5
# closure(5) = 9
# x = 1, y = 4, z = 6
# closure(6) = 11
# x = 2, y = 4, z = 7
# closure(7) = 13

# Decoradores 

def construir_operacion(operador, numero):
    def operacion_matematica(operador):
        if operador == "+":
            return lambda n1, n2 = numero: n1+n2
        elif operador == "-":
            return lambda n1, n2 = numero: n1-n2
        elif operador == "x":
            return lambda n1, n2 = numero: n1*n2
        elif operador == "/":
            return lambda n1, n2 = numero: n1/n2
    return operacion_matematica(operador)

for i in range(10):
    operador = 'x'
    tabla = construir_operacion(operador,i+1)
    for j in range(10):
        print(f"{j+1} {operador} {i+1} = {tabla(j+1)}")
