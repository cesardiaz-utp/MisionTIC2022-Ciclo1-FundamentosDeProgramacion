#-------------------------------------------------------------------------------------------------
# Funciones del sistema
#-------------------------------------------------------------------------------------------------
# abs(x)   # Valor absoluto.
print(abs(50))   # 50
print(abs(-50))  # 50
print(abs(-2.5)) # 2.5

# chr(i)   # Devuelve una cadena de un solo carácter: aquél cuyo código ASCII es i.
print(chr(72))  # "H"
print(chr(123)) # "{"

# eval(s)  # Evalúa s interpretándola como una expresión Python.
print(eval("6 / 2 * ( 2 + 1 )")) # 9
print(eval("3**5"))              # 243

# len(s)   # Devuelve la longitud de la secuencias.
print(len("Hola Mundo!")) # 11

# max(s)   # Devuelve el máximo de la secuencias.
print(max(10, 30, 40, 20))     # 40
print(max("A", "B", "Z", "G")) # Z

# min(s)   # Devuelve el mínimo de la secuencias.
print(min(10, 30, 40, 20))     # 10
print(min("A", "B", "Z", "G")) # A

# ord(c)   # Devuelve el código ASCII del carácter c.
print(ord("H")) # 72
print(ord("{")) # 123

# round(f[, p]) # Redondea un número flotante f a una precisión p (por defecto 0 dígitos).
print(round(135.561))    # 136
print(round(135.315))    # 135
print(round(135.561, 1)) # 135.6
print(round(135.561, 2)) # 135.56

# help(c)  # Invoca el menú de ayuda del intérprete de Python
help(print)