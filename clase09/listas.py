# Definición de una lista
lista = [1, 2.5, 'MisiónTIC2022', [5,6], {"nombre":"Cesar", "apellido":"Diaz"}, True]

# Navegando en la lista
print(lista[0]) # 1
print(lista[1]) # 2.5
print(lista[2]) # 'MisiónTIC2022'
print(lista[2][5]) # 'n'
print(lista[3]) # [5,6]
print(lista[3][0]) # 5
print(lista[3][1]) # 6
print(lista[4]["nombre"] + " " + lista[4]["apellido"]) # 'Cesar Diaz'

print('Hicimos este cambio ->',lista[1:4]) # [2.5, 'MisiónTIC2022', [5,6]]
print(lista[1:6]) # [2.5, 'MisiónTIC2022', [5, 6], {"nombre":"Cesar", "apellido":"Diaz"}, True]
print(lista[1:6:2]) # [2.5, [5, 6], True]
print(lista[-4:-1]) # ['MisiónTIC2022', [5, 6], {'nombre': 'Cesar', 'apellido': 'Diaz'}]
print("Hola Estructura de Lenguajes")

lista = []
lista = list()

nombre = "Pepe"
edad = 25
lista = [nombre, edad]
print(lista) # ["Pepe", 25]

nombres = ["Ana", "Bernardo"]
edades = [22.0, 21]
lista = [nombres, edades]
print(lista) # [["Ana", "Bernardo"], [22.0, 21]]

nombres += ["Cristina"] # nombres = nombres + ["Cristina"]
print(lista)  # [["Ana", "Bernardo", "Cristina"], [22.0, 21]]

#for letra in nombre:
#    print(letra)

#for var in coleccion:
#    var
#    pass

for elemento in lista:
    tam = len(elemento); print(elemento, tam, sep=" -> ") # elemento = [22.0, 21]
    if tam > 0:
        for dato in elemento: # dato = 22.0
            if isinstance(dato, int) or isinstance(dato, float): #str type(dato) -> <class int>
                print(dato, "no es una colección")
            else:
                print(dato, len(dato), sep=" -> ")

len(lista)       # 2
len(lista[0])    # 3
len(lista[0][1]) # len("Bernardo") -> 8



# Metodos
versiones = [2.5, 3.6, 4, 5]
#versiones += [6]
versiones.append(6) # [2.5, 3.6, 4, 5, 6]
print(versiones)

print("6 ->", versiones.count(6)) # "6 -> 1"

versiones.extend([4]) # [2.5, 3.6, 4, 5, 6, 4]
versiones.extend(range(5,7)) # [2.5, 3.6, 4, 5, 6, 4, 5, 6]

print(versiones.index(4))    # 2
print(versiones.index(4, 3)) # 5
# print(versiones.index(4, 6)) # Error != -1

versiones.insert(2, 3.7) # [2.5, 3.6, 3.7, 4, 5, 6, 4, 5, 6]

print(versiones.pop()) # 6
print(versiones)       # [2.5, 3.6, 3.7, 4, 5, 6, 4, 5]

versiones.remove(2.5)
#versiones.remove([4, 5])
print(versiones)       # [3.6, 3.7, 4, 5, 6, 4, 5]
#for dato in [4, 5]:
#    versiones.remove(dato)

versiones.reverse()
print(versiones)       # [5, 4, 6, 5, 4, 3.7, 3.6]

versiones.sort()
print(versiones)       # [3.6, 3.7, 4, 4, 5, 5, 6]
versiones.sort(reverse=True)
print(versiones)       # [6, 5, 5, 4, 4, 3.7, 3.6]

versiones.clear()      # []

del versiones          # versiones = None


# Convirtiendo una cadena a lista
mensaje = "Hola, como estas tu?"
print(mensaje.split()) # ['Hola,', 'como', 'estas', 'tu?']

for palabra in mensaje.split():
    print(palabra)



# Iterar sobre dos o más secuencias usando zip
preguntas = ['nombre', 'objetivo', 'sistema operativo']
respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']

for pregunta, respuesta in zip(preguntas, respuestas):
    print('¿Cual es tu {}?, la respuesta es: {}.'.format(pregunta, respuesta))



# Iterar por una cadena con salto
mensaje = "Hola, como estas tu?"
print(mensaje[::3])

mensaje[2] = 'i'

# Extrae vocales del mensaje
vocales = 'aeiou'
for letra in mensaje:
     if letra in vocales:
            print(letra, end=" ")
print()
# Extrae consonantes del mensaje
vocales = 'aeiou'
for letra in mensaje:
     if letra not in vocales and letra != " ":
            print(letra, end=" ")
print()