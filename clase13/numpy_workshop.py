import numpy as np

# Array de 1 dimension
a = np.array([4, 7, 5]); print(a, "\n")
print(a.shape, "\n")
a[1] = 2
print(a, "\n")

# Matriz (2 dimensiones)
b = np.array([[1,2,3],[4,5,6]]); print(b, "\n")
print(b.shape, "\n") 
print(b[0, 0], b[0, 1], b[1, 0], "\n")

# Generar una matrices básicas
print(np.zeros((4, 3)), "\n")
print(np.ones((3, 4)), "\n")
print(np.identity(5), "\n")
print(np.eye(4,3), "\n")

# Generar valores 
print(np.arange(1, 30, 2), "\n")
print(np.arange(30, 1, -2, dtype=float), "\n")
print(np.arange(1, 30, 2).reshape(3, 5), "\n")
print(np.arange(1, 32, 2).reshape(4, 4), "\n")

print(np.linspace(1, 10, 10), "\n")
print(np.linspace(2, 4, 10), "\n")
print(np.linspace(-2, 4, 30), "\n")

print(np.random.random((3,3)), "\n")

print(np.array([x**3 for x in range(3,20,3)]).reshape((3,2)), "\n")

# Operaciones con vectores (arrays)
a=np.arange(5) # array([0, 1, 2, 3, 4])
b=np.array([2, 4, 0, 1, 2])

print(a - b, "\n")
print(b**2, "\n")
print(2 * b, "\n")
print(a * b, "\n")

print(b > 2, "\n")
print(b > a, "\n")

print(a.dot(b), "\n") # Producto Punto

# Funciones
print(np.sin(a), "\n")

print(np.sum(a), "\n")
print(np.mean(a), "\n")

print(np.max(a), "\n")
print(np.min(a), "\n")

# Operaciones con matrices
x=np.array([[1,1],[0,1]]); print(x, "\n")
y=np.array([[2,0],[3,4]]); print(y, "\n")
print(x * y, "\n")
print(x.dot(y), "\n")

print(np.cross(x, y), "\n")   # Producto Cruz

print(np.linalg.inv(x), "\n") # Matriz inversa x
print(np.linalg.inv(y), "\n") # Matriz inversa y
print(x.dot(np.linalg.inv(x)), "\n") #  El producto punto de X con su inversa genera la Identidad

print(y.diagonal(), "\n")            # Diagonal de la matriz
print(np.fliplr(y).diagonal(), "\n") # Diagonal invertida

print(x.sum(), "\n")
print(x.sum(axis = 0), "\n") # columnas
print(x.sum(axis = 1), "\n") # filas

# Operaciones estadísticas
z = np.random.random((3,4)); print(z, "\n")
print(np.mean(z), np.median(z), np.std(z), "", sep="\n")

# Extraer datos de matrices
data_set=np.random.random((5,10)); print(data_set, "\n")
print(data_set[1], "\n")
print(data_set[1][0], "\n")
print(data_set[1,0], "\n")
print(data_set[2:4], "\n")
print(data_set[2:4,0], "\n")
print(data_set[2:4,0:2], "\n")
print(data_set[:, 0], "\n")
print(data_set[2:5:2], "\n")
print(data_set[:2], "\n")
print(data_set[2:4,::2], "\n")
