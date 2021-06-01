def mostrar_mensaje(mensaje=''):
    print()
    print(mensaje)
    print()

def mostrar_error(mensaje=''):
    print("Ha ocurrido un problema:", mensaje)
    print()

def espera_enter():
    leer_cadena("Presiona Enter para continuar.")

def leer_cadena(mensaje="Ingrese un valor: "):
    return input(mensaje)

def leer_entero(mensaje="Ingrese un valor: ", opcional = False):
    valor = None
    if not opcional:
        while valor == None:
            try:
                valor = int(input(mensaje))
            except:        
                print("Entrada inválida: Se debe ingresar una opción numérica.") 
    else:
        try:
            valor = int(input(mensaje))
        except:
            valor = None

    return valor

def imprimir_tarea(tarea: dict): 
    identificador = tarea["id"]
    print(identificador,"->",end="\t")
    for key, atributo in tarea.items():
        if key == "id":
            continue
        print(atributo, end="\t")
    print()

def opcion_menu_principal():
    print(" ")
    print("-- Aplicación CRUD TareasPendientes ---")
    print("1. Listar tareas")
    print("2. Consultar una tarea")
    print("3. Adicionar Tarea")
    print("4. Actualizar Tarea")
    print("5. Eliminar Tarea")
    print("0. Salir")

    valor = None
    while valor == None:
        valor = leer_entero("Ingrese una opción: ")
        if valor not in range(6):
            print("Numero de opción inválido. Intente de nuevo.")
            valor = None

    return valor

