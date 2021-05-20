from datos import tareas

def create(identificador, tarea):    
    tareas[identificador] = tarea

def read() -> dict:
    return tareas

def read_one(identificador: str) -> dict:
    return tareas[identificador];

def estaElemento(identificador):
    #Extraer de la base de datos (contenedor) los identificadores
    conjuntoIdentificadores = set(tareas.keys())
    
    #Revisar si se encuentra el elemento solicitado        
#    if identificador in conjuntoIdentificadores:
#        return True
#    else:
#        return False
    return identificador in conjuntoIdentificadores
    
def update(identificador, tarea):
    tareas[identificador] = tarea

def delete(identificador):
    tareas.pop(identificador)