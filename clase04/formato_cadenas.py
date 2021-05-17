def mayor_de_numeros(num_1 = 0, num_2 = 0):
    resultado = max(num_1, num_2)
    return "El valor mayor enviado es " + str(resultado)

def promedio_numeros(num_1, num_2, num_3):
    promedio = (num_1+ num_2 + num_3) / 3
    return f"El promedio de los números {num_1}, {num_2} y {num_3+1} es {round(promedio,2)}"

def suma(num_1, num_2):
    var_1 = num_1+ num_2
    return "La suma de los números {} y {} es {}".format(num_1, num_2, var_1)