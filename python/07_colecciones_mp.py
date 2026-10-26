salas = ["Auditorio Principal", "Sala de Prensa", "Laboratorio Cloud"]
print("Salas: ", salas)
print("tipo: ", type(salas))

print("Tuplas")
horarios = (9, 14, 18)
print("horarios: ", horarios)
print("tipo: ", type(horarios))

print("Diccionario")
conferencia = {
    "titulo": "Arquitectura de Software y Cloud",
    "area": "Ingeniería de Sistemas",
    "disponible": True
}
print("conferencia: ", conferencia)
print("tipo: ", type(conferencia))

print("Conjunto")
tracks = {
    "Ciberseguridad",
    "Inteligencia Artificial",
    "DevOps"
}
print("tracks: ", tracks)
print("tipo: ", type(tracks))

print("CRUD DE LISTAS EN PYTHON")
conferencias = [
    {"id": 1, "ponente": "Ing. Carlos Mendoza", "tema": "DevOps & CI/CD", "estado": "Confirmado"},
    {"id": 2, "ponente": "Dra. Sofía Alarcón", "tema": "Inteligencia Artificial", "estado": "Confirmado"},
    {"id": 3, "ponente": "Msc. Roberto Silva", "tema": "Ciberseguridad Ofensiva", "estado": "En Espera"},
]

id_publico = 4

def create():
    id_registro = 4
    print("Registrar Nueva Conferencia")
    ponente = input("Nombre del Ponente: ")
    tema = input("Tema de la Conferencia: ")
    estado = input("Estado (Confirmado, En Espera, Cancelado): ")
    nueva_conferencia = {
        "id": id_registro,
        "ponente": ponente,
        "tema": tema,
        "estado": estado
    }
    conferencias.append(nueva_conferencia)