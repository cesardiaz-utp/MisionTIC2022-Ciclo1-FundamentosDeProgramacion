#
# Función map(function, iterable(s))
#
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
def starts_with_A(s):
    return s[0] == "A"
lista = list(map(starts_with_A, fruit))         # [True, False, False, True, False]

lista = list(map(lambda s: s[0] == "A", fruit)) # [True, False, False, True, False]

# Varias listas a la vez
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

#
# Función filter(function, iterable(s))
#
lista = list(filter(starts_with_A, fruit))      # ['Apple', 'Apricot']

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes)) # ['madam', 'anutforajaroftuna']

#
# Función reduce(function, sequence[, initial])
#
from functools import reduce

lista = [2, 4, 7, 3]
valor = reduce(lambda x, y: x + y, lista)      # 16

valor = reduce(lambda x, y: x + y, lista, 10)  # 26

#
# Función zip(*iterables)
#
a = [1, 2]
b = ["Uno", "Dos"]
list(zip(a, b)) # [(1, 'Uno'), (2, 'Dos')]

numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
list(zip(numeros, espanol, ingles, frances)) # [(1, 'Uno', 'One', 'Un'), (2, 'Dos', 'Two', 'Deux')]

# Cancelar el zip()
c = [(1, 'One'), (2, 'Two'), (3, 'Three')]
a, b = zip(*c)
print(a)  # (1, 2, 3)
print(b)  # ('One', 'Two', 'Three')


#
# Función enumerate(iterables)
#
lenguajes = ["Java", "C", "C++", "Rust", "Elixir"]
list(enumerate(lenguajes)) # [(0, 'Java'), (1, 'C'), (2, 'C++'), (3, 'Rust'), (4, 'Elixir')]

list(enumerate(lenguajes, 1)) # [(1, 'Java'), (2, 'C'), (3, 'C++'), (4, 'Rust'), (5, 'Elixir')]

#
# Función all(iterables)
# Función any(iterables)
#
print(all([True, False, True])) # False
print(any([True, False, True])) # True

print(all([]))                  # True
print(any([]))                  # False


"""
La empresa ABCD tiene hasta 100 empleados. La compañía decide crear un número
de identificación único UID para cada uno de sus empleados. La compañía le ha
asignado la tarea de validar los UIDsgenerados aleatoriamente. Un UID válido debe
cumplir con las siguientes reglas:
* Debe contener por lo menos dos letras mayúsculas en el alfabeto inglés.
* Debe tener por lo menos 3 dígitos.
* Contener únicamente dígitos alfanuméricos.
* No tener repeticiones.
* Contener exactamente 10 caracteres.
"""
uids = ["B1CD102354", "B1CDEF2354"]
for uid in uids:
    cond = []
    # Debe contener por lo menos dos letras mayúsculas en el alfabeto inglés.
    cond.append( len(list(filter(lambda x: x.isupper(), list(uid)))) >= 2 )
    # Debe tener por lo menos 3 dígitos.
    cond.append( len(list(filter(lambda x: x.isdigit(), list(uid)))) >= 3 )
    # Contener únicamente dígitos alfanuméricos.
    cond.append( len(list(filter(lambda x: not(x.isalnum()), list(uid)))) == 0 )
    # No tener repeticiones.
    cond.append( len(uid) == len(set(uid)) )
    # Contener exactamente 10 caracteres.
    cond.append( len(uid) == 10 )

    print("Válido") if all(cond) else print("Inválido")
