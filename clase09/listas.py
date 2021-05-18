# Definición de una lista
lista = [1, 2.5, 'MisiónTIC2022', [5,6] , {"nombre":"Cesar", "apellido":"Diaz"}]

# Navegando en la lista
print(lista[0]) # 1
print(lista[1]) # 2.5
print(lista[2]) # MisiónTIC2022
print(lista[3]) # [5,6]
print(lista[3][0]) # 5
print(lista[3][1]) # 6
print(lista[4]["nombre"] + " " + lista[4]["apellido"]) # 'Cesar Diaz'

print('Hicimos este cambio ->',lista[1:4]) # [2.5, 'DevCode']
print(lista[1:6]) # [2.5, 'DevCode', [5, 6], {"nombre":"Cesar", "apellido":"Diaz"}]
print(lista[1:6:2]) # [2.5, [5, 6]]
print("Hola Estructura de Lenguajes")

lista = []

nombre = "Pepe"
edad = 25
lista = [nombre, edad]
print(lista)

nombres = ["Ana", "Bernardo"]
edades = [22, 21]
lista = [nombres, edades]
print(lista)

nombres += ["Cristina"]
print(lista)

len(lista)
len(lista[0])

# Metodos
versiones = [2.5, 3.6, 4, 5]
versiones.append(6) # [2.5, 3.6, 4, 5, 6]
print(versiones)

print("6 ->", versiones.count(6)) # "6 -> 1"

versiones.extend([4]) # [2.5, 3.6, 4, 5, 6, 4]
versiones.extend(range(5,7)) # [2.5, 3.6, 4, 5, 6, 4, 5, 6]

print(versiones.index(4))    # 2
print(versiones.index(4, 4)) # 5

versiones.insert(2, 3.7) # [2.5, 3.6, 3.7, 4, 5, 6, 4, 5, 6]

print(versiones.pop()) # 6
print(versiones)       # [2.5, 3.6, 3.7, 4, 5, 6, 4, 5]

versiones.remove(2.5)
print(versiones)       # [3.6, 3.7, 4, 5, 6, 4, 5]

versiones.reverse()
print(versiones)       # [5, 4, 6, 5, 4, 3.7, 3.6]

versiones.sort()
print(versiones)       # [3.6, 3.7, 4, 4, 5, 5, 6]
versiones.sort(reverse=True)
print(versiones)       # [6, 5, 5, 4, 4, 3.7, 3.6]



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
print(mensaje[::2])

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