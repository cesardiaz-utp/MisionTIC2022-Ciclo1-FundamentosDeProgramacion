###########################################################
# Lo que sabemos 
###########################################################
nombre = "Cesar" # 'Cesar'
edad = 40

# Lo que sabemos hasta ahora
print("Hola ", nombre," y su edad es ", edad, "!", sep="")
print(f"Hola {nombre} y su edad es {edad + 1}!")
print("Hola " + nombre + " y su edad es " + str(edad) + "!")
print("Hola {} y su edad es {}!".format(nombre, edad))

plantilla = "Hola {} y su edad es {}!"
print(plantilla.format(nombre, edad))

plantilla = "Hi {} and you are {} years old!"
print(plantilla.format(nombre, edad))

###########################################################
# Lo nuevo 
###########################################################

# Conjunto de caracteres
nombre = "Cesar "
letra = nombre[0]      # C
print(letra)

# C e s a r _
# 0 1 2 3 4 5
letra = nombre[5]      # r
print(letra)

longitud = len(nombre) # 6
print(longitud)

         #0123456789012345678901234567 # 28 caracteres, indices del 0 al 27
cadena = "esto es una cadena muy larga"
print(cadena[0])                 # 
print(cadena[len(cadena) - 1])   # Ultima letra
print("cadena[-1]:", cadena[-1]) # 
print("cadena[-2]:", cadena[-2]) # 

print(cadena[13]) 

# Subcadenas
         #0123456789012345678901234567 # 28 caracteres, indices del 0 al 27
cadena = "esto es una cadena muy larga"
print(cadena[0:10])  # 'esto es un' [0,10) i >= 0 and i < 10
print(cadena[1:5])   # 'sto '
print(cadena[13:15]) # 'ad'
print(cadena[20:25]) # 'uy la'

#Rangos
print(cadena[:15])   # 'esto es una cad'
print(cadena[15:])   # 'ena muy larga'
print(cadena[15:15]) # ''
print(cadena[:])     # 'esto es una cadena muy larga'

print(cadena[15:1])  # ''

print(cadena[-5:-1]) # ''

# Operaciones
print("Hola " + "Mundo!")   # 'Hola Mundo!'
print("Hola " * 3)           # 'Hola Hola Hola '

cadena = "esto es una Cadena muy Larga. y esto?"
print(cadena.capitalize())  # 
print(cadena.upper())       # 
print(cadena.lower())       # 

# Busquedas en cadenas
print(cadena.find("d"))     # 
print(cadena.find("L"))     # 
print(cadena.find("l"))     # 
print(cadena.find("a"))     # 
print(cadena.find("a", 11)) # 

# Separar la cadena en 2 partes por el carácter '.' punto,
#   donde cada parte debe estar con mayúscula inicial.
#   
cadena = "esto es una Cadena muy Larga. y esto?"
pos_punto = cadena.find(".") # 28
parte_1 = cadena[:pos_punto].capitalize() # 'esto es una Cadena muy Larga'
parte_2 = cadena[pos_punto+1:].strip().capitalize() #

# invertir cadenas (slicing)
print(cadena[::-1]) # '?otse y .agraL yum anedaC anu se otse'

#%s cadenas
#%d enteros
#%f flotantes
print("Hola %s y su edad es %d y su estatura es de %0.2f!" % (nombre.strip(), edad, 1.83))
