#-------------------------------------------------------------------------------------------------
# Imprimir datos en pantalla
#-------------------------------------------------------------------------------------------------
print()
print("Hola, Mundo!")
print(10 + 25)
print("10 + 25 = ", (10+25)) 

print("10 + 25 ="); print(10 + 25)





#-------------------------------------------------------------------------------------------------
# Comentarios
#-------------------------------------------------------------------------------------------------

# Esto es un comentario de una sola línea
print("Comentarios") # Tambien puedo comentar al final de una expresión

# Este es un comentario multilínea, osea que para mejorar la legibilidad 
# del texto, se puede escribir varias líneas
# Siempre es muy importante dejar las ideas claras cuando se programa

# Tambien se pueden comentar líneas de código
# print("Hola, Mundo!")



#-------------------------------------------------------------------------------------------------
# Tipos de datos
#-------------------------------------------------------------------------------------------------
# Tipos texto: str

"Este es un texto"  # Preferido
'Este tambien es un texto válido en python'

print("Cadena:", 'Hola', type('Hola'))
print("Cadena:", "Mundo", type("Mundo"))



# Tipos numéricos: int, float, complex

# Enteros 
0
10
35
2154225
-3562

# print("Enteros:", 10, type(10))

# Decimales / Flotantes
0.0
10.0
35.3055425
25252365.55
-127.2548
35e3 # 35000.0
12E4 # 120000.0
-87.7e100 # -87700000000000000...
15e-5 # 0.00015

1e6 # 1000000.0
1e50 #1000000000000000000000000000000000000000000000000000000000.0
12.514e10 # 125140000000.0 = 12514e7
# 15e-3 = 1 / 10 /10 /10 = 0.015
# 0.1e-20 = 0.0000000000000000000000000000000001


# print("Flotante:", 10.0, type(10.0))

# Complejos
3 + 5j # 3 real, 5 imaginarios -> (3, 5i)
4j # 0 real, 5 imaginarios -> (0, 4i)
-7j # 0 real, -7 imaginarios -> (0, -7i)
1j #

# print("Complejos:", 7j, type(7j))



# Tipos secuenciales: list, tuple, range

# Listas
[]
[1, 2, 3]
["A", "B", "C"]
[1.0, 2, "3", [1, 2, 3]] # En una lista, los elementos pueden ser de cualquier tipo

# print("Listas:", [1, 2, 3], type([1, 2, 3]))

# Tuplas
()
(1, 2, 3)
("A", "B", "C")
(1.0, 2, "3", [1, 2, 3]) # En las tuplas, los elementos tambien pueden ser de cualquier tipo

# print("Tuplas:", (1, 2, 3), type((1, 2, 3)))

# Rangos
range(7) # 0, 1, 2, 3, 4, 5, 6
range(1,10) # 1, 2, 3, 4, 5, 6, 7, 8, 9
range(0,10,2) # 0, 2, 4, 6, 8

# print("Rangos:", range(7), type(range(7)))



# Tipos de mapas: dict
{} # Diccionario vácio
{ "clave": "valor" }
{
    "nombre": "Cesar Diaz",
    "edad": 40,
    "estatura": 1.83
}

# print("Diccionarios:", { "clave": "valor" }, type({ "clave": "valor" }))



# Tipos de conjunto: set, frozenset
# Conjuntos
{ 1 }
{ "a", "b", "c" }
{"abc", 34, True, 40, "male"} 

# print("Conjuntos:", { "a", "b"}, type({ "a", "b"}))



# Tipos booleanos: bool
True
False

# print("Booleanos:", True, type(True))


# Tipos de binarios: bytes, bytearray, memoryview

# Bytes
# print("Bytes:", b"Hello", type(b"Hello"))
# print("Bytearray:", bytearray(5), type(bytearray(5)))
# print("Memoryview:", memoryview(bytes(5)), type(memoryview(bytes(5))))





#-------------------------------------------------------------------------------------------------
# Variables 
#-------------------------------------------------------------------------------------------------
variable_1 = 5
variable_2 = "Cesar"
# print(variable_1, type(variable_1)) # int
# print(variable_2, type(variable_2)) # str

variable_2 = variable_1
# print(variable_2, type(variable_2)) # int

a = 0
A = 0

variable_3 = 325.0
Variable_3 = "Es una variable diferente"
# print(variable_3, Variable_3) # 325.0 Es una variable diferente

# Nombres de variables
mivariable = "John"
mi_variable = "John" # preferido
_mi_variable = "John"
m1iVariable = "John"
MIVARIABLE = "John" # Solo para constantes, pero es sugerido MI_VARIABLE
mivariable2 = "John"


#-------------------------------------------------------------------------------------------------
# Conversiones de tipo
#-------------------------------------------------------------------------------------------------
variable_entera_1 = int(1)   # 1
variable_entera_2 = int(2.8) # 2
variable_entera_3 = int("3") # 3

variable_flotante_1 = float(1000000000000000000)     # 1.0E15
variable_flotante_2 = float(2.8)   # 2.8
variable_flotante_3 = float("3")   # 3.0
variable_flotante_4 = float("4.2") # 4.2

variable_cadena_1 = str("s1") # "s1"
variable_cadena_1 = str(2)    # "2"
variable_cadena_1 = str(3.0)  # "3.0"





#-------------------------------------------------------------------------------------------------
# Operadores aritméticos
#-------------------------------------------------------------------------------------------------
# '+' -> Adición (suma)
adicion_1 = 5 + 3                  # 5 + 3 = 8
adicion_2 = adicion_1 + 10.1       # 8 + 10.1 = 18.1
adicion_3 = adicion_1 + adicion_2  # 8 + 18.1 = 26.1
adicion_3 = adicion_3 + 15         # 26.1 + 15 = 41.1
# print("Operador adición:", adicion_3)

