t = 'a', 'b', 'c', 'd', 'e', 7
print(t)

t = ('esto es una cadena', 'b', 'c', 'd', 'e')
print(t)

t = tuple('lupines')
print(t) # ('l', 'u', 'p', 'i', 'n', 'e', 's')
print(t[1:3])

# Comprobando tuplas

# Creando listas desde textos
txt = "but soft what light in yonder window breaks"
palabras = txt.split() # ['but', 'soft', 'what', 'light', 'in', 'yonder', 'window', 'breaks']

l = list()
for subcadena in palabras:
    l.append((len(subcadena), subcadena))
print(l) # [(3, 'but'), (4, 'soft'), (4, 'what'), (5, 'light'), (2, 'in'), (6, 'yonder'), (6, 'window'), (6, 'breaks')]

l.sort(reverse=True)
print(l) # [(6, 'yonder'), (6, 'window'), (6, 'breaks'), (5, 'light'), (4, 'what'), (4, 'soft'), (3, 'but'), (2, 'in')]

res = list()
for longitud, palabra in l: # (6, "window")
    res.append(palabra)
print(res) # ['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']

# Asignacion de una tupla
m = ['have', 'fun']
x, y = m

addr = 'monty@python.org'
uname, domain = addr.split('@') # uname = addr.split('@')[0]; domain = addr.split('@')[1] 

# Metodos
valores = ("Python", True, "Zope", 5, False)
print("True ->", valores.count(True)) # 'True -> 1'

print(valores.index(True)) # 1 

# "nombre;apellidos;edad;estado"
linea = "Cesar;Diaz;40;True"
nombre, apellido, edad, estado = linea.split(sep=";")
print(nombre, apellido, int(edad), bool(estado))

