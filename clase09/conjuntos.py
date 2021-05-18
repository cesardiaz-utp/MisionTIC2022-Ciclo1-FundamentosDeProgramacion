s = {1, 2, 3, 4}

s = {True, 3.14, None, False, "Hola mundo", (1, 2)}

s1 = set([1, 2, 3, 4])
s2 = set(range(10))
print(s1)  # {1, 2, 3, 4}
print(s2)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

a = set('Hola Pythonista')
print(a)   # {'h', ' ', 's', 'n', 'i', 'y', 'H', 'l', 't', 'a', 'o', 'P'}

# Acceder a los elementos de un conjunto
mi_conjunto = {1, 3, 2, 9, 3, 1}
print(mi_conjunto)        # {1, 2, 3, 9}
for numero in mi_conjunto:
    print(numero)

# Metodos
set_mutable = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable.add(22.000001)
print(set_mutable)   # {1, 2, 3, 4, 5, 7, 11, 22.000001}

set_mutable.clear()
print(set_mutable)   # set()


set_mutable = set([4.0, 'Carro', True])
otro_set_mutable = set_mutable.copy()
print(set_mutable == otro_set_mutable)        # True

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4]) # {1, 2, 3, 4, 5, 7, 11}
set_mutable2 = set([11, 5, 9, 2, 4, 8])       # {2, 4, 5, 8, 9, 11}
print(set_mutable1.difference(set_mutable2))  # {1, 3, 7}
print(set_mutable2.difference(set_mutable1))  # {8, 9}

a = {1, 2, 3, 4}
b = {2, 3}
c = a - b
print(c)  # {1, 4}

proyecto1 = {'python', 'Zope2', 'ZODB3', 'pytz'}
proyecto2 = {'python', 'Plone', 'diazo'}
proyecto1.difference_update(proyecto2)
print(proyecto1)    # proyecto1 = {'python', 'Zope2', 'ZODB3', 'pytz'}

paquetes = {'python', 'zope', 'plone', 'django'}
paquetes.discard('django') # {'python', 'zope', 'plone'}
paquetes.discard('php')    # {'python', 'zope', 'plone'}

print(set_mutable1.intersection(set_mutable2)) # {2, 11, 4, 5}
print(set_mutable2.intersection(set_mutable1)) # {2, 11, 4, 5}

print(set_mutable1.union(set_mutable2))        # {1, 2, 3, 4, 5, 7, 8, 9, 11}

# Conjuntos inmutables
s1 = frozenset([1, 2, 3, 4])

print(set("HolaMundo"))