def cuenta_regresiva(numero):
    # Algoritmo
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero - 1)
    else:
        print("Boooooooom!")

def factorial(n):
    # Validar
    if n < 0:
        return "Número erróneo"

    # Algoritmo
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

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
        num_1=fibonacci(n - 1)
        num_2 =fibonacci(n - 2)
        print(num_1+num_2)
        return num_1 + num_2

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

def hanoi(discos, torre_a, torre_b, torre_c):
    if discos == 1:
        print(f"Mover disco {discos} de la torre {torre_a} a la torre {torre_c}")
    else:
        hanoi(discos - 1, torre_a, torre_c, torre_b)
        
        print(f"Mover disco {discos} de la torre {torre_a} a la torre {torre_c}")

        hanoi(discos - 1, torre_b, torre_a, torre_c)