info_1 = {
    "id_cliente": 1,
    "nombre": "Johanna Fernandez",
    "edad": 20,
    "primer_ingreso": True
    }

info_2 = {
    "id_cliente": 1,
    "nombre": "Johanna Fernandez",
    "edad": 20,
    "primer_ingreso": False
    }

info_3 = {
    "id_cliente": 2,
    "nombre": "Gloria Suarez",
    "edad": 3,
    "primer_ingreso": True
    }

info_4 = {
    "id_cliente": 3,
    "nombre": "Tatiana Suarez",
    "edad": 17,
    "primer_ingreso": True
    }

info_5 = {
    "id_cliente": 3,
    "nombre": "Tatiana Suarez",
    "edad": 17,
    "primer_ingreso": False
    }

info_6 = {
    "id_cliente": 3,
    "nombre": "Tatiana Ruiz",
    "edad": 8,
    "primer_ingreso": True
    }

info_7 = {
    "id_cliente": 3,
    "nombre": "Tatiana Ruiz",
    "edad": 8,
    "primer_ingreso": False
    }



def cliente(informacion: dict) -> dict:
    
    retorno_diccionario = {
        "nombre": informacion["nombre"],
        "edad": informacion["edad"],
        'atracccion': "N\A",
        'apto': True,
        "primer_ingreso": informacion["primer_ingreso"],
        "total_boleta": "N\A" }
    
    
    if  retorno_diccionario['edad'] >= 7 and retorno_diccionario['edad'] < 15 :
        retorno_diccionario['atracccion'] = "Sillas Voladoras"
        if retorno_diccionario["primer_ingreso"] == True:
            vb = 10000 * .95
            retorno_diccionario["total_boleta"] = vb
        elif retorno_diccionario["primer_ingreso"] == False:
            vb = 10000
            retorno_diccionario["total_boleta"] = vb
    
    elif retorno_diccionario['edad'] >= 15 and retorno_diccionario['edad'] < 18 :
         retorno_diccionario['atracccion'] = "Carros Chocones"
         if retorno_diccionario["primer_ingreso"] == True:
            vb = 5000 * .93
            retorno_diccionario["total_boleta"] = vb
         elif retorno_diccionario["primer_ingreso"] == False:
            vb = 5000
            retorno_diccionario["total_boleta"] = vb
    
    elif retorno_diccionario['edad'] >= 18 :
         retorno_diccionario['atracccion'] = "X Treme"
         if retorno_diccionario["primer_ingreso"] == True:
            vb = 20000 * .95
            retorno_diccionario["total_boleta"] = vb
         elif retorno_diccionario["primer_ingreso"] == False:
            vb = 20000
            retorno_diccionario["total_boleta"] = vb
    else:
         retorno_diccionario['apto'] = False
         
        
    return retorno_diccionario
    
    
    


print(cliente(info_1))
print(cliente(info_2))
print(cliente(info_3))
print(cliente(info_4))
print(cliente(info_5))
print(cliente(info_6))
print(cliente(info_7))

