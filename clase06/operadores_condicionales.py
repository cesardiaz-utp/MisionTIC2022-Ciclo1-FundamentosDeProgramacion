# Valores posibles del tipo de datos 'bool'
True
False

# Creando proposiciones usando operadores de comparación
# Igual
print(5 == 5.0) # True
print("hola" == "Hola") # False
print("Hola " == "Hola") # False

# Diferente
print(5 != 5.0) # False
print("hola" != "Hola") # True
print("Hola " != "Hola") # True


# Menor que
print(5.01 < 5.10) # True
print("hola" < "Hola") # False
print("Hola " < "Hola ") # False

# Menor o igual a que
print(5 <= 5.00) # True
print("hola" <= "Hola") # False
print("HoLa " <= "Hola") # False

# Mayor que
print(5.01 > 5.10) # False
print("hola" > "Hola") # True

# Mayor o igual que
print(5 >= 5.00) # True
print("hola" >= "Hola") # True

# Son el mismo 
print(5 is 5.0) # False
var_1 = 5.0
print(var_1 is (1 + 2 + 2.0)) # True

print(5 is not 5.0) # True


# Operadores lógicos (Conectores)
# and # Conjuncion, adición
# or # Disyuncion, comparación
var_2 = 10
p = var_2 >= 5 and var_2 <= 10
print("p:",p)

q = var_1 < var_2 or var_1 >= var_2 - 5
print("q:",q)

r = var_1 > var_2 and var_1 == 5 or var_2 > var_1 + 3
print("r:",r)


