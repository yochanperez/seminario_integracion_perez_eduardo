print("Practica crud de listas")

Familia = [
    {"id":1,"nombre":"Rick Sanchez","rol":"Abuelo"},
    {"id":2,"nombre":"Morty Smith","rol":"Nieto"}
]

id_publico=4
def create():
    global id_publico
    print("Crear miembro de la familia")
    nombre= input("Nombre: ")
    rol= input("Rol: ")
    nuevo_miembro ={
        "id":id_publico,
        "nombre": nombre,
        "rol": rol
    }

    Familia.append(nuevo_miembro)
    id_publico +=1
    print("Miembro agregado exitosamente.")

def read():
    print("Lista de miembro de la familia")
    for miembro in Familia:
        print(f"{miembro['id']} - {miembro['nombre']} - {miembro['rol']}")

def update():
    print("Actualizar miembro de la familia")
    id_update = int(input("id a modificar: "))
    for miembro in Familia:
        if(miembro['id']==id_update):
            miembro["nombre"]= input("Nuevo miembro: ")
            miembro["rol"]= input("Nuevo rol: ")
            print("Actualizado")

def delete():
    print("Eliminar miembro de la familia")
    id_delete = int(input("id a eliminar: "))
    for miembro in Familia:
        if(miembro['id']==id_delete):
            Familia.remove(miembro)
            print("Miembro eliminado")

def menu():
    while True:
        print("Familia")
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
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()