# '-' --> Sustracción (resta)
sustraccion_1 = 35 - 10                       # 35 - 10 = 25
sustraccion_2 = 50.1 - sustraccion_1          # 50.1 - 25 = 25.1
sustraccion_3 = sustraccion_1 - sustraccion_2 # 25 - 25.1 = -0.1
sustraccion_3 = sustraccion_3 - 1             # -0.1 - 1 = -1.1
# print("Operador sustracción:", sustraccion_3)

# '*' --> Multiplicación 
multiplicacion_1 = 5 * 7                  # 5 * 7 = 35
multiplicacion_2 = multiplicacion_1 * 2.0 # 35 * 2.0 = 70.0
multiplicacion_3 = multiplicacion_2 * 0.2 # 70.0 * 0.2 = 14.0 
multiplicacion_3 = multiplicacion_3 * 0.5 # 14.0 * 0.5 = 7.0
# print("Operador multiplicación:", multiplicacion_3)

# '/' --> División (Entera o decimal)
division_1 = 100 / 2          # 100 / 2 = 50
division_2 = division_1 / 4   # 50 / 4 = 12.5
division_3 = division_2 / 0.2 # 12.5 / 0.2 = 62.5 
division_3 = division_3 / 0.5 # 62.5 / 0.5 = 125.0
# print("Operador división:", division_3)

# '//' --> División entera (Parte entera de la división)
division_entera_1 = 100 // 2                 # 100 // 2 = 50
division_entera_2 = division_entera_1 // 4   # 50 // 4 = 12
division_entera_3 = division_entera_2 // 0.2 # 12 // 0.2 = 59.0 # Ojo con el ajuste!!
division_entera_3 = division_entera_3 // 0.5 # 59 // 0.5 = 118.0
# print("Operador división entera:", division_entera_3)

# '%'  --> Módulo (Resto de la división)
modulo_1 = 25 % 2        # 1 => 25 // 2 = 12 y resta 1
modulo_2 = 25 % 7        # 4 => 25 // 7 = 3 y resta 4
modulo_3 = 73 % modulo_2 # 1 => 73 // 4 = 18 y resta 1
# print("Operador módulo:", modulo_3)

# '**' --> Exponenciación ^
exponenciacion_1 = 11 ** 2                 # 121 => 11 * 11
exponenciacion_2 = exponenciacion_1 ** 0.5 # 11.0 => Raiz Cuadrada
exponenciacion_3 = exponenciacion_2 ** 3   # 1331.0 => 11 * 11 * 11
# print("Operador exponenciación:", exponenciacion_3)

# Operadores de asignación aritmética
# '+=' -> Asignación de suma / Incremento a += b <==> a = a + b
asinacion_suma = 110
asinacion_suma += 15   # 125 
asinacion_suma += 10.0 # 135.0 
# print("Operador asignación de suma:", asinacion_suma)

# '-=' --> Asignación de resta / Decremento a -= b <==> a = a - b
asignacion_resta = 110
asignacion_resta -= 15   # 95 
asignacion_resta -= 10.0 # 85.0 
# print("Operador asignación de resta:", asignacion_resta)

# '*=' --> Asignación de multipicación a *= b <==> a = a * b
asignacion_multiplicacion = 110
asignacion_multiplicacion *= 5   # 550
asignacion_multiplicacion *= 0.2 # 110.0
# print("Operador asignación de multiplicación:", asignacion_multiplicacion)

# '/=' --> Asignación de división a /= b <==> a = a / b
asignacion_division = 110
asignacion_division /= 5   # 22.0
asignacion_division /= 0.2 # 110.0
# print("Operador asignación de división:", asignacion_division)

# '//=' --> Asignación de división entera a //= b <==> a = a // b
asignacion_division_entera = 110
asignacion_division_entera //= 5   # 22
asignacion_division_entera //= 0.2 # 109.0
# print("Operador asignación de división entera:", asignacion_division_entera)

# '%=' --> Asignación de módulo  a %= b <==> a = a % b
asignacion_modulo = 111
asignacion_modulo %= 5   # 1
asignacion_modulo %= 0.2 # 0.1999999...
# print("Operador asignación de módulo:", asignacion_modulo)
# '**=' --> Asignación de exponenciación  a **= b <==> a = a ** b
asignacion_exponenciacion = 1
asignacion_exponenciacion **= 5   # 1
asignacion_exponenciacion **= 0.2 # 1.0
# print("Operador asignación de exponenciación:", asignacion_exponenciacion)

#-------------------------------------------------------------------------------------------------
# Precedencia en operadores aritméticos
#-------------------------------------------------------------------------------------------------
# 1. Parentesis ( )
# 2. Exponenciación **
# 3. Negación de expresiones -
# 4. Multiplicación *, División /, División entera //, Módulo %
# 5. Adición +, Sustracción -
# 6. Asignación =

13 - 4 * ( 5 - 2 ) + 3 * ( 2 + 8 )
13 - 4 *      3     + 3 *     10
13 -   12          +      30
31

ejercicio_1 = 16 + 3 * (6 - 4) - 3 * 5
print("Ejercicio 1", ejercicio_1)

ejercicio_2 = 23 - 8 + 6 * 2 - 3 * 4 
#print("Ejercicio 2", ejercicio_2)

ejercicio_3 = 6 * (7 * 5 - 4 * 6) + 81 / 9 - 6
#print("Ejercicio 3", ejercicio_3)

ejercicio_4 = 6 * 4 + 3 * (450 / 10 - 5 * (3 + 2))
#print("Ejercicio 4", ejercicio_4)

ejercicio_5 = 5 * 6 / 2 - (12 - 3) * 2
#print("Ejercicio 5", ejercicio_5)
