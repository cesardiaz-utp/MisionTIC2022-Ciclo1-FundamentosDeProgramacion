#-------------------------------------------------------------------------------------------------
# Llamar funciones de bibliotecas
# https://docs.python.org/3/py-modindex.html
#-------------------------------------------------------------------------------------------------
# Opcion 1
import math
print(math.sin(2.0))

# Opcion 2
import turtle as t
t.forward(200)
t.right(90)


# Opcion 3
from random import random, randrange, choice
print(random(), random()) # Numeros decimales aleatorios del 0 a 1
print(randrange(10))      # Numeros decimales aleatorios 0 y el 9
print(choice(["win","lose","draw"])) # Elige un elemento aleatorio de la lista
