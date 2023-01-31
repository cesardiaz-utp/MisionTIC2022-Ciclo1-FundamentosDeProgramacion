from operator import concat


nombre = input('Nombre: ')
apellido = input('Apellido: ')

def NombreCompleto(a, b):
    r = f'Nombre Completo: {a} {b}' 
    return r;
    

print(NombreCompleto(nombre, apellido))