print("CRUD DE CONFERENCIAS Y EVENTOS EN PYTHON")
conferencias = [
    {"id": 1, "ponente": "Ing. Carlos Mendoza", "tema": "DevOps & CI/CD", "estado": "Confirmado"},
    {"id": 2, "ponente": "Dra. Sofía Alarcón", "tema": "Inteligencia Artificial", "estado": "Confirmado"},
    {"id": 3, "ponente": "Msc. Roberto Silva", "tema": "Ciberseguridad Ofensiva", "estado": "En Espera"},
]

id_publico = 4

def create():
    global id_publico
    print("Registrar Nueva Conferencia")
    ponente = input("Nombre del Ponente: ")
    tema = input("Tema de la Conferencia: ")
    estado = input("Estado (Confirmado, En Espera, Cancelado): ")
    nueva_conferencia = {
        "id": id_publico,
        "ponente": ponente,
        "tema": tema,
        "estado": estado
    }
    conferencias.append(nueva_conferencia)
    id_publico += 1

def read():
    print("Lista de Conferencias Registradas")
    for conferencia in conferencias:
        print(f"[{conferencia['id']}] Ponente: {conferencia['ponente']} | Tema: {conferencia['tema']} | Estado: {conferencia['estado']}")

def update():
    print("Actualizar Conferencia")
    id_update = int(input("ID de la conferencia a modificar: "))
    for conferencia in conferencias:
        if conferencia["id"] == id_update:
            conferencia["ponente"] = input("Nuevo Ponente: ")
            conferencia["tema"] = input("Nuevo Tema: ")
            conferencia["estado"] = input("Nuevo Estado: ")
            print("Conferencia actualizada exitosamente")
            return
    print("ID no encontrado")

def delete():
    print("Eliminar Conferencia")
    id_delete = int(input("ID de la conferencia a borrar: "))
    for conferencia in conferencias:
        if conferencia["id"] == id_delete:
            conferencias.remove(conferencia)
            print("Conferencia eliminada exitosamente")
            return
    print("ID no encontrado")

def menu():
    while True:
        print("\n--- GESTIÓN DE CONFERENCIAS ---")
        print("1. Registrar Conferencia")
        print("2. Listar Conferencias")
        print("3. Modificar Conferencia")
        print("4. Eliminar Conferencia")
        print("5. Salir")
        option = input("Seleccione una opción (1-5): ")
        if option == "1":
            create()
        elif option == "2":
            read()
        elif option == "3":
            update()
        elif option == "4":
            delete()
        elif option == "5":
            print("Cerrando el sistema de conferencias")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()