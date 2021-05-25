# Lists Comprehension

frutas = ["manzana", "banano", "cereza", "kiwi", "mango"]
list = [x for x in frutas if "a" in x]

list = [x for x in frutas if x != "manzana"] 

list = [x for x in range(10) if x < 5] 

list = [x.upper() for x in frutas] 

list = [ x + y for x in [10,30,50] for y in [20,40,60]]

list = [x if x != "banano" else "naranja" for x in frutas] 

# Otros ejemplos
oracion = 'El cohete se devuelve desde marte'
vocales = [i for i in oracion if i in 'aeiou']

def es_consonante(letra: str):
    vocales = 'aeiou'
    return letra.isalpha() and letra.lower() not in vocales
consonantes = [i for i in oracion if es_consonante(i)]

precios_originales = [1250, -9450, 10220, 3780, -5920, 1160]
precios = [i if i > 0 else 0 for i in precios_originales]

# Con conjuntos
oracion = 'El cohete se devuelve desde marte'
vocales_usadas = {i for i in oracion if i in 'aeiou'}

# Con diccionarios
cuadrados = { str(i): i * i for i in range(10)}

pass


