# Recursión

![Muñecas Rusas](https://miro.medium.com/max/700/0*opEAS5f4H5qOnETV.jpg)

![Recursividad](https://cdn-images-1.medium.com/max/1200/1*AX103NrmJFS5s4lsNRJTYg.jpeg)

## Fractales 
Los fractales son una aplicación de la recursividad, ya que se van aplicando el mismo partón una y otra vez sobre la figura hasta el infinito.

### Curva de Koch
![Curva de Koch](https://www.matesfacil.com/fractales/von-Koch/Snowflake/3/Koch_snowflake_mini.gif)

### Fractal de Cesàro
![Fractal de Cesàro](https://www.matesfacil.com/fractales/von-Koch/Cesaro/Mini_Cesaro_fractal_gif.gif)

### La salchicha de Minkowski
![La salchicha de Minkowski](https://www.matesfacil.com/fractales/von-Koch/T2/T2_fractal_gif.gif)

### Triángulo de Sierpinski
![Triángulo de Sierpinski 1](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Animated_construction_of_Sierpinski_Triangle.gif/581px-Animated_construction_of_Sierpinski_Triangle.gif)

![Triángulo de Sierpinski 2](https://upload.wikimedia.org/wikipedia/commons/6/6b/Sierpinski_zoom_2.gif)

# Funciones recursivas

Funciones recursivas que son aquellas que se llaman a sí mismas.

## Cuenta regresiva
```python
def cuenta_regresiva(numero):
    # Algoritmo
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero - 1)
    else:
        print("Boooooooom!")
```

## Factorial
### Definición
```
factorial(0) = 1
factorial(n) = n * factorial(n - 1)
```
### Solución
```python
def factorial(n):
    # Validar
    if n < 0:
        return "Número erróneo"

    # Algoritmo
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

## Fibonacci
### Definición
```
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
```
### Solución
```python
def fibonacci(n):
    # Validar
    if n < 0:
        return "Número erróneo"

    # Algoritmo
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

## Máximo común divisor
### Definición
```
mcd(x, y):-
    si y == 0 ==> x
    si y > 0 ∧ x >= y ==> mcd(y, mod(x,y))  
```
### Solución
```python
def mcd(x, y):
    # Validar
    if y < 0:
        return "No puede buscar divisores si hay números negativos"

    # Algoritmo
    if y == 0:
        return x
    if x >= y:
        return mcd(y, x % y) 
    else:
        return mcd(y, x)
```

## Torres de Hanoi

![Juego torre de colores](https://ae01.alicdn.com/kf/HTB1WErAbovrK1RjSszfq6xJNVXa4/Juguete-educativo-cl-sico-para-edades-tempranas-juego-de-rompecabezas-matem-tico-de-madera-de-torre.jpg_q50.jpg)

Las Torres de Hanói es un rompecabezas o juego matemático inventado en 1883 por el matemático francés Édouard Lucas. Este juego de mesa individual consiste en un número de discos perforados de radio creciente que se apilan insertándose en uno de los tres postes fijados a un tablero. El objetivo del juego es trasladar la pila a otro de los postes siguiendo ciertas reglas, como que no se puede colocar un disco más grande encima de un disco más pequeño. El problema es muy conocido en la ciencia de la computación y aparece en muchos libros de texto como introducción a la teoría de algoritmos. 

![Torres de Hanoi](https://upload.wikimedia.org/wikipedia/commons/8/8d/Iterative_algorithm_solving_a_6_disks_Tower_of_Hanoi.gif)

### Solución
```python
def hanoi(discos, torre_a, torre_b, torre_c):
    if discos == 1:
        print(f"Mover disco {discos} de la torre {torre_a} a la torre {torre_c}")
    else:
        hanoi(discos - 1, torre_a, torre_c, torre_b)

        print(f"Mover disco {discos} de la torre {torre_a} a la torre {torre_c}")

        hanoi(discos - 1, torre_b, torre_a, torre_c)
```
