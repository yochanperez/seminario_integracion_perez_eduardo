
print("Practica para crud de listas")

Liga_justicia = [
    {"id":1,"nombre":"Clark Kent","heroe":"Superman","estado":"Activo"},
    {"id":2,"nombre":"Bruce Wayne","heroe":"Batman","estado":"Activo"},
    {"id":3,"nombre":"Diana","heroe":"Wonder Woman","estado":"Activo"},
]

id_publico=4

def create():
    global id_publico
    print("Reclutar Liga de la justicia")
    nombre= input("Nombre Heroe: ")
    heroe= input("Heroe: ")
    estado= input("Estado (Activo, Retirado, Desaparecido): ")
    nuevo_heroe ={
        "id": id_publico,
        "nombre":nombre,
        "heroe":heroe,
        "estado":estado
    }

    Liga_justicia.append(nuevo_heroe)
    id_publico += 1
    print("Heroe reclutado exitosamente.")

def read():
    print("Lista de Liga de la justicia")
    for liga in Liga_justicia:
        print(f"{liga['id']} - nombre: {liga['nombre']}")

def update():
    print("Actualizar Liga de la justicia")
    id_update= int(input("id a modificar: "))
    for liga in Liga_justicia:
        if(liga['id']==id_update):
            liga["nombre"]=input("Nuevo Nombre: ")
            liga["heroe"]=input("Nuevo Heroe: ")
            liga["estado"]=input("Nuevo estado: ")
            print("Actualizado")

def delete():
    print("Eliminar miembro de la liga de la justicia")
    id_delete=int(input("id a borrar: "))
    for liga in Liga_justicia:
        if(liga['id']==id_delete):
            Liga_justicia.remove(liga)
            print("Miembro eliminado")

def menu():
    while True:
        print("Liga de la justicia")
        print("1. Crear")
        print("2. Leer")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")
        option= input("Seleccione una opción (1-5): ")
        if option=="1":
            create()
        elif option=="2":
            read()
        elif option=="3":
            update()
        elif option=="4":
            delete()
        elif option=="5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()