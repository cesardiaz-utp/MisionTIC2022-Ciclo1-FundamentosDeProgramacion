profesor = {
    "key": "value",
    "nombre": "Cesar",
    "nacionalidad": "Colombiano",
    "edad": 40
}

print(profesor)
profesor["nombre"] = "Cesar Diaz"
profesor["edad"] += 1
profesor["estudiante"] = { "nombre": "Edwin", "nota": 3.0}
print(profesor)
print("Nombre:",profesor["nombre"])
print("Nombre estudiante:",profesor["estudiante"]["nombre"])
