# JSON - JavaScript Object Notation
"""
[{
    "nombre": "Cesar Diaz",
    "email": "cesar.a.diaz@gmail.com",
    "edad": 41,
    "profesor": true
},
{
    "nombre": "Sebastian Murillo",
    "email": "sebastian.murillo@gmail.com",
    "edad": 30,
    "profesor": false
}]
"""
import json

def crear_archivo(nombre_archivo="usuarios.json"):
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
    #print(datos)
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=2)

#crear_archivo()

def leer_archivo():
    with open("usuarios.json") as archivo:
        datos = json.load(archivo)

        for dato in datos:
            print(dato, type(dato))

            print(dato["nombre"])
            if dato["profesor"]:
                grupos = []
                for grupo in dato["grupos"]:
                    grupos.append(grupo["numero"])
                print("Los grupos del profesor son:", grupos)

#leer_archivo()

def crear_archivo_2():
    datos = {
        '01': {
            'descripcion': 'Ir a mercar',
            'estado': 'pendiente',
            'tiempo': 60
        },
        '02': {
            'descripcion': 'Estudiar',
            'estado': 'pendiente',
            'tiempo': 180
        },
        '03': {
            'descripcion': 'Hacer ejercicio',
            'estado': 'pendiente',
            'tiempo': 50
        },
        "04": {
            'descripcion': "Clase de programacion",
            'estado': 'En curso',
            'tiempo': 120
        }
    }

    with open('tareas.json', "w") as archivo:
        # json.dump(datos, archivo, indent=2)
        json.dump((1, 2, 3, 4, 5), archivo)

    with open('tareas.json', "r") as archivo:
        dato = json.load(archivo)
        print(dato, type(dato))

# crear_archivo_2()