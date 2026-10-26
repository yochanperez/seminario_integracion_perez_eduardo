print("CRUD DE LISTAS EN PYTHON")
Avengers = [
    {"id": 1,"nombre":"Tony Stark", "heroe":"Iron Man", "estado":"Activo"},
    {"id": 2,"nombre":"Steve Rogers", "heroe":"Capitan America", "estado":"Activo"},
    {"id": 3,"nombre":"Thor Odison", "heroe":"Thor", "estado":"Activo"},
]

id_publico =4
def create():
    global id_publico
    print("Reclutar Avengers")
    nombre=input("Nomber Heroe:")
    heroe=input("Heroe: ")
    estado= input("Estado (Activo, Retirado, Desaparecido)")
    nuevo_avengers = {
        "id": id,
        "nombre":nombre,
        "heroe":heroe,
        "estado":estado
    }

    Avengers.append(nuevo_avengers)

def read():
    print("Listas de Avengers")
    print("Lista de Avengers")
    for avenger in Avengers:
        print(f"{avenger["id"]} - nombre : {avenger["nombre"]}")

def update():
    print("Actualizar Avengers")
    id_update = int (input("id a modificar"))
    for avenger in Avengers:
        if(avenger [id]==id_update):
            avenger["nombre"]= input("Nuevo Nombre")
            avenger["heroe"]= input("Nuevo Heroe")
            avenger["estado"]= input("Nuevo Estado")
            print("Actualizado")

def delete():
    print("Elimar Avenger")
    id_delete= int(input("id a borrar"))
    for avenger in Avengers:
        if (avenger[id]==id_delete):
            Avengers.remove(avenger)
            print("Avenger Elimminado")

def menu():
    while True:
        print("Avengers")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Borrar")
        print("5. Salir")
        option= input ("seleccione 1 al 5")
        if option=="1":
            create()
        elif option =="2":
            read()
        elif option== "3":
            update()
        elif option=="4":
            delete
        elif option=="5":
            print("Cerrando sistema")
            break
        else:
            print("No existe esa opcion")

if __name__ == "__main__":
    menu()