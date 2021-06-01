# JSON - JavaScript Object Notation
"""
[{
    "nombre": "Cesar Diaz",
    "email": "cesar.a.diaz@gmail.com"
    "edad": 41,
    "profesor": true
},
{
    "nombre": "Sebastian Murillo",
    "email": "sebastian.murillo@gmail.com"
    "edad": 30,
    "profesor": false
}]
"""
import json

def crear_archivo():
    datos = [{
        "nombre": "Cesar Diaz",
        "email": "cesar.a.diaz@gmail.com",
        "edad": 41,
        "profesor": True
    },
    {
        "nombre": "Sebastian Murillo",
        "email": "sebastian.murillo@gmail.com",
        "edad": 30,
        "profesor": False
    }]

    with open('usuarios.json', "w") as archivo:
        json.dump(datos, archivo, indent=2)

def leer_archivo():
    with open("usuarios.json") as archivo:
        datos = json.load(archivo)

        for dato in datos:
            print(dato, type(dato))

