from logica import *

def menu_principal():
    mainloop = True

    while mainloop: 
        print(" ")
        print("-- Aplicación CRUD TareasPendientes ---")
        print("1. Listar tareas")
        print("2. Consultar una tarea")
        print("3. Adicionar Tarea")
        print("4. Actualizar Tarea")
        print("5. Eliminar Tarea")
        print("0. Salir")

        entrada = True
        while entrada:
            try:
                opcion = int(input("Ingrese una opción: "))
                if opcion in range(6):
                    entrada = False
                else:
                    print("Numero de opción inválido. Intente de nuevo.")
            except:
                print("La entrada no es válida. Intenta de nuevo.")
        
        if opcion == 1:
            listar_tareas()
        elif opcion == 2:
            consultar_tarea()
        elif opcion == 3:
            adicionar_tarea()
        elif opcion == 4:
            actualizar_tarea()
        elif opcion == 5:
            eliminar_tarea()
        elif opcion == 0:
            mainloop = False
            print("Ha salido exitosamente.")
        else:
            print("Valor inválido!")

def imprimir_tarea(identificador, tarea): 
    print(identificador," - ",end="")
    for nombre_atributo, atributo in tarea.items():
        print(atributo, ", ", end="")
    print()

def listar_tareas():
    print()
    print("->Listado de Tareas")
    print()

    tareas = read()
    for identificador, tarea in tareas.items(): # (key, value)
        imprimir_tarea(identificador, tarea)
    
    input("Presiona Enter para continuar.")

def consultar_tarea():
    print()
    print("->Consultar Tarea")
    print()

    #Solicitar al usuario el identificador
    identificador = input("Ingrese identificador de la Tarea para modificar: ")
   
    #Lectura de tareas
    if estaElemento(identificador):
        tarea = read_one(identificador)
        imprimir_tarea(identificador, tarea)
    else:
        print("No ha sido encontrada la Tarea!")

    input("Presiona Enter para continuar.")

def adicionar_tarea():
    print()
    print("->Adicionando Tarea")        
    print()
    
    identificador = input("Ingrese identificador de la Tarea: ")
    
    descripcion = input("Ingrese descripción de Tarea: ")
    estado = input("Ingrese el estado inicial de la Tarea: ")
    tiempo = int(input("Ingrese el tiempo de realización: "))
    
    tareaNueva = {
        "descripcion":descripcion,
        "estado" : estado,
        "tiempo" : tiempo
    }
    
    #Adicionar la tarea
    create(identificador, tareaNueva)

    print("Tarea agregada exitosamente!")

    input("Presiona Enter para continuar.")

def actualizar_tarea():
    print()
    print("->Actualizar Tarea")
    print()
    
    #Solicitar al usuario el identificador
    identificador = input("Ingrese identificador de la Tarea para modificar: ")        

    #Revisar si se encuentra el elemento solicitado        
    if estaElemento(identificador):
        try:
            tarea = read_one(identificador)

            # Mostrar la información actual
            imprimir_tarea(identificador, tarea)
            
            #Capturar los campos de interés
            nuevaDescripcion = input("Nueva descripción: ")
            if nuevaDescripcion:
                tarea["descripcion"] = nuevaDescripcion

            nuevoEstado = input("Nuevo estado: ")
            if nuevoEstado:
                tarea["estado"] = nuevoEstado

            nuevoTiempo = input("Nuevo tiempo: ")
            if nuevoTiempo:
                tarea["tiempo"] = int(nuevoTiempo)

            update(identificador, tarea)            

            print("Tarea modificada exitosamente!")
        except:
            print("Ocurrio un error al actualizar la tarea")
    else:
        print("No ha sido encontrada la Tarea!")

    input("Presiona Enter para continuar.")

def eliminar_tarea():
    print()
    print("->Eliminar Tarea")
    print()
    
    #Solicitar al usuario el identificador
    identificador = input("Ingrese identificador de la Tarea para eliminar: ")

    #Revisar si se encuentra el elemento solicitado        
    if estaElemento(identificador):
        delete(identificador)

        print("Tarea eliminada exitosamente!")
    else:
        print("No ha sido encontrada la Tarea!")

    input("Presiona Enter para continuar.")

menu_principal()