"""
* Series: Estructura de una dimensión.
* DataFrame: Estructura de dos dimensiones (tablas).
* Panel: Estructura de tres dimensiones (cubos).
"""
import pandas as pd
import numpy as np

# Series(data=lista, index=indices, dtype=tipo) : Devuelve un objeto de tipo Series
#     con los datos de la lista lista, las filas especificados en la lista indices
#     y el tipo de datos indicado en tipo. 
s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string'); print(s, "\n")

s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5}); print(s, "\n")
print(s[1:3], "\n")
print(s['Economía'], "\n")
print(s[['Programación', 'Matemáticas']], "\n")

# Filtrar la serie
print(s > 5, "\n")
print(s[s > 5], "\n")

s = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]); print(s)
print(s.size)
print(s.index)
print(s.count())
print(s.sum())
print(s.cumsum())
print(s.value_counts())
print(s.value_counts(normalize=True))
print(s.min())
print(s.max())
print(s.mean())
print(s.std())
print(s.describe(), "\n")

# Aplicar una función       
s = pd.Series(['a', 'b', 'c']); print(s)
print(s.apply(str.upper), "\n")
print(s.apply(lambda x : str(x)+"123"), "\n")

# DataFrame(data=diccionario, index=filas, columns=columnas, dtype=tipos) :
#     Devuelve un objeto del tipo DataFrame cuyas columnas son las listas contenidas
#     en los valores del diccionario diccionario, los nombres de filas indicados en
#     la lista filas, los nombres de columnas indicados en la lista columnas y los
#     tipos indicados en la lista tipos.
datos = {
    'nombre' : ['María', 'Luis', 'Carmen', 'Antonio'],
    'edad' : [18, 22, 20, 21],
    'grado' : ['Economía', 'Medicina', 'Arquitectura', 'Economía'],
    'correo' : ['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
}
df = pd.DataFrame(datos);
print(df, "\n")

df = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad']);
print(df, "\n")

df = pd.DataFrame(np.random.randn(4, 3), columns=['a', 'b', 'c']);
print(df, "\n")

df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df, "\n")
print(df.describe(), "\n")
print(df.loc[2, 'colesterol'], "\n")
print(df.loc[:3, ('colesterol','peso')], "\n")
print(df['colesterol'], "\n")

# Agregar una nueva serie
df['diabetes'] = pd.Series([False, False, True, False, True])
print(df, "\n")

print(df['altura'].apply(lambda x : x * 100), "\n")

print(df.groupby('sexo').groups, "\n")
print(df.groupby(['sexo','edad']).groups, "\n")
print(df.groupby('sexo').agg(np.mean), "\n")

datos = {
    'nombre':['María', 'Luis', 'Carmen'],
    'edad':[18, 22, 20],
    'Matemáticas':[8.5, 7, 3.5],
    'Economía':[8, 6.5, 5],
    'Programación':[6.5, 4, 9]}
df = pd.DataFrame(datos)
print(df, "\n")

df1 = df.melt(id_vars=['nombre', 'edad'], var_name='asignatura', value_name='nota')
print(df1, "\n")

print(df1.pivot(index=['nombre', 'edad'], columns='asignatura', values='nota'), "\n")

print(df1.pivot(index='nombre', columns='asignatura', values='nota'), "\n")